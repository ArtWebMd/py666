import requests
import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
ON_HEROKU = os.environ.get('ON_HEROKU')

if ON_HEROKU:
    # get the heroku port
    port = int(os.environ.get('PORT', 17995))  # as per OP comments default is 17995
else:
    port = 3000
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options = chrome_options)



def verify_competitors():
    page = requests.get("https://999.md/ru/list/all-for-celebrations/gifts-for-fans-of-smoking")
    soup = BeautifulSoup(page.content, 'html.parser')
    a_tags = soup.select('div.ads-list-photo-item-title > a')

    # setam masivul pentru nikname-uri
    user_names_array = []

    # aici gasim link-urile
    for link in a_tags[3:]:
        full_link = "https://999.md" + link.get('href')
        user_ad = requests.get(full_link)
        parse_page = BeautifulSoup(user_ad.content, 'html.parser')
        user_names = parse_page.select('a.adPage__aside__stats__owner__login')
        for i in range(len(user_names)):
            print(user_names[i].contents[0].strip())
            if(user_names[0].contents[0].strip() == 'rentcalianmd'):
                print('RentCalian Nambar oan!!! Incepem de la inceput curand!')
                time.sleep(10)
                verify_competitors()
            else:
                if(user_names[i].contents[0].strip() == 'vinzarionline' or user_names[i].contents[0].strip() == 'aaandreiii' or user_names[i].contents[0].strip() == 'pislaru-888' or user_names[i].contents[0].strip() == 'rentinthecapital' or user_names[i].contents[0].strip() == 'smoke-lab-md'):
                    if(user_names[i-1].contents[0] == 'rentcalianmd'):
                        print('RentCalian Nambar oan, verificam din nou')
                        time.sleep(10)
                        verify_competitors()
                    else:
                        print('Ucidem concurentii start!')
                        kill_competitors()
            # user_names_array.append(u_name.contents[0].strip())
            # print(u_name.contents[0].strip())
        # print(user_names)
    # print(divs)
    

    
def kill_competitors():
    driver = webdriver.Chrome()
    driver.get("https://simpalsid.com/user/login?project_id=999a46c6-e6a6-11e1-a45f-28376188709b&lang=ru")
    time.sleep(2)
    # gasim campurile login,password
    username = driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[2]/input")
    password = driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[3]/input")
    login_button = driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[4]/button")

    #logam
    username.send_keys("rentcalianmd")
    password.send_keys("dumitru1221")
    time.sleep(2)
    login_button.click()

    driver.get("https://999.md/cabinet/items/rentcalianmd?page=15&ad_states=public")

    republish = driver.find_element_by_xpath('/html/body/div[4]/div/section/div/div/div[1]/form/table/tbody/tr[28]/td[7]/div/a')
    republish.click()

    time.sleep(2)

    republish_button = driver.find_element_by_xpath('//*[@id="js-product-payment"]/button')
    republish_button.click()




    # print(all_links)
    now = datetime.datetime.now()
    f = open("hours.txt", "a")
    f.write(str(now.day) + '-' + str(now.hour) + ':' + str(now.minute))
    f.close()
    time.sleep(3)
    driver.close()
    verify_competitors()

verify_competitors()
