from lang.gen_horoscope import gen_horoscope
from lang.scraper import ZODIAC_SIGNS


def sample_response(input_text):
	user_message = str(input_text).lower()

	if user_message in ("hallo freddy", "widder"):
		return gen_horoscope()
