from bs4 import BeautifulSoup as bs
import requests
url = "https://estivalet.github.io/static-testing-sites/simple/ids_classes.html"
response = requests.get(url)
soup = bs(response.content, 'html.parser')

print(soup.find_all(id='first')[0].get_text().strip())


    