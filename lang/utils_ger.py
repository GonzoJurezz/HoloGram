import requests
from bs4 import BeautifulSoup


def get_horoscope_by_day_eng(zodiac_sign: int, day: str):
    if "-" in day:
        day = day.replace("-", "")
        res = requests.get(
            f"https://www.horoscope.com/us/horoscopes/general/horoscope-archive.aspx?sign={zodiac_sign}&laDate={day}")
    else:
        res = requests.get(
            f"https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-{day}.aspx?sign={zodiac_sign}")
    soup = BeautifulSoup(res.content, 'html.parser')
    data = soup.find('div', attrs={'class': 'main-horoscope'})
    return data.p.text


# horoskop: mein-horoskop-jeden-tag.com
def get_horoscope_mhjt(zodiac_sign: str):
    res = requests.get(
        f"https://www.mein-horoskop-jeden-tag.com/horoskop/heute/{zodiac_sign}.htm")

    soup = BeautifulSoup(res.content, 'lxml')
    horoscope_txt = soup.find('div', class_='txt').p.text
    return horoscope_txt


# horoskop: www.astroportal.com
def get_horoscope_ap(zodiac_sign: str):
    res = requests.get(
        f"https://www.astroportal.com/tageshoroskope/{zodiac_sign}/")

    horoscope_txt = BeautifulSoup(res.content, 'lxml').text
    return horoscope_txt


# horoskop: https://natune.net
def get_horoscope_nat(zodiac_sign: str):
    res = requests.get(
        f"https://natune.net/horoskop/tageshoroskop-{zodiac_sign}")

    soup = BeautifulSoup(res.content, 'lxml')
    horoscope_txt = soup.find('div', class_='szcontent').div.div.text
    return horoscope_txt


# horoskop: https://horoskop.de
def get_horoscope_hk(zodiac_sign: str):
    res = requests.get(
        f"https://horoskop.de/dein-horoskop/{zodiac_sign}/tageshoroskop/")

    soup = BeautifulSoup(res.content, 'lxml')
    horoscope_txt = soup.find('p', class_='module-daily-horoscope__copy').text
    return horoscope_txt


# horoskop: https://mein.astrocenter.de
def get_horoscope_mac(zodiac_sign: str):
    res = requests.get(
        f"https://mein.astrocenter.de/horoskop/tag/{zodiac_sign}/")

    soup = BeautifulSoup(res.content, 'lxml')
    horoscope_txt = soup.find_all('div', class_='article-horoscope')
    return horoscope_txt


print(get_horoscope_mac('widder'))
