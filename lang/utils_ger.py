import requests
from bs4 import BeautifulSoup


class horoscopeOutput:

    # horoskop: mein-horoskop-jeden-tag.com
        def get_horoscope_mhjt(zodiac_sign: str):
            if zodiac_sign == 'loewe':
                zodiac_sign ='lowe'
            if zodiac_sign == 'schuetze':
                zodiac_sign ='schutze'

            res = requests.get(
            f"https://www.mein-horoskop-jeden-tag.com/horoskop/heute/{zodiac_sign}.htm")

            soup = BeautifulSoup(res.content, 'lxml')
            horoscope_txt = soup.find('div', class_='txt').p.text
            return horoscope_txt

    # horoskop: www.astroportal.com
        def get_horoscope_ap(zodiac_sign: str):
            res = requests.get(
                f"https://www.astroportal.com/tageshoroskope/{zodiac_sign}/")

            soup = BeautifulSoup(res.content, 'lxml')
            horoscope_txt = soup.find('h4', class_ ='h2').parent.p.text
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
                f"https://mein.astrocenter.de/horoskop/tag/{zodiac_sign}")

            soup = BeautifulSoup(res.content, 'lxml')
            horoscope_txt = soup.find('div', class_='article-horoscope').p.text
            return horoscope_txt

    # horoskop: https://sternbild-horoskop.de
        def get_horoscope_shk(zodiac_sign: str):
            res = requests.get(
                f"https://sternbild-horoskop.de/tageshoroskop/horoskop-{zodiac_sign}/")

            soup = BeautifulSoup(res.content, 'lxml')
            # class is always widder on this site
            horoscope_txt = soup.find('div', class_=f'avia_textblock horoskop_text widder').div.text
            return horoscope_txt

    # horoskop: https://www.cosmopolitan.de
        def get_horoscope_cmp(zodiac_sign: str):
            res = requests.get(
                f"https://www.cosmopolitan.de/tageshoroskop/heute/{zodiac_sign}")

            soup = BeautifulSoup(res.content, 'lxml')
            horoscope_txt = soup.find('div', class_='bx-content--horoscope bx-js-horoscope-1-1').div.div.text
            return horoscope_txt



def main():
    print(horoscopeOutput.get_horoscope_cmp('widder'))


if __name__ == '__main__':
    main()
