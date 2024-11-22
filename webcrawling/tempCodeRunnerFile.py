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

for book in book_list:
    cursor.execute('INSERT INTO books VALUES(?,?,?,?)', book.to_list())

conn.commit()
conn.close()
print('success')