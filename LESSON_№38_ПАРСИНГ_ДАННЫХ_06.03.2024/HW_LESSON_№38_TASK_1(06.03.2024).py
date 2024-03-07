# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
"""""
Дата выполнения ДОМАШНЕЙ РАБОТЫ: 06 МАРТА - 07 МАРТА 2024 года.
"""""
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
                                            Домашняя работа

                                            Курс: Разработка Web-приложений на Python, с применением Фреймворка Django
                                                                         Дисциплина: Основы программирования на Python

Домашняя работа №38: Парсинг данных. Библиотеки - beatifulsoup4 и selenium


                                            Выполните следующие задания:


Задание №1

а) Получить все цены с динамического сайта маркетплейса, используя selenium.
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
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

def get_prices(url):
    # Настройка для запуска браузера в фоновом режиме
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    # Укажите путь к вашему драйверу Chrome
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
        prices = soup.find_all('span', class_='item-card__prices-price')

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
url = "https://kaspi.kz/shop/karaganda/c/smartphones/?q=%3Acategory%3ASmartphones&sort=created-desc&sc"

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
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
"""
Описание: 

Здесь импортируются библиотеки для автоматизации браузера (Selenium) и парсинга HTML-кода (BeautifulSoup).
"""
"""
Шаг номер 2

Пример: Определение функции get_prices.

Код:
"""
def get_prices(url):
    # Настройка для запуска браузера в фоновом режиме
    chrome_options = Options()
    chrome_options.add_argument("--headless")
"""
Описание: 

Создается функция get_prices, которая принимает URL в качестве параметра.
Также настраиваются опции для браузера, чтобы он работал в режиме headless (без графического интерфейса).
"""
"""
Шаг номер 3

Пример: Запуск браузера и получение HTML-кода страницы.

Код:
"""
# Укажите путь к вашему драйверу Chrome
driver_service = ChromeService(
    executable_path="I:/IT/PY/LESSON_№38_ПАРСИНГ_ДАННЫХ_06.03.2024/chromedriver-win64/chromedriver.exe")
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

Создаются объекты для сервиса и драйвера Chrome. 
Драйвер запускается с использованием указанного пути к исполняемому файлу. 
Затем браузер открывает указанный URL, и с помощью implicitly_wait предоставляется некоторое время для загрузки данных.
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

Создается объект soup с использованием BeautifulSoup, чтобы удобно парсить HTML-код страницы.
"""
"""
Шаг номер 5

Пример: Поиск цен на странице.

Код:
"""
# Замените этот код на соответствующий для вашего сайта
# Например, найдем цены по классу CSS
prices = soup.find_all('span', class_='item-card__prices-price')
"""
Описание: 

Здесь используется find_all для поиска всех элементов с тегом 'span' и классом 'item-card__prices-price'.
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
Описание: Создается массив prices_array, в который добавляются текстовые значения найденных цен.
"""
"""
Шаг номер 7

Пример: Закрытие браузера и возврат массива цен.

Код:
"""
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None

    finally:
        # Закрываем браузер
        driver.quit()

# Замените URL на адрес нужного вам сайта
url = "https://kaspi.kz/shop/karaganda/c/smartphones/?q=%3Acategory%3ASmartphones&sort=created-desc&sc"

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