from bs4 import BeautifulSoup as bs
import requests
url = "https://estivalet.github.io/static-testing-sites/simple/simple.html"
response = requests.get(url)

print(response.status_code)  #2 sucesso / 4;5 erro

soup = bs(response.content, 'html.parser')

html = list(soup.children)[2]
body = list(html.children)[3]
print(list(body.children))
p = list(body.children)[1]
print(p.get_text())