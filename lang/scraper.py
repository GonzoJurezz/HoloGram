from utils_ger import horoscopeOutput
import json
from datetime import datetime
import inspect


ZODIAC_SIGNS = ["widder", "stier", "zwillinge", "krebs", "loewe", "jungfrau",
                "waage", "skorpion", "schuetze", "steinbock", "wassermann",
                "fische"]
JSON_FILE_NAME = "data/"+datetime.today().strftime('%Y%m%d') + ".json"


def get_horoscopes(zodiac_signs:list, functions:list):
    '''
    Scrapes horoscopes from the combination of zodiac signs and scraper
    functions.

    If a scrape is successful it is returned in a list of dicts containing the
    name of the used function, the zodiac sign and the scrapped horoscope text.

    If unsuccessful the function name, zodiac sign and an exception is returned
    in a list of error tuples.

    @type zodiac_signs: list
    @param zodiac_signs: List of strings of zodiac signs

    @type functions: list
    @param functions: List of scraper functions of type str -> str, which are
                      called to scrape horoscope

    @rtype: tuple
    @return: Tuple (hs,errors), where hs is a list of successfully scraped
             horoscopes in a dict
             {"func":func_name, "zodiac_sign":zs, "text":text}
             and errors is a list of tuples (func_name, zs, e), where
             func_name  is the name of the called function as a string,
             zs is the string of the zodiac sign,
             text is the scraped horoscope text
             and e is a thrown exception.

    '''

    hs = []
    errors = []

    for f in functions:
        for zs in ZODIAC_SIGNS:
            try:
                hs.append( {"func":f.__name__, "zodiac_sign":zs, "text":f(zs)} )
            except Exception as e:
                errors.append((f.__name__, zs, e))

    return (hs,errors)


def dump_json(hs:list, file_name:str):
    '''
    Dumps list of python dicts as a json dict into a file.

    @type hs: list
    @param hs: List of dicts to dump

    @type file_name: str
    @param file_name: Path to file where to dump the dict
    '''
    try:
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(hs, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(e)


def main():
    hO = horoscopeOutput

    # Get all functions of the horoscopeOutput class
    attrs = list((getattr(hO, name) for name in dir(hO)))
    functions = [attr for attr in attrs if inspect.isfunction(attr)]
    #rint(list(map(lambda x: x.__name__, functions)))

    #scrape all horoscopes for today
    (hs, errors) = get_horoscopes(ZODIAC_SIGNS, functions)

    # Print errors if any
    if(errors != []):
        print("-----------------ERRORS-----------------")
        for e in errors:
            print(e)

    # Dump json file of todays scraped horoscopes
    dump_json(hs, JSON_FILE_NAME)


if __name__ == '__main__':
    main()
