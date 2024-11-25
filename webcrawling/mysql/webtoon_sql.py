import pymysql
import pandas as pd

db_config = {
    'host': 'localhost',        
    'user': 'root',             
    'password': '1234',         
    'port': 3306,
    'database': 'webtoon_db'               
}

csv_file = './webtoons.csv'
data = pd.read_csv(csv_file)

connection = pymysql.connect(
    host=db_config['host'],
    user=db_config['user'],
    password=db_config['password'],
    port=db_config['port'],
    database=db_config['database']
)

cursor = connection.cursor()

for index, row in data.iterrows():
    title = row['title']
    author = row['author']
    rating = row['rating']
    
    # SQL 쿼리 작성
    insert_query = """
    INSERT INTO webtoons (title, author, rating)
    VALUES (%s, %s, %s)
    """
    
    # 데이터 삽입
    cursor.execute(insert_query, (title, author, rating))
    
    
# 커밋 (변경사항 저장)
connection.commit()

# 연결 종료
cursor.close()
connection.close()

print("Data inserted successfully")