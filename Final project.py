import requests
from selenium import webdriver
from time import sleep
import os
from bs4 import BeautifulSoup
import shutil
import sys

username = sys.argv[1]
password = sys.argv[2]
username_to_scrap_pics_from = sys.argv[3]

driver = webdriver.Chrome('D:\PYTHON LEARNING LECTURES CODES\SECOND LECTURE CODES\chromedriver.exe')
driver.maximize_window()
driver.get('https://www.instagram.com/')
# driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(5)

search = driver.find_element_by_xpath("//div[@id='react-root']//p[@class='izU2O']/a")
search = driver.find_element_by_link_text('Log in')
search.click()
current = driver.current_url
driver.get(current)
sleep(7)
user_name = driver.find_element_by_xpath("//div[@id='react-root']//input[@name='username']")
user_name.send_keys(username)
password = driver.find_element_by_xpath("//div[@id='react-root']//input[@name='password']")
password.send_keys(password)
sleep(2)
# driver.find_element_by_xpath("//button[contains(.,'Log In')]").click()
password.submit()  # submit function basically submits a form so it will automatically click the login button.
sleep(10)
close_window = driver.find_element_by_xpath("//button[@class='aOOlW  bIiDR  ']")
close_window.click()
sleep(3)
search_name = driver.find_element_by_xpath("//input[@class='XTCLo x3qfX ']")
search_name.send_keys(username_to_scrap_pics_from)
sleep(2)
user_url = 'https://www.instagram.com/'+username_to_scrap_pics_from+'/'
driver.get(user_url)
sleep(2)
get_posts = driver.find_element_by_xpath("//span[@class='g47SY ']").text
get_posts = str(get_posts).replace(',', '')  # if posts are 15,483 ---> then result will be 15483
get_posts = int(get_posts)
print(get_posts)
if get_posts > 12:
    scrolls = int(get_posts / 12) + 3
    for value in range(3):
        print(value)
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        sleep(2)
# to open images add this at the end it will take you to the whole picture 'media/?size=m'
sleep(5)
if os.path.isdir("D:\instaphotos"):
    pass
else:
    os.mkdir("D:\instaphotos")
soup = BeautifulSoup(driver.page_source, 'html.parser')
images = soup.find_all('img')
for index, img in enumerate(images):
    filename = 'image_' + str(index) +".png"
    path = os.path.join("D:\instaphotos", filename)
    link = img['src']
    req = requests.get(link, stream=True)
    with open(path,'wb') as file:
        shutil.copyfileobj(req.raw,file)
    #print(img['src'])
driver.close()
