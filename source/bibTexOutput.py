from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase

def bibTex(articles):
    db = BibDatabase()
    db.entries = standard_entry(articles)
    writer = BibTexWriter()
    with open('./output/bibtex.bib', 'w') as bibfile:
        bibfile.write(writer.write(db))

def standard_entry(inputs):
    for input in inputs:
        input["ID"] = input["year"]
        input["ENTRYTYPE"] = 'article'
    
    return inputs
