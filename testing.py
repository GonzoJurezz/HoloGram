import requests
from bs4 import BeautifulSoup

res = requests.get(
    f"https://www.mein-horoskop-jeden-tag.com/horoskop/heute/stier.htm")

soup = BeautifulSoup(res.content, 'lxml')
course_cards = soup.find('div', class_='txt')
print(course_cards.p.text)
