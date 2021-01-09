from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase

def bibTex(articles):
    # article = standard_entry(articles)
    db = BibDatabase()
    db.entries = standard_entry(articles)
    writer = BibTexWriter()
    with open('bibtex.bib', 'w') as bibfile:
        bibfile.write(writer.write(db))

def standard_entry(inputs):
    new_inputs = []
    for input in inputs:
        input["ID"] = input["year"]
        input["ENTRYTYPE"] = 'article'
        new_inputs.append(input)
    
    return new_inputs
