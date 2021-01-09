from bibTexOutput import bibTex
from search import search_in_excel, search_in_google_scholar

def get_search_keyword():
    key = input('Enter Your Keyword: ')
    return key

if __name__ == '__main__':
    main_years, main_citations, main_titles, main_summaries, main_authors, scholars = [], [], [], [], [], []
    articles_len = 0
    keyword = get_search_keyword()
    found_article = search_in_excel(keyword)
    print(found_article.iloc[0])
    main_titles, main_authors, main_years, main_citations, main_summaries, articles_len = search_in_google_scholar(found_article.iloc[0])
    
    for i in range(articles_len):
        scholars.append({
            "title": main_titles[i],
            "author": main_authors[i],
            "year": main_years[i],
            "citation": main_citations[i],
            "summary": main_summaries[i]
        })

    bibTex(scholars)
    for scholar in scholars:
        print(f"title: {scholar['title']}\nauthor: {scholar['author']}\nyear: {scholar['year']}\ncitation: {scholar['citation']}\nsummary: {scholar['summary']}\n************************")
