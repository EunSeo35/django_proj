class Book:
    def __init__(self, rank, title, author, price):
        self.rank = rank
        self.title = title
        self.author = author
        self.price = price
    
    def __str__(self):
        return f'{self.rank}위: {self.title} - {self.author} - {self.price}'
    
    def to_dict(self):
        return {'rank':self.rank, 'title':self.title, 'author':self.author, 'price':self.price}
        
    def to_list(self):
        return [self.rank, self.title, self.author, self.price]



import requests
from bs4 import BeautifulSoup
url = 'https://www.yes24.com/Product/Category/BestSeller?categoryNumber=001'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

#yesBestList > li:nth-child(1) > div > div.item_info > div.info_row.info_name
book_list_element = soup.select("#yesBestList div.item_info") # #은 id selector, .은 class selector
len(book_list_element)


book_list = []

for i, item in enumerate(book_list_element):
    book_title = item.select_one('div.info_name > a').text
    book_author = item.select_one('span.info_auth > a').text
    #print(i+1, book_author)
    ##yesBestList > li:nth-child(1) > div > div.item_info > div.info_row.info_price > strong > em
    book_price = item.select_one('.info_price .yes_b').text
    #print(i+1, book_title, book_author, book_price)
    book_list.append(Book(i+1, book_title, book_author, book_price))

#print(book_list)

#sqlite DB저장
import sqlite3

conn = sqlite3.connect('book.db')
cursor = conn.cursor()

#테이블 생성 
cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS books(
        rank INTEGER,
        title TEXT,
        author TEXT,
        price TEXT
    )
    '''
)

#데이터 삽입 
for book in book_list:
    cursor.execute('INSERT INTO books VALUES(?,?,?,?)', book.to_list())

conn.commit()
conn.close()
print('success')