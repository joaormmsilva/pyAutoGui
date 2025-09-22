from bs4 import BeautifulSoup as bs
import requests
url = "https://affiliate.shopee.com.br/offer/shopee_offer/100001?type=2&trace=eyJ0cmFjZV9pZCI6IjAuSXFQaHFBZlpRWS42MDAiLCJsaXN0X3R5cGUiOjYwMCwicm9vdF90cmFjZV9pZCI6IjAuSXFQaHFBZlpRWS42MDAiLCJyb290X2xpc3RfdHlwZSI6NjAwfQ%3D%3D"
response = requests.get(url)
html = response.content
soup = bs(html, 'lxml')


all_names = soup.find_all(class_="ItemCard__name")
print(all_names)

for h3 in all_names:
    print(h3.get_text(strip=True))
    print(h3)
    