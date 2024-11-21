import requests
print('haha')

url = 'https://jsonplaceholder.typicode.com/posts'
r = requests.get(url)

#r. status_code 
print (r.json())