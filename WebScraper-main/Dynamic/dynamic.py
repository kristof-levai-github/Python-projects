import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd 

#exercise: filter yt top videos filtered by youtuber

url = 'https://www.youtube.com/results?search_query=john+watson+rooney&sp=CAM%253D'

#response = requests.get(url)
#r = response.text

### --------------------- NAVIGATING ---------------------

###getting the driver path
driver = webdriver.Chrome(executable_path="C:\\Users\\ADMIN\\Desktop\\python\\web\\chromedriver")

###getting the url and the source page
driver.get(url)

#kell egy olyan element, ami mindegyikre igaz 


#div class="style-scope ytd-video-renderer"

#title : //*[@id="video-title"]
#view: /html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/ytd-video-meta-block/div[1]/div[2]/span[1]
#date : /html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/ytd-video-meta-block/div[1]/div[2]/span[2]

videos = driver.find_elements(By.CLASS_NAME, "style-scope ytd-video-renderer")

video_list = []

for video in videos:
    title = video.find_element(By.XPATH, './/*[@id="video-title"]').text
    views = video.find_element(By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/ytd-video-meta-block/div[1]/div[2]/span[1]').text
    when = video.find_element(By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/ytd-video-meta-block/div[1]/div[2]/span[2]').text
    vid_item = {
        'title': title,
        'views': views,
        'when': when
    }
    video_list.append(vid_item)

df = pd.DataFrame(video_list)
print(df)