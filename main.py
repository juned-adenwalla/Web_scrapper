import requests
from bs4 import BeautifulSoup

url = input('which website you want to scrap : ')

r = requests.get(url)
htmlContent = r.content

soup = BeautifulSoup(htmlContent, 'html.parser')

title = soup.title
para = soup.find_all('p')

anchor = soup.find_all('a')

print(soup.get_text())