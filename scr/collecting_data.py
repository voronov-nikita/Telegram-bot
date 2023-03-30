from requests import get
from bs4 import BeautifulSoup as bs


class SendRequestMOS:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.url = "https://school.mos.ru/"

        self.url_homework = "https://dnevnik.mos.ru/diary/homeworks/homeworks"

        self.name_work = None
        self.url_homework_one = f"https://dnevnik.mos.ru/diary/homeworks/homeworks?subject={self.name_work}"

    def get_homework(self, day=None):
        get(self.url)

