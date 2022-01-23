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
    horoscope_txt = soup.find('div', class_='txt')
    return horoscope_txt.p.text


# horoskop: www.astroportal.com
def get_horoscope_ap(zodiac_sign: str):
    res = requests.get(
        f"https://www.astroportal.com/tageshoroskope/{zodiac_sign}/")

    soup = BeautifulSoup(res.content, 'lxml')
    horoscope_txt = soup.find('div', class_='h2')
    return soup.p.text


print(get_horoscope_ap('widder'))
