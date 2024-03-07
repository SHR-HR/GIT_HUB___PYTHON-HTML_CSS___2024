# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
"""""
Дата выполнения ПРАКТИЧЕСКОЙ РАБОТЫ: 06 МАРТА - 07 МАРТА 2024 года.
"""""
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
                                            Практическая работа

                                            Курс: Разработка Web-приложений на Python, с применением Фреймворка Django
                                                                         Дисциплина: Основы программирования на Python

Практическая работа №38: Парсинг данных. Библиотеки - beatifulsoup4 и selenium


                                            Выполните следующие задания:


Задание №1

а) Получить массив однотипных данных (цены) с любого динамического сайта.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Урок от 06.03.2024
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
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

def get_prices(url):
    # Настройка для запуска браузера в фоновом режиме
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    # Используем Chrome в режиме headless
    driver_service = ChromeService(executable_path="I:/IT/PY/LESSON_№38_ПАРСИНГ_ДАННЫХ_06.03.2024/chromedriver-win64/chromedriver.exe")
    driver = webdriver.Chrome(service=driver_service, options=chrome_options)

    try:
        # Получение содержимого страницы с использованием Selenium
        driver.get(url)

        # Даем странице немного времени для загрузки данных (может потребоваться настроить под конкретный сайт)
        driver.implicitly_wait(5)

        # Получаем HTML-код страницы
        page_source = driver.page_source

        # Используем Beautiful Soup для парсинга HTML
        soup = BeautifulSoup(page_source, 'html.parser')

        # Замените этот код на соответствующий для вашего сайта
        # Например, найдем цены по классу CSS
        prices = soup.find_all('div', class_='product-buy__price')

        # Создаем массив цен
        prices_array = [price.text for price in prices]

        return prices_array

    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None

    finally:
        # Закрываем браузер
        driver.quit()

# Замените URL на адрес нужного вам сайта
url = "https://www.dns-shop.kz/catalog/17a8a01d16404e77/smartfony/"

# Получение массива цен
prices_result = get_prices(url)

if prices_result:
    print("Цены на сайте:")
    for price in prices_result:
        print(price)
else:
    print("Не удалось получить цены.")
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
"""
Шаг номер 1

Пример: Импорт необходимых библиотек.

Код:
"""
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
"""
Описание: 

В этом шаге происходит импорт библиотек, необходимых для парсинга веб-страницы.
BeautifulSoup используется для анализа HTML, а webdriver из библиотеки selenium - для автоматизации взаимодействия
с браузером.
"""
"""
Шаг номер 2

Пример: Настройка браузера для запуска в фоновом режиме.

Код:
"""
# Настройка для запуска браузера в фоновом режиме
chrome_options = Options()
chrome_options.add_argument("--headless")
"""
Описание: 

Здесь создается объект chrome_options, к которому добавляется аргумент --headless.
Этот аргумент указывает использовать режим браузера без графического интерфейса (headless).
"""
"""
Шаг номер 3

Пример: Запуск браузера и получение HTML-кода страницы.

Код:
"""
# Используем Chrome в режиме headless
driver_service = ChromeService(executable_path="I:/IT/PY/LESSON_№38_ПАРСИНГ_ДАННЫХ_06.03.2024/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=driver_service, options=chrome_options)

try:
    # Получение содержимого страницы с использованием Selenium
    driver.get(url)

    # Даем странице немного времени для загрузки данных (может потребоваться настроить под конкретный сайт)
    driver.implicitly_wait(5)

    # Получаем HTML-код страницы
    page_source = driver.page_source
"""
Описание: 

Здесь создаются объекты driver_service и driver для управления браузером Chrome.
Браузер запускается в режиме headless, открывается указанный URL, и используется implicitly_wait для
ожидания загрузки данных. Затем HTML-код страницы сохраняется в переменной page_source.
"""
"""
Шаг номер 4

Пример: Парсинг HTML-кода с использованием Beautiful Soup.

Код:
"""
# Используем Beautiful Soup для парсинга HTML
soup = BeautifulSoup(page_source, 'html.parser')
"""
Описание: 

Создается объект soup с использованием BeautifulSoup, который позволяет удобно парсить HTML-код страницы.
"""
"""
Шаг номер 5

Пример: Поиск цен на странице.

Код:
"""
# Замените этот код на соответствующий для вашего сайта
# Например, найдем цены по классу CSS
prices = soup.find_all('div', class_='product-buy__price')
"""
Описание: 

Здесь используется find_all для поиска всех элементов с тегом 'div' и классом 'product-buy__price'.
Этот код нужно заменить на соответствующий для конкретного сайта.
"""
"""
Шаг номер 6

Пример: Создание массива цен.

Код:
"""
# Создаем массив цен
prices_array = [price.text for price in prices]
"""
Описание: 

Создается массив prices_array, в который добавляются текстовые значения найденных цен.
"""
"""
Шаг номер 7

Пример: Закрытие браузера и возврат массива цен.

Код:
"""
finally:
    # Закрываем браузер
    driver.quit()

# Замените URL на адрес нужного вам сайта
url = "https://www.dns-shop.kz/catalog/17a8a01d16404e77/smartfony/"

# Получение массива цен
prices_result = get_prices(url)

if prices_result:
    print("Цены на сайте:")
    for price in prices_result:
        print(price)
else:
    print("Не удалось получить цены.")
"""
Описание: 

В блоке finally закрывается браузер после выполнения всех операций. 
Затем определен URL, вызвана функция get_prices для получения массива цен, и в конце выведены цены на экран
(если получены) или сообщение об ошибке.
"""