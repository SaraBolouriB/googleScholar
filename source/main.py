from search import search_in_excel, search_in_google_scholar

def get_search_keyword():
    key = input('Enter Your Keyword: ')
    return key

if __name__ == '__main__':
    keyword = get_search_keyword()
    found_article = search_in_excel(keyword)
    print(found_article.iloc[0])
    search_in_google_scholar(found_article.iloc[0])