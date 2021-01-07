from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

def search_in_excel(keyword):
    excel_file = './excel/test.xlsx'
    articles = pd.read_excel(excel_file)
    found_article = articles['Full Journal Title'].where(articles['JCR Abbreviated Title'] == keyword).dropna()
    return found_article

def search_in_google_scholar(search_keyword):
    driver = webdriver.Chrome(executable_path="./chrome/chromedriver")
    driver.get('https://scholar.google.com')
    inputElems = driver.find_elements_by_css_selector('input[name=q]')
    for inputElem in inputElems:
        inputElem.send_keys(search_keyword)
        inputElem.send_keys(Keys.ENTER)
    articles = get_articles(driver=driver)
    print(articles)
    time.sleep(5)
    driver.close()

def get_articles(driver):
    items = driver.find_elements_by_class_name('gs_rt')
    hrefs = []
    for item in items:
        hrefs.append(item.find_element_by_tag_name('a').get_attribute('href'))
    return hrefs