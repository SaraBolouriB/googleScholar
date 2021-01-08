from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd
import re

years = []
citations = []
scholar = []

def get_search_keyword():
    key = input('Enter Your Keyword: ')
    return key

def search_in_excel(keyword):
    excel_file = './excel/test.xlsx'
    articles = pd.read_excel(excel_file)
    found_article = articles['Full Journal Title'].where(articles['JCR Abbreviated Title'] == keyword).dropna()
    return found_article

def find_year(information):
    year = re.search('\d\d\d\d', information).group(0)
    print(year)

def find_citation(information):
    cited = re.search('(\d)+', information)
    print(cited.group(0))

def search_in_google_scholar(search_keyword):
    driver = webdriver.Chrome(executable_path="./chrome/chromedriver")
    driver.get('https://scholar.google.com')
    time.sleep(5)
    inputElems = driver.find_elements_by_css_selector('input[name=q]')
    for inputElem in inputElems:
        inputElem.send_keys(search_keyword)
        inputElem.send_keys(Keys.ENTER)

    time.sleep(10)
    titles = driver.find_elements_by_css_selector('h3.gs_rt a')
    informations = driver.find_elements_by_css_selector('div.gs_a')
    cites = driver.find_elements_by_css_selector('div.gs_fl a:nth-of-type(3)')
    summaries = driver.find_elements_by_css_selector('div.gs_rs')
    for title in titles:
        print(title.text)
        print('=====================')
    for summary in summaries:
        print(summary.text)
        print('=====================')
    print("Cites:")
    for citation in cites:
        print(citation.text)
        find_citation(citation.text)
    print("Years:")
    for information in informations:
        find_year(information.text)
    driver.close()

if __name__ == '__main__':
    keyword = get_search_keyword()
    found_article = search_in_excel(keyword)
    print(found_article.iloc[0])
    search_in_google_scholar(found_article.iloc[0])