https://docs.opencv.org/4.x/dc/d4d/tutorial_py_table_of_contents_gui.html

#=============================================================================

Simple image loading: 

import cv2 as cv
import sys

img = cv.imread(cv.samples.findFile("starry_night.jpg")) #cv::imread beolvassa, de cv::immat-ba van elmentve utána
if img is None:
    sys.exit("Could not read the image.")
cv.imshow("Display window", img) #imshow: megjelenítés
k = cv.waitKey(0) #waitkey - csak akkor lép ki, ha van billentyű leütés, egyébként egyből kilépne és nem látnánk a képet
if k == ord("s"):
    cv.imwrite("starry_night.png", img) #save it 

#=============================================================================

Capture video from camera 

To capture a video, you need to create a VideoCapture object. Its argument can be either the device index or the name of a video file. A device index is just the number to specify which camera. Normally one camera will be connected (as in my case). So I simply pass 0 (or -1). You can select the second camera by passing 1 and so on. After that, you can capture frame-by-frame. But at the end, don't forget to release the capture. 


import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0) #kamera index
if not cap.isOpened(): # ha meg van nyitva - true / false-t dob vissza | cap.open() - sima megnyitás 
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY) #cv.cvtColor - színválasztás
    # Display the resulting frame
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()

#=============================================================================

Playing Video from file

Playing video from file is the same as capturing it from camera, just change the camera index to a video file name. Also while displaying the frame, use appropriate time for cv.waitKey(). If it is too less, video will be very fast and if it is too high, video will be slow (Well, that is how you can display videos in slow motion). 25 milliseconds will be OK in normal cases. 


import numpy as np
import cv2 as cv
cap = cv.VideoCapture('vtest.avi')
while cap.isOpened():
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()

#=============================================================================

Saving a video

This time we create a VideoWriter object. We should specify the output file name (eg: output.avi). Then we should specify the FourCC code (details in next paragraph). Then number of frames per second (fps) and frame size should be passed. And the last one is the isColor flag. If it is True, the encoder expect color frame, otherwise it works with grayscale frame.

FourCC code is passed as `cv.VideoWriter_fourcc('M','J','P','G')or cv.VideoWriter_fourcc(*'MJPG')` for MJPG.

The below code captures from a camera, flips every frame in the vertical direction, and saves the video. 

import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)
# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi', fourcc, 20.0, (640,  480))
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    frame = cv.flip(frame, 0)
    # write the flipped frame
    out.write(frame)
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break
# Release everything if job is finished
cap.release()
out.release()
cv.destroyAllWindows()

#=============================================================================

Drawing Functions in OpenCV 
#https://docs.opencv.org/4.x/dc/da5/tutorial_py_drawing_functions.html

img : The image where you want to draw the shapes
color : Color of the shape. for BGR, pass it as a tuple, eg: (255,0,0) for blue. For grayscale, just pass the scalar value.
thickness : Thickness of the line or circle etc. If -1 is passed for closed figures like circles, it will fill the shape. default thickness = 1
lineType : Type of line, whether 8-connected, anti-aliased line etc. By default, it is 8-connected. cv.LINE_AA gives anti-aliased line which looks great for curves


# Draw a diagonal blue line with thickness of 5 px
cv.line(img,(0,0),(511,511),(255,0,0),5)

# Draw a blue rectangle
cv.rectangle(img,(384,0),(510,128),(0,255,0),3) #(384,0) - kép jobb felső koordinátája, (512,128) - kép bal alsó koordinátája

#Draw an eclipse 
#https://docs.opencv.org/4.x/d6/d6e/group__imgproc__draw.html#ga28b2267d35786f5f890ca167236cbc69
cv.ellipse(img,(256,256),(100,50),0,0,180,255,-1)


Add text to images: 

To put texts in images, you need specify following things.

    Text data that you want to write
    Position coordinates of where you want put it (i.e. bottom-left corner where data starts).
    Font type (Check cv.putText() docs for supported fonts)
    Font Scale (specifies the size of font)
    regular things like color, thickness, lineType etc. For better look, lineType = cv.LINE_AA is recommended.


font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv.LINE_AA)

#=============================================================================
