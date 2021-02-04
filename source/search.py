from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd
import re


def search_in_excel(scholars):
    validArticles = []
    excel_file = './excel/JCR-2019.xlsx'
    articles = pd.read_excel(excel_file, sheet_name="JCR-All Journals", skiprows=2, usecols="B")
    for scholar in scholars:
        index = 0
        if scholar['journal'] == '':
            continue
        for article in articles['Full Journal Title'].str.lower():
            index += 1
            if scholar['journal'] == article:
                scholar["index in excel"] = str(index + 3)
                validArticles.append(scholar)
                break
    return validArticles


def find_year(information):
    year = re.search('\d\d\d\d', information).group(0)
    return year


def find_author(information):
    author = information.split(' - ')
    return author[0]


def find_citation(information):
    cited = re.search('(\d)+', information).group(0)
    return cited


def find_journal(information):
    journal = information.split(' - ')[1]
    journal = journal.split(',')[0]
    journal = journal.lower().strip('.')
    return journal


def search_in_google_scholar(search_keyword):
    main_years, main_citations, main_titles, main_summaries, main_authors, main_urls, main_journal = [], [], [], [], [], [], []
    options = Options()
    options.add_argument('--headless')
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(executable_path="./chrome/chromedriver", chrome_options=options)
    driver.get('https://scholar.google.com')
    time.sleep(5)

    inputElems = driver.find_elements_by_css_selector('input[name=q]')
    for inputElem in inputElems:
        inputElem.send_keys(search_keyword)
        inputElem.send_keys(Keys.ENTER)
    time.sleep(5)

    titles = driver.find_elements_by_css_selector('h3.gs_rt a')
    informations = driver.find_elements_by_css_selector('div.gs_a')
    cites = driver.find_elements_by_css_selector('div.gs_fl a:nth-of-type(3)')
    summaries = driver.find_elements_by_css_selector('div.gs_rs')
    elems = driver.find_elements_by_css_selector('.gs_rt [href]')
    urls = [elem.get_attribute('href') for elem in elems]
    articles_len = len(titles)

    for i in range(articles_len):
        main_titles.append(titles[i].text)
        main_summaries.append(summaries[i].text)
        main_citations.append(find_citation(cites[i].text))
        main_years.append(find_year(informations[i].text))
        main_authors.append(find_author(informations[i].text))
        main_journal.append(find_journal(informations[i].text))
        main_urls.append(urls[i])

    driver.close()
    return main_titles, main_authors, main_years, main_citations, main_summaries, main_urls, main_journal, articles_len
