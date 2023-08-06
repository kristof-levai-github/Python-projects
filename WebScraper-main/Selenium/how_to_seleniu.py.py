import requests
###--------------------- IMPORTS ---------------------
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

###--------------------- DOCS ---------------------

#https://selenium-python.readthedocs.io/locating-elements.html

######--------------------- REQUESTS ---------------------

url = 'https://www.google.com/'

response = requests.get(url)
r = response.text

### --------------------- NAVIGATING ---------------------

###getting the driver path
driver = webdriver.Chrome(executable_path="C:\\Users\\ADMIN\\Desktop\\python\\web\\chromedriver")

###getting the url and the source page
driver.get(url)

###getting the source page
ps = driver.page_source

### --------------------- FINDING AN ELEMENT ---------------------

#Example input: <input type="text" name="passwd" id="passwd-id" />

element = driver.find_element(By.ID, "passwd-id")
element = driver.find_element(By.NAME, "passwd")
element = driver.find_element(By.XPATH, "//input[@id='passwd-id']")
element = driver.find_element(By.CSS_SELECTOR, "input#passwd-id")

###ALL TAGS:

'''
find_element(By.ID, "id")
find_element(By.NAME, "name")
find_element(By.XPATH, "xpath")
find_element(By.LINK_TEXT, "link text")
find_element(By.PARTIAL_LINK_TEXT, "partial link text")
find_element(By.TAG_NAME, "tag name")
find_element(By.CLASS_NAME, "class name")
find_element(By.CSS_SELECTOR, "css selector")
'''

### --------------------- FINDING MULTIPLE ELEMENTS ---------------------

element = driver.find_elements(By.ID, "passwd-id")
element = driver.find_elements(By.NAME, "passwd")
element = driver.find_elements(By.XPATH, "//input[@id='passwd-id']")
element = driver.find_elements(By.CSS_SELECTOR, "input#passwd-id")

### --------------------- INTERACTING WITH ELEMENT ---------------------

#sending text
element.send_keys("some text")
#sending text and pressing arrow_down key
element.send_keys(" and some", Keys.ARROW_DOWN)
#clear the element input field 
element.clear()

### --------------------- MOVING IN THE BROWSER ---------------------

driver.forward()
driver.back()

### --------------------- COOKIES ---------------------

# Go to the correct domain
driver.get("http://www.example.com")

# Now set the cookie. This one's valid for the entire domain
cookie = {'name' : 'foo', 'value' : 'bar'}
driver.add_cookie(cookie)

# And now output all the available cookies for the current URL
driver.get_cookies()

### --------------------- HYPERLINKS IN TEXT ---------------------

'''
#Example code:
<html>
 <body>
  <p>Are you sure you want to do this?</p>
  <a href="continue.html">Continue</a>
  <a href="cancel.html">Cancel</a>
</body>
</html>
'''

continue_link = driver.find_element(By.LINK_TEXT, 'Continue')
continue_link = driver.find_element(By.PARTIAL_LINK_TEXT, 'Conti')

######--------------------- WAITS ---------------------

#https://selenium-python.readthedocs.io/waits.html


######--------------------- PAGE OBJECTS ---------------------

#https://selenium-python.readthedocs.io/page-objects.html

######--------------------- CLOSING DRIVER ---------------------
driver.close



######--------------------- FAQ AND SOLUTIONS---------------------

####https://selenium-python.readthedocs.io/faq.html####