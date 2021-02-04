from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase

def bibTex(articles):
    db = BibDatabase()
    db.entries = standard_entry(articles)
    writer = BibTexWriter()
    with open('./output/bibtex.bib', 'w') as bibfile:
        bibfile.write(writer.write(db))

def standard_entry(inputs):
    i = 1
    for input in inputs:
        input["ID"] = str(i)
        input["ENTRYTYPE"] = 'article'
        input.pop("journal")
        input.pop("index in excel")
        i += 1
    
    return inputs
