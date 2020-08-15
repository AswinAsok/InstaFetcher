from selenium import webdriver
from config import USERNAME, PASSWORD
from selenium.webdriver.common.keys import Keys
import time

users = ["_aswin_asok_"]

browser = webdriver.Chrome(executable_path='C:/Users/Aswin Asok/chromedriver/chromedriver.exe')

browser.get("http://www.instagram.com/")
time.sleep(2)

username_field = browser.find_element_by_name('username')
username_field.send_keys(USERNAME)

password_field = browser.find_element_by_name('password')
password_field.send_keys(PASSWORD)

login_btn = browser.find_element_by_css_selector('button[type="submit"]')
login_btn.click()

time.sleep(10)

for user in users:
    browser.get(f"https://www.instagram.com/{user}/")

    posts, followers, following = browser.find_elements_by_class_name('g47SY')
    print(posts.text, followers.text, following.text)
    
    lists = browser.find_elements_by_class_name('LH36I')
    lists[2].click()

    time.sleep(15)

    followingcountlist = browser.find_elements_by_class_name('wo9IH')

    followingnamelist = browser.find_elements_by_class_name('d7ByH') 
    
    outF = open("following.txt", "w")
    i=0
    while i<len(followingnamelist):
         outF.write(str(followingnamelist[i].text))
         outF.write("\n")
         i=i+1
    outF.close()

   


    






