from selenium import webdriver
from uspass import USERNAME, PASSWORD
import time

users = [""]

browser = webdriver.Chrome(executable_path='C:/Users/Aswin Asok/chromedriver/chromedriver.exe')

browser.get("http://www.instagram.com/")
time.sleep(2)

username_field = browser.find_element_by_name('username')
username_field.send_keys(USERNAME)
time.sleep(3)

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
    lists[1].click()

    time.sleep(15)
    
    followerscountlist = browser.find_elements_by_class_name('wo9IH')

    followersnamelist = browser.find_elements_by_class_name('Jv7Aj.MqpiF')
    
    outF = open("followers.txt", "w")
    i=0
    while i<len(followersnamelist):
         if i != "Verified":
          outF.write(str(followersnamelist[i].text))
          outF.write("\n")
          i=i+1
    outF.close()

    i=0
    while i<len(followersnamelist):
          followersnamelist[i] = str(followersnamelist[i].text)
          i=i+1

    
browser.close()


browser = webdriver.Chrome(executable_path='C:/Users/Aswin Asok/chromedriver/chromedriver.exe')

browser.get("http://www.instagram.com/")
time.sleep(2)

username_field = browser.find_element_by_name('username')
username_field.send_keys(USERNAME)

password_field = browser.find_element_by_name('password')
password_field.send_keys(PASSWORD)

login_btn = browser.find_element_by_css_selector('button[type="submit"]')
login_btn.click()

time.sleep(20)

for user in users:
    browser.get(f"https://www.instagram.com/{user}/")

    posts, followers, following = browser.find_elements_by_class_name('g47SY')
    print(posts.text, followers.text, following.text)
    
    lists = browser.find_elements_by_class_name('LH36I')
    lists[2].click()

    time.sleep(20)

    followingcountlist = browser.find_elements_by_class_name('wo9IH')

    followingnamelist = browser.find_elements_by_class_name('Jv7Aj.MqpiF')
    
    print(len(followingnamelist))
    
    outF = open("following.txt", "w")
    i=0
    while i<len(followingnamelist):
         if i != "Verified":
          outF.write(str(followingnamelist[i].text))
          outF.write("\n")
          i=i+1
    outF.close()

    i=0
    while i<len(followingnamelist):
          followingnamelist[i] = str(followingnamelist[i].text)
          i=i+1

def nonFollowers(followers, followings):
     outF = open("nonFollowers.txt", "w")

     for i in followings :
         if i not in followers:
              if i != "Verified":
                    outF.write("@"+i)
                    outF.write("\n")
     
     return nonFollowers

nonFollowers(followersnamelist, followingnamelist)

    


    






