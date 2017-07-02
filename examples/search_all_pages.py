from goodreads import client
from goodreads import apikey
import json

def writeToJSONFile(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)

#authetification
gc = client.GoodreadsClient(apikey.key, apikey.secret)

#get all books by query
books = gc.search_books_all_pages(q='Gerri Hill', search_field='author')

#to json
data = []
for book in books:
    i = {}
    i['isbn'] = book.isbn
    i['isbn13'] = book.isbn13
    i['title'] = book.title
    i['author'] = book.authors[0].name
    i['link'] = book.link
    i['popular_shelves'] = [shelve.name for shelve in book.popular_shelves]
    data.append(i)
    
writeToJSONFile('','search_all_pages',data)
