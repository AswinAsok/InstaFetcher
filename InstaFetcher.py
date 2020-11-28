from selenium import webdriver
from dotenv import load_dotenv
import time
import os
import xlwt 
from xlwt import Workbook 

load_dotenv()

USERNAME = os.getenv("InstaUsername")
PASSWORD = os.getenv("InstaPassword")
user = input("Username of The Profile To Fetch : ")

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


print("\n---------Fetching The Followers List---------")
browser.get(f"https://www.instagram.com/{user}/")

posts, followers, following = browser.find_elements_by_class_name('g47SY')
print(f"\nTotal Posts: {posts.text}\nTotal Followers: {followers.text}\nTotal Followings: {following.text}\n")

lists = browser.find_elements_by_class_name('LH36I')
lists[1].click()


time.sleep(3)
scr1 = browser.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')

while not ((len((browser.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/ul/div")).find_elements_by_tag_name("li"))) == int(followers.text)):
      browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)
      time.sleep(2)
      

followerscountlist = browser.find_elements_by_class_name('wo9IH')

followersnamelist = browser.find_elements_by_class_name('Jv7Aj.MqpiF')

print("\nTotal Number of Followers Aquired : ",len(followersnamelist))

if len(followersnamelist)<int(followers.text):
      print("\nComplete list of follwers has not been retrieved please increase the sleep duration")
      print("Proceeding with Accuracy : ",(len(followersnamelist)/int(followers.text))*100.0)
else:
      print("\nComplete List of Follwers has been Retrived\n")



wb = Workbook() 
sheet1 = wb.add_sheet('Sheet 1') 
sheet1.write(0, 0, "List of Followers("+followers.text+")")
row = 2

print("Writing the list of Followers to a Excel File")

for i in range(len(followersnamelist)):
      sheet1.write(row, 0, "@"+str(followersnamelist[i].text)) 
      row = row+1
      
print("\nWriting Completed\n")

i=0
while i<len(followersnamelist):
      followersnamelist[i] = str(followersnamelist[i].text)
      i=i+1



print("\n------------Fetching the Followings List---------------\n")


browser.get(f"https://www.instagram.com/{user}/")

posts, followers, following = browser.find_elements_by_class_name('g47SY')

lists = browser.find_elements_by_class_name('LH36I')
lists[2].click()

time.sleep(3)
scr1 = browser.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')

while not ((len((browser.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/ul/div")).find_elements_by_tag_name("li"))) >= int(following.text)):
      browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)
      time.sleep(1.5)
      


followingcountlist = browser.find_elements_by_class_name('wo9IH')

followingnamelist = browser.find_elements_by_class_name('Jv7Aj.MqpiF')

print("Total Number of Followings Aquired : ",len(followingnamelist))

if len(followingnamelist)<int(following.text):
      print("\nComplete list of follwings has not been retrieved please increase the sleep duration")
      print("Proceeding with Accuracy : ",(len(followingnamelist)/int(following.text))*100.0)

else:
      print("\nComplete List of Follwings has been Retrived\n")


sheet1.write(0, 1, "List of Followings("+following.text+")")
row = 2

print("Writing the list of Followings to a Excel File")

for i in range(len(followingnamelist)):
      sheet1.write(row, 1, "@"+str(followingnamelist[i].text))  
      row = row+1
      
print("\nWriting Completed\n")

i=0
while i<len(followingnamelist):
      followingnamelist[i] = str(followingnamelist[i].text)
      i=i+1



print("-----------Finding Non-Followers------------\n")

def nonFollowers(followers, followings):
      
      print("Writing the list of non-followers to a Excel File")
      
      row = 2
      count = 0
      for i in followings :
            if i not in followers:
                  if i != "Verified":
                        count+=1
                        sheet1.write(row, 2, "@"+str(i))  
                        row = row+1
      
      print("Writing Completed")
      sheet1.write(0, 2, "List of Non-Followers("+str(count)+")")
      wb.save('Details.xls') 
      print("\nNumber of Non-Followers : ",count)
      print("\nWriting Completed")
      return nonFollowers



nonFollowers(followersnamelist, followingnamelist)

browser.close()
