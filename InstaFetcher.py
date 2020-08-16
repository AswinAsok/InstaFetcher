from selenium import webdriver
from uspass import USERNAME, PASSWORD
import time

users = [input("Username of The Profile To Fetch : ")]

browser = webdriver.Chrome(executable_path='C:/Users/Aswin Asok/chromedriver/chromedriver.exe')

browser.get("http://www.instagram.com/")
time.sleep(2)

username_field = browser.find_element_by_name('username')
username_field.send_keys(USERNAME)

password_field = browser.find_element_by_name('password')
password_field.send_keys(PASSWORD)

login_btn = browser.find_element_by_css_selector('button[type="submit"]')
login_btn.click()

time.sleep(6)

for user in users:

    print("\n---------Fetching The Followers List---------")
    browser.get(f"https://www.instagram.com/{user}/")

    posts, followers, following = browser.find_elements_by_class_name('g47SY')
    print(f"\nTotal Posts: {posts.text}\nTotal Followers: {followers.text}\nTotal Followings: {following.text}\n")
    
    lists = browser.find_elements_by_class_name('LH36I')
    lists[1].click()


    print("Sleep Started\n")
    print("**Please Scroll Down The Entire List.\n")
    t1  = int(input("Enter the Time Required for Scrolling(in Seconds) : "))
    time.sleep(t1)
    print("Sleep Over")
    
    followerscountlist = browser.find_elements_by_class_name('wo9IH')

    followersnamelist = browser.find_elements_by_class_name('Jv7Aj.MqpiF')
    
    print("\nTotal Number of Followers Aquired : ",len(followersnamelist))

    if len(followersnamelist)<int(followers.text):
          print("\nComplete list of follwers has not been retrieved please increase the sleep duration")
          print("Proceeding with Accuracy : ",(len(followersnamelist)/int(followers.text))*100.0)
    else:
          print("\nComplete List of Follwers has been Retrived\n")


    outF = open("followers.txt", "w")
    print("\nWriting the Usernames of Follwers to a Text File\n")
    
    i=0
    while i<len(followersnamelist):
         if i != "Verified":
          outF.write("@"+str(followersnamelist[i].text))
          outF.write("\n")
          i=i+1
    outF.close()
    print("Writing Completed\n")

    i=0
    while i<len(followersnamelist):
          followersnamelist[i] = str(followersnamelist[i].text)
          i=i+1

print("\n------------Fetching the Followings List---------------")

for user in users:
    browser.get(f"https://www.instagram.com/{user}/")

    posts, followers, following = browser.find_elements_by_class_name('g47SY')
    
    lists = browser.find_elements_by_class_name('LH36I')
    lists[2].click()
    
    print("\nSleep Started\n")
    print("**Please Scroll Down The Entire List.\n")
    t2 = int(input("Enter the Time Required for Scrolling(in Seconds) : "))
    time.sleep(t2)
    print("Sleep Over\n")

    followingcountlist = browser.find_elements_by_class_name('wo9IH')

    followingnamelist = browser.find_elements_by_class_name('Jv7Aj.MqpiF')
    
    print("Total Number of Followings Aquired : ",len(followingnamelist))

    if len(followingnamelist)<int(following.text):
          print("\nComplete list of follwings has not been retrieved please increase the sleep duration")
          print("Proceeding with Accuracy : ",(len(followingnamelist)/int(following.text))*100.0)

    else:
          print("\nComplete List of Follwings has been Retrived\n")
    
    
    outF = open("following.txt", "w")
    print("\nWriting the Usernames of Follwings to a Text File\n")
    i=0
    while i<len(followingnamelist):
         if i != "Verified":
          outF.write("@"+str(followingnamelist[i].text))
          outF.write("\n")
          i=i+1
    outF.close()
    print("Writing Completed\n")

    i=0
    while i<len(followingnamelist):
          followingnamelist[i] = str(followingnamelist[i].text)
          i=i+1

print("-----------Finding Non-Followers------------\n")

def nonFollowers(followers, followings):
     outF = open("nonFollowers.txt", "w")
     print("Writing the list of non-followers to a Text File")
     count = 0
     for i in followings :
         if i not in followers:
              if i != "Verified":
                    count+=1
                    outF.write("@"+i)
                    outF.write("\n")
     print("\nNumber of Non-Followers : ",count)
     print("\nWriting Completed")
     return nonFollowers

nonFollowers(followersnamelist, followingnamelist)

browser.close()

    


    






