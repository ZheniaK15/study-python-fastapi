import requests

response = requests.get('https://jsonplaceholder.typicode.com/')
print(response.text)



import requests

params = {'key1': 'value1', 'key2': 'value2'}
response = requests.get('https://jsonplaceholder.typicode.com/', params=params)
print(response.text)




import requests

data = {'username': 'user', 'password': 'pass'}
response = requests.post('https://jsonplaceholder.typicode.com/login', data=data)
print(response.status_code)





import requests

response = requests.get('https://jsonplaceholder.typicode.com/')
print(response.headers)
print(response.status_code)




import requests

try:
    response = requests.get('https://example.com')
    response.raise_for_status()
    print(response.text)
except requests.exceptions.RequestException as e:
    print('Error:', e)




import requests

response = requests.get('https://example.com')
with open('page_content.html', 'w') as f:
    f.write(response.text)
print('Content saved to file page_content.html')
