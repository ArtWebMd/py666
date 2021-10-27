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
            print(user_names[i].contents[0])
            if(user_names[0].contents[0].strip() == 'rentcalianmd'):
                time.sleep(10)
                verify_competitors()
                print('Rentcalian e nambar oan')
            else:
                if(user_names[i].contents[0] == 'vinzarionline' or user_names[i].contents[0] == 'aaandreiii' or user_names[i].contents[0] == 'pislaru-888' or user_names[i].contents[0] == 'rentinthecapital' or user_names[i].contents[0] == 'smoke-lab-md'):
                    if(user_names[i-1].contents[0] != 'rentcalianmd'):
                        kill_competitors()
                    else:
                        time.sleep(10)
                else:
                    time.sleep(10)
                    verify_competitors()
                    print('Verificam din nou')
#         for u_name in user_names:
#             user_names_array.append(u_name.contents[0].strip())
#             print(u_name.contents[0].strip())
        # print(user_names)
    # print(divs)
#     if('rentcalianmd' in user_names_array):
#         rentcalian_index = user_names_array.index('rentcalianmd')
#     else:
#         rentcalian_index = 9999

#     if('vinzarionline' in user_names_array):
#         vinzarionline_index = user_names_array.index('vinzarionline')
#     else:
#         vinzarionline_index = 9999

#     if('aaandreiii' in user_names_array):
#         aaandreiii_index = user_names_array.index('aaandreiii')
#     else:
#         aaandreiii_index = 9999

#     if('pislaru-888' in user_names_array):
#         pislaru888_index = user_names_array.index('pislaru-888')
#     else:
#         pislaru888_index = 9999

#     if('rentinthecapital' in user_names_array):
#         rentinthecapital_index = user_names_array.index('rentinthecapital')
#     else:
#         rentinthecapital_index = 9999

#     if('smoke-lab-md' in user_names_array):
#         smoke_lab_md_index = user_names_array.index('smoke-lab-md')
#     else:
#         smoke_lab_md_index = 9999

#     if(rentcalian_index > vinzarionline_index or rentcalian_index > aaandreiii_index or rentcalian_index > pislaru888_index or rentcalian_index > rentinthecapital_index or rentcalian_index > smoke_lab_md_index):
#         # chemam functia republicare
#         print('Republicam acum, procesul de ucidere a concurentilor incepe:')
#         time.sleep(5)
#         kill_competitors()
#     else:
#         # repetam peste 1 minut
#         time.sleep(5)
#         print('Verificam din nou concurentii')
#         verify_competitors()

#     print(str(rentcalian_index) + '\n' + str(vinzarionline_index) + '\n' + str(aaandreiii_index) + '\n' + str(pislaru888_index) + '\n' + str(rentinthecapital_index) + '\n' + str(smoke_lab_md_index))

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

    republish = driver.find_element_by_xpath('//*[@id="js-cabinet-items-list"]/tr[28]/td[7]/div/a')
    republish.click()

    time.sleep(2)

    republish_button = driver.find_element_by_xpath('//*[@id="js-product-payment"]/button')
    republish_button.click()




    # print(all_links)
    now = datetime.datetime.now()
    f = open("hours.txt", "a")
    f.write(str(now.day) + '-' + str(now.hour) + ':' + str(now.minute) + '\n')
    f.close()
    time.sleep(3)
    driver.close()
    verify_competitors()

verify_competitors()
