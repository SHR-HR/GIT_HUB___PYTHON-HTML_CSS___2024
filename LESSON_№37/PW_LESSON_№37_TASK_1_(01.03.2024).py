# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
"""""
Дата выполнения ПРАКТИЧЕСКОЙ РАБОТЫ: 01 МАРТА - 02 МАРТА 2024 года.
"""""
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
                                            Практическая работа

                                            Курс: Разработка Web-приложений на Python, с применением Фреймворка Django
                                                                         Дисциплина: Основы программирования на Python

Практическая работа №37: Парсинг данных. Библиотеки - beatifulsoup4 и selenium


                                            Выполните следующие задания:


Задание №1

а) Получить первый абзац с любого динамического сайта.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Урок от 01.03.2024
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Выполнение задания: a)
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
КОД:
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
from bs4 import BeautifulSoup
from selenium import webdriver

def get_first_paragraph_text(url):
    driver = webdriver.Chrome()
    driver.get(url)
    page_source = driver.page_source
    driver.quit()

    soup = BeautifulSoup(page_source, 'html.parser')
    first_paragraph = soup.find('p')

    if first_paragraph:
        return first_paragraph.get_text(strip=True)
    else:
        return "Параграф не найден."

# url0 = 'https://anidubonline.com/'
# result = get_first_paragraph_text(url0)
#
# url1 = 'https://www.anilibria.tv/'
# result = get_first_paragraph_text(url1)

url2 = 'https://habr.com/ru/flows/popsci/articles/'
result = get_first_paragraph_text(url2)

print(result)
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
"""
Подробнее о коде
"""
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Шаг первый: Импорт библиотек:
'''
from bs4 import BeautifulSoup
from selenium import webdriver
'''
BeautifulSoup используется для парсинга HTML-кода в структурированный объект Python.
webdriver из библиотеки Selenium предоставляет инструменты для взаимодействия с браузером через код.
'''
'''
Шаг второй: Определение функции get_first_paragraph_text:
'''
def get_first_paragraph_text(url):
''''
Функция принимает URL в качестве аргумента.
''''
'''
Шаг третий: Открытие браузера с помощью Selenium:
'''
driver = webdriver.Chrome()
driver.get(url)
'''
Создается экземпляр веб-драйвера (в данном случае, Chrome).
Браузер открывает указанный URL.
'''
'''
Шаг четвертый: Получение HTML-кода страницы:
'''
page_source = driver.page_source
'''
driver.page_source используется для получения HTML-кода текущей страницы.
'''
'''
Шаг пятый: Закрытие браузера:
'''
driver.quit()
'''
Закрывается экземпляр веб-драйвера.
'''
'''
Шаг шестой: Использование BeautifulSoup для парсинга:
'''
soup = BeautifulSoup(page_source, 'html.parser')
'''
TML-код передается в BeautifulSoup для создания объекта soup.
'''
'''
Шаг седьмой: Поиск первого параграфа (<p>):
'''
first_paragraph = soup.find('p')
'''
soup.find('p') находит первый тег <p> в HTML-документе.
'''
'''
Шаг восьмой: Получение текста из параграфа:
'''
if first_paragraph:
    return first_paragraph.get_text(strip=True)
else:
    return "Параграф не найден."
'''
Если найден хотя бы один параграф, возвращается его текст без лишних пробелов.
В противном случае возвращается сообщение "Параграф не найден."
'''
'''
Шаг девятый: Примеры использования функции:
'''
url2 = 'https://habr.com/ru/flows/popsci/articles/'
result = get_first_paragraph_text(url2)
print(result)
'''
Пример использования функции с URL Habr. Полученный текст выводится на экран.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Выполнение задания: a)
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
ВАРИАНТ КОДа №2:
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import WebDriverException

class WebPageParser:
    def __init__(self, url, headless=True):
        self.url = url
        self.headless = headless
        self.page_source = None

    def _setup_driver(self):
        options = webdriver.ChromeOptions()
        if self.headless:
            options.add_argument('--headless')
        return webdriver.Chrome(options=options)

    def _get_page_source(self):
        try:
            driver = self._setup_driver()
            driver.get(self.url)
            self.page_source = driver.page_source
        except WebDriverException as e:
            print(f"Ошибка WebDriver: {e}")
        finally:
            driver.quit()

    def get_first_paragraph_text(self):
        self._get_page_source()
        if self.page_source:
            soup = BeautifulSoup(self.page_source, 'html.parser')
            first_paragraph = soup.find('p')
            return first_paragraph.get_text(strip=True) if first_paragraph else "Параграф не найден."
        else:
            return "Не удалось получить исходный код страницы."

# Пример использования класса
url_to_parse = 'https://habr.com/ru/flows/popsci/articles/'
parser = WebPageParser(url_to_parse)
result_text = parser.get_first_paragraph_text()

# Запись результата в файл
with open('result.txt', 'w', encoding='utf-8') as file:
    file.write(result_text)
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
"""
Подробнее о коде
"""
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Шаг первый: Импорт библиотек:
'''
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
'''
BeautifulSoup используется для парсинга HTML-кода в структурированный объект Python.
webdriver из библиотеки Selenium предоставляет инструменты для взаимодействия с браузером через код.
WebDriverException - исключение, которое может возникнуть при работе с веб-драйвером.
'''
'''
Шаг второй: Определение класса WebPageParser:
'''
class WebPageParser:
    def __init__(self, url, headless=True):
        self.url = url
        self.headless = headless
        self.page_source = None
'''
Класс принимает URL страницы и флаг headless, который определяет,
будет ли использоваться режим без отображения браузера.
'''
'''
Шаг третий: Метод _setup_driver:
'''
def _setup_driver(self):
    options = webdriver.ChromeOptions()
    if self.headless:
        options.add_argument('--headless')
    return webdriver.Chrome(options=options)
'''
Создает и настраивает веб-драйвер (в данном случае, Chrome) с учетом параметра headless.
'''
'''
Шаг четвертый: Метод _get_page_source:
'''
def _get_page_source(self):
    try:
        driver = self._setup_driver()
        driver.get(self.url)
        self.page_source = driver.page_source
    except WebDriverException as e:
        print(f"Ошибка WebDriver: {e}")
    finally:
        driver.quit()
'''
Открывает браузер, получает HTML-код страницы и закрывает браузер.
В случае возникновения ошибки WebDriverException, выводится сообщение.
'''
'''
Шаг пятый: Метод get_first_paragraph_text:
'''
def get_first_paragraph_text(self):
    self._get_page_source()
    if self.page_source:
        soup = BeautifulSoup(self.page_source, 'html.parser')
        first_paragraph = soup.find('p')
        return first_paragraph.get_text(strip=True) if first_paragraph else "Параграф не найден."
    else:
        return "Не удалось получить исходный код страницы."
'''
Вызывает _get_page_source и затем использует BeautifulSoup для поиска первого параграфа на странице.
'''
'''
Шаг шестой: Пример использования класса:
'''
url_to_parse = 'https://habr.com/ru/flows/popsci/articles/'
parser = WebPageParser(url_to_parse)
result_text = parser.get_first_paragraph_text()
'''
Создается объект WebPageParser для указанного URL.
Вызывается метод get_first_paragraph_text для получения текста первого параграфа.
'''
'''
Шаг седьмой: Запись результата в файл:
'''
with open('result.txt', 'w', encoding='utf-8') as file:
    file.write(result_text)
'''
Результат записывается в текстовый файл 'result.txt'.
'''