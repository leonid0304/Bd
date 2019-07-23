import requests
r = requests.get('http://httpbin.org/headers')
p= requests.get('http://localhost/')
print(r.text)
print p.text