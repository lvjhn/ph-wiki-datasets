import core.helpers as helpers

helpers.DEBUG = True

from core.main_articles.na import NationalArticle

ma = NationalArticle(
    "Philippines", 
    folder="./misc/data/main-articles/national/"
) 

fields = ma.extract_all()

for field in fields:
    print(f"{field} = {fields[field]}")
    print()

