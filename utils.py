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


def get_horoscope_by_day_ger(zodiac_sign: str):
    res = requests.get(
        f"https://www.astrolantis.de/tageshoroskop-{zodiac_sign}.php")

    soup = BeautifulSoup(res.content, 'html.parser')
    data = soup.find('div', attrs={'class': 'main-horoscope'})
    return data.p.text
