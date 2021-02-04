from bibTexOutput import bibTex
from search import search_in_excel, search_in_google_scholar


def get_search_keyword():
    key = input('Enter Your Keyword: ')
    return key


if __name__ == '__main__':
    scholars = []
    keyword = get_search_keyword()
    main_titles, main_authors, main_years, main_citations, main_summaries, main_urls, main_journal, articles_len = search_in_google_scholar(keyword)

    for i in range(articles_len):
        scholars.append({
            "title": main_titles[i],
            "author": main_authors[i],
            "year": main_years[i],
            "journal": main_journal[i],
            "citation": main_citations[i],
            "summary": main_summaries[i],
            "url": main_urls[i]
        })
    validArticle = search_in_excel(scholars)
    for valid in validArticle:
        print(
            f"title: {valid['title']}\nauthor: {valid['author']}\nyear: {valid['year']}\njournal: {valid['journal']}\ncitation: {valid['citation']}\nindex in excel: {valid['index in excel']}\nsummary: {valid['summary']}\nurl: {valid['url']}\n************************")
    bibTex(validArticle)