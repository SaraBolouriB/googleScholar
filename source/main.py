from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd

scholar = []

def get_search_keyword():
    key = input('Enter Your Keyword: ')
    return key

def search_in_excel(keyword):
    excel_file = './excel/test.xlsx'
    articles = pd.read_excel(excel_file)
    found_article = articles['Full Journal Title'].where(articles['JCR Abbreviated Title'] == keyword).dropna()
    return found_article

def search_in_google_scholar(search_keyword):
    driver = webdriver.Chrome(executable_path="./chrome/chromedriver.exe")
    driver.get('https://scholar.google.com')
    inputElems = driver.find_elements_by_css_selector('input[name=q]')
    for inputElem in inputElems:
        inputElem.send_keys(search_keyword)
        inputElem.send_keys(Keys.ENTER)

    time.sleep(3)
    titles = driver.find_elements_by_css_selector('h3.gs_rt a')
    writers = driver.find_elements_by_css_selector('div.gs_a')
    citations = driver.find_elements_by_css_selector('div.gs_fl a:nth-of-type(3)')
    summaries = driver.find_elements_by_css_selector('div.gs_rs')
    for title in titles:
        print(title.text)
        print('=====================')
    for summary in summaries:
        print(summary.text)
        print('=====================')
    for citation in citations:
        print(citation.text)
    for writer in writers:
        print(writer.text)
        scholar.append({"writer": writer.text})
    driver.close()

if __name__ == '__main__':
    keyword = get_search_keyword()
    found_article = search_in_excel(keyword)
    print(found_article.iloc[0])
    search_in_google_scholar(found_article.iloc[0])