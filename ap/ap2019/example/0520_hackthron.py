import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import config

open_data = requests.get(config.open_data_url)
print(open_data)
soup = BeautifulSoup(open_data.text, features="html.parser")
print(soup)
# exit()
new_time = str(soup.find_all('sent'))

try:
    file = open("output.txt", 'r')
except FileNotFoundError:
    old_time = "no file"
else:
    file.close()
    with open('output.txt', 'r') as f:
        old_time = f.read()

if old_time == new_time:
    print("Typhoon data didn't update.")
    # exit()
else:
    print("Typhoon data updated, start screenshot.")
    with open('output.txt', 'w+') as f:
        f.truncate(0)
        f.write(new_time)

# start opening server
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument("--headless")
chrome = webdriver.Chrome('C:/chromedriver_win32/chromedriver.exe', chrome_options=chrome_options)
chrome.get(config.goal_url)

time.sleep(8)
chrome.set_window_size(1296, 729)
time.sleep(2)
print("Done opening")

# get check box xpath

# chrome.find_element('xpath', '//*[@id="mainmap"]/div[2]/div[2]/div/form/div[3]/label[2]/div/input')
main_map = chrome.find_element('xpath', '//*[@id="mainmap"]')
left_list = chrome.find_element('xpath', '//*[@id="mainmap"]/div[2]/div[1]/div[1]/a[2]')
right_list = chrome.find_element('xpath', '//*[@id="mainmap"]/div[2]/div[2]/div')
sea_range = chrome.find_element('xpath', '//*[@id="mainmap"]/div[2]/div[2]/div/form/div[3]/label[2]/div/input')
time_tag = chrome.find_element('xpath', '//*[@id="mainmap"]/div[2]/div[2]/div/form/div[3]/label[5]/div/input')
left_bar = chrome.find_element('xpath', "/html/body/div/header/nav/a")
# window adjustment
action = ActionChains(chrome)
for i in range(0, 4):
    left_list.click()
    time.sleep(1)
    main_map.send_keys(Keys.UP)
    time.sleep(1)

main_map.send_keys(Keys.DOWN)
time.sleep(1)
main_map.send_keys(Keys.DOWN)
time.sleep(1)
main_map.send_keys(Keys.RIGHT)
time.sleep(1)
main_map.send_keys(Keys.RIGHT)
time.sleep(1)
left_bar.click()
print("Done window adjustment")

now_time = str(time.strftime('%Y-%m-%d_%H', time.localtime()))
filename = [now_time+"_nTag_nLine.png", now_time+"_ntag_wLine.png",
            now_time+"_wtag_wLine.png", now_time+"_wtag_nLine.png"]

# First screenshot, no time tag / no sea line
action.move_to_element(right_list).perform()
time.sleep(1)
time_tag.click()
action.move_to_element(left_list).perform()
for i in range(0, 6):
    main_map.send_keys(Keys.PAGE_DOWN)
chrome.save_screenshot(filename[0])
for i in range(0, 6):
    main_map.send_keys(Keys.PAGE_UP)
time.sleep(3)
print("Done screenshot : " + filename[0])

# Second screenshot, no time tag / with sea line
action.move_to_element(right_list).perform()
time.sleep(1)
sea_range.click()
action.move_to_element(left_list).perform()
for i in range(0, 6):
    main_map.send_keys(Keys.PAGE_DOWN)
chrome.save_screenshot(filename[1])
for i in range(0, 6):
    main_map.send_keys(Keys.PAGE_UP)
time.sleep(3)
print("Done screenshot : " + filename[1])

# Third screenshot, with time tag / with sea line
action.move_to_element(right_list).perform()
time.sleep(1)
time_tag.click()
action.move_to_element(left_list).perform()
for i in range(0, 6):
    main_map.send_keys(Keys.PAGE_DOWN)
chrome.save_screenshot(filename[2])
for i in range(0, 6):
    main_map.send_keys(Keys.PAGE_UP)
time.sleep(3)
print("Done screenshot : " + filename[2])

#  Forth screenshot, with time tag / no sea line
action.move_to_element(right_list).perform()
time.sleep(1)
sea_range.click()
action.move_to_element(left_list).perform()
for i in range(0, 6):
    main_map.send_keys(Keys.PAGE_DOWN)
chrome.save_screenshot(filename[3])
for i in range(0, 6):
    main_map.send_keys(Keys.PAGE_UP)
time.sleep(1)
print("Done screenshot : " + filename[3])
