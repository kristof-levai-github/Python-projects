import cv2 as cv
import pyautogui
from time import sleep, time
from threading import Thread, Lock
from math import sqrt


class BotState:
    INITIALIZING = 0
    SEARCHING = 1
    MOVING = 2
    MINING = 3
    BACKTRACKING = 4


class AlbionBot:
    
    # constants
    INITIALIZING_SECONDS = 6
    MINING_SECONDS = 14
    MOVEMENT_STOPPED_THRESHOLD = 0.975
    IGNORE_RADIUS = 130
    TOOLTIP_MATCH_THRESHOLD = 0.72

    # threading properties
    stopped = True
    lock = None

    # properties
    state = None
    targets = []
    screenshot = None
    timestamp = None
    movement_screenshot = None
    window_offset = (0,0)
    window_w = 0
    window_h = 0
    limestone_tooltip = None
    click_history = []

    def __init__(self, window_offset, window_size):
        # create a thread lock object
        self.lock = Lock()

        # for translating window positions into screen positions, it's easier to just
        # get the offsets and window size from WindowCapture rather than passing in 
        # the whole object
        self.window_offset = window_offset
        self.window_w = window_size[0]
        self.window_h = window_size[1]

        # pre-load the needle image used to confirm our object detection
        self.limestone_tooltip = cv.imread('limestone_tooltip.jpg', cv.IMREAD_UNCHANGED)

        # start bot in the initializing mode to allow us time to get setup.
        # mark the time at which this started so we know when to complete it
        self.state = BotState.INITIALIZING
        self.timestamp = time()

    def click_next_target(self):
        # 1. order targets by distance from center
        # loop:
        #   2. hover over the nearest target
        #   3. confirm that it's limestone via the tooltip
        #   4. if it's not, check the next target
        # endloop
        # 5. if no target was found return false
        # 6. click on the found target and return true
        targets = self.targets_ordered_by_distance(self.targets)

        target_i = 0
        found_limestone = False
        while not found_limestone and target_i < len(targets):
            # if we stopped our script, exit this loop
            if self.stopped:
                break

            # load up the next target in the list and convert those coordinates
            # that are relative to the game screenshot to a position on our
            # screen
            target_pos = targets[target_i]
            screen_x, screen_y = self.get_screen_position(target_pos)
            print('Moving mouse to x:{} y:{}'.format(screen_x, screen_y))

            # move the mouse
            pyautogui.moveTo(x=screen_x, y=screen_y)
            # short pause to let the mouse movement complete and allow
            # time for the tooltip to appear
            sleep(1.250)
            # confirm limestone tooltip
            if self.confirm_tooltip(target_pos):
                print('Click on confirmed target at x:{} y:{}'.format(screen_x, screen_y))
                found_limestone = True
                pyautogui.click()
                # save this position to the click history
                self.click_history.append(target_pos)
            target_i += 1

        return found_limestone

    def have_stopped_moving(self):
        # if we haven't stored a screenshot to compare to, do that first
        if self.movement_screenshot is None:
            self.movement_screenshot = self.screenshot.copy()
            return False

        # compare the old screenshot to the new screenshot
        result = cv.matchTemplate(self.screenshot, self.movement_screenshot, cv.TM_CCOEFF_NORMED)
        # we only care about the value when the two screenshots are laid perfectly over one 
        # another, so the needle position is (0, 0). since both images are the same size, this
        # should be the only result that exists anyway
        similarity = result[0][0]
        print('Movement detection similarity: {}'.format(similarity))

        if similarity >= self.MOVEMENT_STOPPED_THRESHOLD:
            # pictures look similar, so we've probably stopped moving
            print('Movement detected stop')
            return True

        # looks like we're still moving.
        # use this new screenshot to compare to the next one
        self.movement_screenshot = self.screenshot.copy()
        return False

    def targets_ordered_by_distance(self, targets):
        # our character is always in the center of the screen
        my_pos = (self.window_w / 2, self.window_h / 2)
        # searched "python order points by distance from point"
        # simply uses the pythagorean theorem
        # https://stackoverflow.com/a/30636138/4655368
        def pythagorean_distance(pos):
            return sqrt((pos[0] - my_pos[0])**2 + (pos[1] - my_pos[1])**2)
        targets.sort(key=pythagorean_distance)

        # print(my_pos)
        # print(targets)
        # for t in targets:
        #    print(pythagorean_distance(t))

        # ignore targets at are too close to our character (within 130 pixels) to avoid 
        # re-clicking a deposit we just mined
        targets = [t for t in targets if pythagorean_distance(t) > self.IGNORE_RADIUS]

        return targets

    def confirm_tooltip(self, target_position):
        # check the current screenshot for the limestone tooltip using match template
        result = cv.matchTemplate(self.screenshot, self.limestone_tooltip, cv.TM_CCOEFF_NORMED)
        # get the best match postition
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        # if we can closely match the tooltip image, consider the object found
        if max_val >= self.TOOLTIP_MATCH_THRESHOLD:
            # print('Tooltip found in image at {}'.format(max_loc))
            # screen_loc = self.get_screen_position(max_loc)
            # print('Found on screen at {}'.format(screen_loc))
            # mouse_position = pyautogui.position()
            # print('Mouse on screen at {}'.format(mouse_position))
            # offset = (mouse_position[0] - screen_loc[0], mouse_position[1] - screen_loc[1])
            # print('Offset calculated as x: {} y: {}'.format(offset[0], offset[1]))
            # the offset I always got was Offset calculated as x: -22 y: -29
            return True
        #print('Tooltip not found.')
        return False

    def click_backtrack(self):
        # pop the top item off the clicked points stack. this will be the click that
        # brought us to our current location.
        last_click = self.click_history.pop()
        # to undo this click, we must mirror it across the center point. so if our
        # character is at the middle of the screen at ex. (100, 100), and our last
        # click was at (120, 120), then to undo this we must now click at (80, 80).
        # our character is always in the center of the screen
        my_pos = (self.window_w / 2, self.window_h / 2)
        mirrored_click_x = my_pos[0] - (last_click[0] - my_pos[0])
        mirrored_click_y = my_pos[1] - (last_click[1] - my_pos[1])
        # convert this screenshot position to a screen position
        screen_x, screen_y = self.get_screen_position((mirrored_click_x, mirrored_click_y))
        print('Backtracking to x:{} y:{}'.format(screen_x, screen_y))
        pyautogui.moveTo(x=screen_x, y=screen_y)
        # short pause to let the mouse movement complete
        sleep(0.500)
        pyautogui.click()

    # translate a pixel position on a screenshot image to a pixel position on the screen.
    # pos = (x, y)
    # WARNING: if you move the window being captured after execution is started, this will
    # return incorrect coordinates, because the window position is only calculated in
    # the WindowCapture __init__ constructor.
    def get_screen_position(self, pos):
        return (pos[0] + self.window_offset[0], pos[1] + self.window_offset[1])

    # threading methods

    def update_targets(self, targets):
        self.lock.acquire()
        self.targets = targets
        self.lock.release()

    def update_screenshot(self, screenshot):
        self.lock.acquire()
        self.screenshot = screenshot
        self.lock.release()

    def start(self):
        self.stopped = False
        t = Thread(target=self.run)
        t.start()

    def stop(self):
        self.stopped = True

    # main logic controller
    def run(self):
        while not self.stopped:
            if self.state == BotState.INITIALIZING:
                # do no bot actions until the startup waiting period is complete
                if time() > self.timestamp + self.INITIALIZING_SECONDS:
                    # start searching when the waiting period is over
                    self.lock.acquire()
                    self.state = BotState.SEARCHING
                    self.lock.release()

            elif self.state == BotState.SEARCHING:
                # check the given click point targets, confirm a limestone deposit,
                # then click it.
                success = self.click_next_target()
                # if not successful, try one more time
                if not success:
                    success = self.click_next_target()

                # if successful, switch state to moving
                # if not, backtrack or hold the current position
                if success:
                    self.lock.acquire()
                    self.state = BotState.MOVING
                    self.lock.release()
                elif len(self.click_history) > 0:
                    self.click_backtrack()
                    self.lock.acquire()
                    self.state = BotState.BACKTRACKING
                    self.lock.release()
                else:
                    # stay in place and keep searching
                    pass

            elif self.state == BotState.MOVING or self.state == BotState.BACKTRACKING:
                # see if we've stopped moving yet by comparing the current pixel mesh
                # to the previously observed mesh
                if not self.have_stopped_moving():
                    # wait a short time to allow for the character position to change
                    sleep(0.500)
                else:
                    # reset the timestamp marker to the current time. switch state
                    # to mining if we clicked on a deposit, or search again if we
                    # backtracked
                    self.lock.acquire()
                    if self.state == BotState.MOVING:
                        self.timestamp = time()
                        self.state = BotState.MINING
                    elif self.state == BotState.BACKTRACKING:
                        self.state = BotState.SEARCHING
                    self.lock.release()
                
            elif self.state == BotState.MINING:
                # see if we're done mining. just wait some amount of time
                if time() > self.timestamp + self.MINING_SECONDS:
                    # return to the searching state
                    self.lock.acquire()
                    self.state = BotState.SEARCHING
                    self.lock.release()






DETECTION.PY



import cv2 as cv
from threading import Thread, Lock


class Detection:

    # threading properties
    stopped = True
    lock = None
    rectangles = []
    # properties
    cascade = None
    screenshot = None

    def __init__(self, model_file_path):
        # create a thread lock object
        self.lock = Lock()
        # load the trained model
        self.cascade = cv.CascadeClassifier(model_file_path)

    def update(self, screenshot):
        self.lock.acquire()
        self.screenshot = screenshot
        self.lock.release()

    def start(self):
        self.stopped = False
        t = Thread(target=self.run)
        t.start()

    def stop(self):
        self.stopped = True

    def run(self):
        # TODO: you can write your own time/iterations calculation to determine how fast this is
        while not self.stopped:
            if not self.screenshot is None:
                # do object detection
                rectangles = self.cascade.detectMultiScale(self.screenshot)
                # lock the thread while updating the results
                self.lock.acquire()
                self.rectangles = rectangles
                self.lock.release()








MAIN.PY


import cv2 as cv
import numpy as np
import os
from time import time
from windowcapture import WindowCapture
from detection import Detection
from vision import Vision
from bot import AlbionBot, BotState

# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their 
# own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))


DEBUG = True

# initialize the WindowCapture class
wincap = WindowCapture('Albion Online Client')
# load the detector
detector = Detection('limestone_model_final.xml')
# load an empty Vision class
vision = Vision()
# initialize the bot
bot = AlbionBot((wincap.offset_x, wincap.offset_y), (wincap.w, wincap.h))

wincap.start()
detector.start()
bot.start()

while(True):

    # if we don't have a screenshot yet, don't run the code below this point yet
    if wincap.screenshot is None:
        continue

    # give detector the current screenshot to search for objects in
    detector.update(wincap.screenshot)

    # update the bot with the data it needs right now
    if bot.state == BotState.INITIALIZING:
        # while bot is waiting to start, go ahead and start giving it some targets to work
        # on right away when it does start
        targets = vision.get_click_points(detector.rectangles)
        bot.update_targets(targets)
    elif bot.state == BotState.SEARCHING:
        # when searching for something to click on next, the bot needs to know what the click
        # points are for the current detection results. it also needs an updated screenshot
        # to verify the hover tooltip once it has moved the mouse to that position
        targets = vision.get_click_points(detector.rectangles)
        bot.update_targets(targets)
        bot.update_screenshot(wincap.screenshot)
    elif bot.state == BotState.MOVING:
        # when moving, we need fresh screenshots to determine when we've stopped moving
        bot.update_screenshot(wincap.screenshot)
    elif bot.state == BotState.MINING:
        # nothing is needed while we wait for the mining to finish
        pass

    if DEBUG:
        # draw the detection results onto the original image
        detection_image = vision.draw_rectangles(wincap.screenshot, detector.rectangles)
        # display the images
        cv.imshow('Matches', detection_image)

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    key = cv.waitKey(1)
    if key == ord('q'):
        wincap.stop()
        detector.stop()
        bot.stop()
        cv.destroyAllWindows()
        break

print('Done.')





VISION.PY





import cv2 as cv
import numpy as np


class Vision:

    # given a list of [x, y, w, h] rectangles returned by find(), convert those into a list of
    # [x, y] positions in the center of those rectangles where we can click on those found items
    def get_click_points(self, rectangles):
        points = []

        # Loop over all the rectangles
        for (x, y, w, h) in rectangles:
            # Determine the center position
            center_x = x + int(w/2)
            center_y = y + int(h/2)
            # Save the points
            points.append((center_x, center_y))

        return points

    # given a list of [x, y, w, h] rectangles and a canvas image to draw on, return an image with
    # all of those rectangles drawn
    def draw_rectangles(self, haystack_img, rectangles):
        # these colors are actually BGR
        line_color = (0, 255, 0)
        line_type = cv.LINE_4

        for (x, y, w, h) in rectangles:
            # determine the box positions
            top_left = (x, y)
            bottom_right = (x + w, y + h)
            # draw the box
            cv.rectangle(haystack_img, top_left, bottom_right, line_color, lineType=line_type)

        return haystack_img

    # given a list of [x, y] positions and a canvas image to draw on, return an image with all
    # of those click points drawn on as crosshairs
    def draw_crosshairs(self, haystack_img, points):
        # these colors are actually BGR
        marker_color = (255, 0, 255)
        marker_type = cv.MARKER_CROSS

        for (center_x, center_y) in points:
            # draw the center point
            cv.drawMarker(haystack_img, (center_x, center_y), marker_color, marker_type)

        return haystack_img

    def centeroid(self, point_list):
        point_list = np.asarray(point_list, dtype=np.int32)
        length = point_list.shape[0]
        sum_x = np.sum(point_list[:, 0])
        sum_y = np.sum(point_list[:, 1])
        return [np.floor_divide(sum_x, length), np.floor_divide(sum_y, length)]







WINDOWCAPTURE.PY


import numpy as np
import win32gui, win32ui, win32con
from threading import Thread, Lock


class WindowCapture:

    # threading properties
    stopped = True
    lock = None
    screenshot = None
    # properties
    w = 0
    h = 0
    hwnd = None
    cropped_x = 0
    cropped_y = 0
    offset_x = 0
    offset_y = 0

    # constructor
    def __init__(self, window_name=None):
        # create a thread lock object
        self.lock = Lock()

        # find the handle for the window we want to capture.
        # if no window name is given, capture the entire screen
        if window_name is None:
            self.hwnd = win32gui.GetDesktopWindow()
        else:
            self.hwnd = win32gui.FindWindow(None, window_name)
            if not self.hwnd:
                raise Exception('Window not found: {}'.format(window_name))

        # get the window size
        window_rect = win32gui.GetWindowRect(self.hwnd)
        self.w = window_rect[2] - window_rect[0]
        self.h = window_rect[3] - window_rect[1]

        # account for the window border and titlebar and cut them off
        border_pixels = 8
        titlebar_pixels = 30
        self.w = self.w - (border_pixels * 2)
        self.h = self.h - titlebar_pixels - border_pixels
        self.cropped_x = border_pixels
        self.cropped_y = titlebar_pixels

        # set the cropped coordinates offset so we can translate screenshot
        # images into actual screen positions
        self.offset_x = window_rect[0] + self.cropped_x
        self.offset_y = window_rect[1] + self.cropped_y

    def get_screenshot(self):

        # get the window image data
        wDC = win32gui.GetWindowDC(self.hwnd)
        dcObj = win32ui.CreateDCFromHandle(wDC)
        cDC = dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, self.w, self.h)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0, 0), (self.w, self.h), dcObj, (self.cropped_x, self.cropped_y), win32con.SRCCOPY)

        # convert the raw data into a format opencv can read
        #dataBitMap.SaveBitmapFile(cDC, 'debug.bmp')
        signedIntsArray = dataBitMap.GetBitmapBits(True)
        img = np.fromstring(signedIntsArray, dtype='uint8')
        img.shape = (self.h, self.w, 4)

        # free resources
        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())

        # drop the alpha channel, or cv.matchTemplate() will throw an error like:
        #   error: (-215:Assertion failed) (depth == CV_8U || depth == CV_32F) && type == _templ.type() 
        #   && _img.dims() <= 2 in function 'cv::matchTemplate'
        img = img[...,:3]

        # make image C_CONTIGUOUS to avoid errors that look like:
        #   File ... in draw_rectangles
        #   TypeError: an integer is required (got type tuple)
        # see the discussion here:
        # https://github.com/opencv/opencv/issues/14866#issuecomment-580207109
        img = np.ascontiguousarray(img)

        return img

    # find the name of the window you're interested in.
    # once you have it, update window_capture()
    # https://stackoverflow.com/questions/55547940/how-to-get-a-list-of-the-name-of-every-open-window
    @staticmethod
    def list_window_names():
        def winEnumHandler(hwnd, ctx):
            if win32gui.IsWindowVisible(hwnd):
                print(hex(hwnd), win32gui.GetWindowText(hwnd))
        win32gui.EnumWindows(winEnumHandler, None)

    # translate a pixel position on a screenshot image to a pixel position on the screen.
    # pos = (x, y)
    # WARNING: if you move the window being captured after execution is started, this will
    # return incorrect coordinates, because the window position is only calculated in
    # the __init__ constructor.
    def get_screen_position(self, pos):
        return (pos[0] + self.offset_x, pos[1] + self.offset_y)

    # threading methods

    def start(self):
        self.stopped = False
        t = Thread(target=self.run)
        t.start()

    def stop(self):
        self.stopped = True

    def run(self):
        # TODO: you can write your own time/iterations calculation to determine how fast this is
        while not self.stopped:
            # get an updated image of the game
            screenshot = self.get_screenshot()
            # lock the thread while updating the results
            self.lock.acquire()
            self.screenshot = screenshot
            self.lock.release()
