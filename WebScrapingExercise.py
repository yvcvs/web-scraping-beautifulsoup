from bs4 import BeautifulSoup
import requests
import csv

#get request function
def getHTML(fullURL):
    response = requests.get(fullURL)
    return response.text

#for loop idea from Abey
books = []

#look through pages with for loop
for i in range(1,51):
    try:
        html = getHTML(f'http://books.toscrape.com/catalogue/page-{i}.html')
        soup = BeautifulSoup(html,'html.parser')
        table = soup.find_all('li',attrs={'class':"col-xs-6 col-sm-4 col-md-3 col-lg-3"})
        for item in table:
            book = {}
            book['title'] = item.find('h3').find('a').attrs['title']
            book['price'] = item.find('p', attrs={'price_color'}).get_text()[2:]
            book['rating'] = item.find('p', attrs={'class':'star-rating'}).attrs['class'][1]
            books.append(book)
    except:
        continue

with open('ScrapedBooks.csv', 'w', encoding='utf8', newline='') as output:
    f = csv.DictWriter(output, books[0].keys())
    f.writeheader()
    f.writerows(books)