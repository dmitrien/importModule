from translate import Translator
from aplication.db.people import get_employees
from aplication.salary import calculate_salary
import datetime

def translate():
    translator = Translator(to_lang="ar")  # Язык на который надо перевести принимает значение ISO_639-1 https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
    translation = translator.translate("Helloy world") # Фраза которую надо перевести
    return translation


if __name__ == '__main__':
    print(translate)
    get_employees()
    calculate_salary()
    print(datetime.datetime.now())

