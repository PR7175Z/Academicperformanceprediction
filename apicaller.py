import requests

# url = 'http://127.0.0.1:4444/predict'
url = 'http://127.0.0.1:8000/predict'

data = {'features': [0, 53.7948461, 18.23871036, 3, 51.6587823 ]}
response = requests.post(url, json=data)

print(response.json())