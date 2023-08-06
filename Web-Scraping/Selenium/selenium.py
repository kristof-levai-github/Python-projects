from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#https://www.youtube.com/watch?v=o3tYiyE_OXE&t=11880s#

#======================================================================================

driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver.exe")

#======================================================================================

driver.get("https://www.randombookclub.co.uk/") #get the page itself
print(driver.title) #get the title of the page
print(driver.current_url) #get the current url
#print(driver.page_source) #html code for the page

#======================================================================================

#Navigating, Finding elements and inputs!
time.sleep(3)

driver.get("https://www.tripadvisor.com/ShowUserReviews-g551960-d4173908-r314069604-The_Book_Shop-Wigtown_Newton_Stewart_Dumfries_and_Galloway_Scotland.html")

#két megnyitott page között tudunk előre és hátra lépkedni, plusz tudjuk refreshelni is
print(driver.title)
driver.back() # vissza lép az előző url-re
print(driver.title)

time.sleep(3)

driver.forward() #egy url-t előre megy ha van még url
print(driver.title)
#driver.refresh()


time.sleep(5)


driver.get("https://www.randombookclub.co.uk/contact-us/")
ele = driver.find_element(By.NAME, "contact_name") #egy elementet megkeres az adott oldalon a neve alapján
element = driver.find_element(By.ID, "contact_email") #egy elementet megkeres az adott oldalon az ID-ja alapján
#+ by.TAG_NAME = az oldalon minden olyan taget megkeres
#element = driver.find_element(By.CSS_SELECTOR, "input#hint required email")

login_form = driver.find_element(By.XPATH, "/html/body/form[1]")  #relatív vagy abszolút elérést lehet vele megadni input után
#és ha több egyező van XPATH-nál, akkor csak az első értéket adja vissza , de king, mert lehet vele keresni 3.-ra is pl

print(ele.is_displayed()) #true or false -> vagy van a pagen, vagy nincs
print(ele.is_enabled()) #true or false ez is

#======================================================================================

#interacting with elements

ele.send_keys("some text") #az element objektbe ír
element.send_keys(" and some", Keys.ARROW_DOWN) #az element objektbe ír, majd lenyom egy gombot
element.clear() #sima törlés a textboxból


#======================================================================================

#Filling out forms

#pl: az első selectet megkeresi, annak minden optionjának megnézi az értékét

element = driver.find_element(By.XPATH, "//select[@name='name']")
all_options = element.find_elements(By.TAG_NAME, "option")
for option in all_options:
    print("Value is: %s" % option.get_attribute("value"))
    option.click()

#SELECT method:

from selenium.webdriver.support.ui import Select
select = Select(driver.find_element(By.NAME, 'name'))
select.select_by_index(index) #pl: dropdown menüknél
select.select_by_visible_text("text")
select.select_by_value(value)

select = Select(driver.find_element(By.ID, 'id'))
select.deselect_all()

#Minden opció:
options = select.options

#Beküldés:
element.submit()

#======================================================================================

#Drag and drop

#You can use drag and drop, either moving an element by a certain amount, or on to another element:

element = driver.find_element(By.NAME, "source")
target = driver.find_element(By.NAME, "target")

from selenium.webdriver import ActionChains
action_chains = ActionChains(driver)
action_chains.drag_and_drop(element, target).perform()

#======================================================================================

#Other Mouse Actions

action = ActionChains()

action.move_to_element(action_chains).move_to_element(element).click().perform() #elementről elemekre mozgatja az egeret | kell a perform() a click után hogy végre hajtsa
action.double_click(element).perform() #double click
action.context_click(element).perform() #right click

#======================================================================================

#Scrolling

#Scroll down the page by pixels
driver.execute_script("window.scrollBy(0,500)","")

#Scroll down the page till element found
driver.execute_script("arguments[0].scrollIntoView();", Element)

#Scroll down till the end of the page
driver.execute_script("window.scrollBy(0, document.body.scollHeight)")

#======================================================================================

#Navigálás több ablak között :

driver.switch_to_window("windowName")
driver.switch_to_frame("frameName")

driver.switch_to_default_content() #kilépés a framekből

#======================================================================================
#Felugró ablakok közötti váltás (popup)

alert = driver.switch_to.alert

#======================================================================================


#Waits
#főleg ajax betöltés miatt kell várni

#Selenium Webdriver provides two types of waits - implicit & explicit.
# An explicit wait makes WebDriver wait for a certain condition to occur before proceeding further with execution. An implicit wait makes WebDriver poll the DOM for a certain amount of time when trying to locate an element.

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Explicit:

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "myDynamicElement"))
    )
finally:
    driver.quit()


#Implicit:

driver.implicitly_wait(10) # seconds
driver.get("http://somedomain/url_that_delays_loading")
myDynamicElement = driver.find_element_by_id("myDynamicElement")

#======================================================================================

#Screenshots

driver.get('http://www.python.org/')
driver.save_screenshot('screenshot.png')



#======================================================================================

driver.close() # close the browser
driver.quit() #close all the browsers

#======================================================================================