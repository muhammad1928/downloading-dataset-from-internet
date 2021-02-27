from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import random
import time
import csv


websites = [

    'https://coinmarketcap.com/currencies/bitcoin/historical-data/',
    'https://coinmarketcap.com/currencies/polkadot-new/historical-data/',
    'https://coinmarketcap.com/currencies/ethereum/historical-data/',
    'https://coinmarketcap.com/currencies/cardano/historical-data/',
    'https://coinmarketcap.com/currencies/xrp/historical-data/',
    'https://coinmarketcap.com/currencies/uniswap/historical-data/',
    'https://coinmarketcap.com/currencies/stellar/historical-data/',
    'https://coinmarketcap.com/currencies/dogecoin/historical-data/',
    'https://coinmarketcap.com/currencies/tether/historical-data/',
    'https://coinmarketcap.com/currencies/usd-coin/historical-data/',
    'https://coinmarketcap.com/currencies/litecoin/historical-data/',
    'https://coinmarketcap.com/currencies/waves/historical-data/',
    'https://coinmarketcap.com/currencies/uma/historical-data/',
    'https://coinmarketcap.com/currencies/pancakeswap/historical-data/',
    'https://coinmarketcap.com/currencies/bittorrent/historical-data/'

]
# websites = ['https://coinmarketcap.com/currencies/cardano/historical-data/',
#             'https://coinmarketcap.com/currencies/avalanche/historical-data/',
#             'https://coinmarketcap.com/currencies/tron/historical-data/',
#             'https://coinmarketcap.com/currencies/pancakeswap/historical-data/',
#             'https://coinmarketcap.com/currencies/waves/historical-data/',
#             'https://coinmarketcap.com/currencies/uniswap/historical-data/'
#
#             ]

for coin in websites:

    path_driver = "D:/Python projects/testestteest/chromedriver.exe"
    # Specifying incognito mode as you launch your browser[OPTIONAL]
    option = webdriver.ChromeOptions()
    option.add_argument("--incognito")

    # Create new Instance of Chrome in incognito mode
    browser = webdriver.Chrome(executable_path=path_driver, options=option)

    # Go to desired website
    browser.get(coin)

    # basliklar icin liste
    basliklar = []

    # Wait 20 seconds for page to load
    timeout = 20
    five_sec = 5
    try:
        # Wait until the final element [Avatar link] is loaded.
        # Assumption: If Avatar link is loaded, the whole page would be relatively loaded because it is among
        # the last things to be loaded.
        WebDriverWait(browser, timeout).until(EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[3]/div/div/div[2]/table/tbody/tr[4]/td[1]')))
    except TimeoutException:
        print("Timed out waiting for page to load")
        browser.quit()

    time.sleep(5)
    try:
        WebDriverWait(browser, five_sec).until(EC.visibility_of_element_located((By.CLASS_NAME, 'rangeBtn___11ATL'))).click()
    except TimeoutException:
        try:
            WebDriverWait(browser, five_sec).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#__next > div > div.sc-57oli2-0.dEqHl.cmc-body-wrapper > div > div.sc-16r8icm-0.hKZfDX.container > div:nth-child(2) > div > div.hrfjxe-0.kFcBuZ > span > button'))).click()

        except TimeoutException:
            print("Couldnt find Date Range")
            browser.quit()
    # date_range_button = browser.find_element_by_class_name('rangeBtn___11ATL').click()

    # tippy-19 > div > div.tippy-content > div > div > div.pickers___166Od > div:nth-child(1) > div > button.react-datepicker__navigation.react-datepicker__navigation--previous
    time.sleep(5)
    try:
        month_button = WebDriverWait(browser, five_sec).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#tippy-18 > div > div.tippy-content > div > div > div.pickers___166Od > div:nth-child(1) > div > button.react-datepicker__navigation.react-datepicker__navigation--previous')))
        # month_button = browser.find_element_by_css_selector("#tippy-19 > div > div.tippy-content > div > div > div.pickers___166Od > div:nth-child(1) > div > button.react-datepicker__navigation.react-datepicker__navigation--previous")
        for i in range(100):
            month_button.click()
            time.sleep(0.5)

    except TimeoutException:
        try:
            month_button = WebDriverWait(browser, five_sec).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#tippy-19 > div > div.tippy-content > div > div > div.pickers___166Od > div:nth-child(1) > div > button.react-datepicker__navigation.react-datepicker__navigation--previous')))
            for i in range(100):
                month_button.click()
                time.sleep(0.5)
        except TimeoutException:
            try:
                month_button = WebDriverWait(browser, five_sec).until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                                                                        '#tippy-20 > div > div.tippy-content > div > div > div.pickers___166Od > div:nth-child(1) > div > button.react-datepicker__navigation.react-datepicker__navigation--previous')))
                for i in range(100):
                    month_button.click()
                    time.sleep(0.5)
            except TimeoutException:
                print("could find month switch button")

    xpath_date = "#tippy-19 > div > div.tippy-content > div > div > div.pickers___166Od > div:nth-child(1) > div > div.react-datepicker__month-container > div.react-datepicker__month > div:nth-child(2) > div.react-datepicker__day.react-datepicker__day--013.react-datepicker__day--keyboard-selected"

    try:
        WebDriverWait(browser, five_sec).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="tippy-19"]/div/div[1]/div/div/div[1]/div[1]/div/div[2]/div[2]/div[3]/div[2]' ))).click()

    except TimeoutException:
        try:
            WebDriverWait(browser, five_sec).until(EC.visibility_of_element_located((By.XPATH,
                                                                                     '//*[@id="tippy-20"]/div/div[1]/div/div/div[1]/div[1]/div/div[2]/div[2]/div[3]/div[2]'))).click()
        except TimeoutException:
            try:
                WebDriverWait(browser, five_sec).until(EC.visibility_of_element_located((By.XPATH,
                                                                                         '//*[@id="tippy-18"]/div/div[1]/div/div/div[1]/div[1]/div/div[2]/div[2]/div[3]/div[2]'))).click()

            except TimeoutException:
                print("could not pick a date inside month")
    # select_date_button = browser.find_element_by_xpath('//*[@id="tippy-19"]/div/div[1]/div/div/div[1]/div[1]/div/div[2]/div[2]/div[3]/div[2]')

    # Choose return date
    # select_date_button.click()
    time.sleep(3)
    try:
        WebDriverWait(browser, five_sec).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#tippy-18 > div > div.tippy-content > div > div > div.footer___12pdF > button.sc-1ejyco6-0.czBWYA' ))).click()
    except TimeoutException:
        try:
            WebDriverWait(browser, five_sec).until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                                                     '#tippy-20 > div > div.tippy-content > div > div > div.footer___12pdF > button.sc-1ejyco6-0.czBWYA'))).click()
        except TimeoutException:
            try:
                WebDriverWait(browser, five_sec).until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                                                         '#tippy-19 > div > div.tippy-content > div > div > div.footer___12pdF > button.sc-1ejyco6-0.czBWYA'))).click()
            except TimeoutException:
                print("couldnt find Done button")

    # select_done_button = browser.find_element_by_css_selector("#tippy-19 > div > div.tippy-content > div > div > div.footer___12pdF > button.sc-1ejyco6-0.czBWYA")
    # select_done_button.click()

    time.sleep(10)
    # Get all of the titles for the pinned repositories
    # We are not just getting pure titles but we are getting a selenium object
    # with selenium elements of the titles.
    title_text = browser.find_element_by_xpath(
        '//*[@id="__next"]/div/div[2]/div/div[1]/div[2]/div[1]/div[1]/h2/small').text
    time.sleep(10)

    rws = browser.find_elements_by_xpath('//*[@id="__next"]/div/div[2]/div/div[3]/div/div/div[2]/table/tbody/tr')

    # len method is used to get the size of that list
    r = len(rws)
    # to get column count of table
    cols = browser.find_elements_by_xpath('//*[@id="__next"]/div/div[2]/div/div[3]/div/div/div[2]/table/thead/tr/th')
    # len method is used to get the size of that list
    c = len(cols)
    # basliklari teker teker listeye ekle
    for j in range(1, c):
        # getting text from the ith row and jth column
        d = browser.find_element_by_xpath("//tr/th[" + str(j) + "]").text
        basliklar.append(d)

    elem = []
    for i in range(1, r):

        # row data set to 0 each time in list
        row = []

        # iterate over the columns
        for j in range(1, c):
            # getting text from the ith row and jth column
            d = browser.find_element_by_xpath("//tr[" + str(i) + "]/td[" + str(j) + "]").text
            
            row.append(d)
            if row not in elem:
                # finally store and print the list in console
                elem.append(row)

    print(elem)
    # to close the browser
    browser.close()

    with open(f"downloads2/{title_text}_100_month.csv", "w") as f:
        write = csv.writer(f)
        write.writerow(basliklar)
        write.writerows(elem)

    wait_time = random.randint(30, 60)
    time.sleep(wait_time)

#
# from bs4 import BeautifulSoup
# import requests
# import json
#
#
# # bu kod tum web sitelerini topluyor ve wesite links dizisi icerisine aktariyor.
# websitelinks = []
# # simple test for coinmarketcap.com
# link = requests.get('https://coinmarketcap.com/')
# soup = BeautifulSoup(link.content, 'html.parser')

# print(soup.prettify())
#
# data = soup.find('script', id="__NEXT_DATA__", type="application/json")
# # print(data)
# coins = {}
# coin_data = json.loads(data.contents[0])
# # print(coin_data)
# listings = coin_data['props']['initialState']['cryptocurrency']['listingLatest']['data']
# for i in listings:
#     coins[str(i['id'])] = i['slug']
#     # print(coins[i])
#     # websitelinks.append(coins[i])
#
#     for i in coins:
#         page = requests.get(f'https://coinmarketcap.com/currencies/{coins[i]}/historical-data/?start=20200101&end=20210101')
#         # print(coins[i])
#         website = f'https://coinmarketcap.com/currencies/{coins[i]}/historical-data/?start=20200101&end=20210101'
#         if website not in websitelinks:
#             websitelinks.append(website)
#         print(websitelinks)
#         print(i)
#
#
#
