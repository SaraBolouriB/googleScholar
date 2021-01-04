from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

def get_search_keyword():
    key = input('Enter Your Keyword: ')
    return key

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
    items = driver.find_elements_by_class_name('gs_r gs_or gs_scl')
    print(items)
    time.sleep(5)
    driver.close()

if __name__ == '__main__':
    keyword = get_search_keyword()
    found_article = search_in_excel(keyword)
    print(found_article.iloc[0])
    search_in_google_scholar(found_article.iloc[0])