# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
"""""
Дата выполнения Домашней-Работы: 28 - ФЕВРАЛЯ - 29 ФЕВРАЛЯ 2024 года.
"""""
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Домашняя работа

Курс: Разработка Web-приложений на Python, с применением Фреймворка Django
Дисциплина: Основы программирования на Python

Домашняя работа №36: Парсинг данных. Библиотеки beatifulsoup4 и selenium

Выполните следующие задания:

Задание №1

а) Получить погоду в Астане с статического сайта погоды, используя string.split()
б) Получить погоду в Астане с статического сайта погоды, используя bs4
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Урок от 28.02.2024
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Выполнение задания: a) и б) - В одном коде.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
КОД:
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
import requests
from bs4 import BeautifulSoup

def get_weather_with_split(url):
    try:
        headers = {'User-Agent':
                       'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                       'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        # Используйте split() для разделения текста страницы
        start_tag = '<span class="temp">'
        end_tag = '</span>'
        start_index = response.text.find(start_tag)
        end_index = response.text.find(end_tag, start_index + len(start_tag))

        temperature_info = response.text[start_index + len(start_tag):end_index]

        print(f"Текущая температура в Астане (используя split()): {temperature_info}")

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе страницы {url}: {e}")

def get_weather_with_bs4(url):
    try:
        headers = {'User-Agent':
                       'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                       'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        temperature_element = soup.find(class_='temp')

        if temperature_element:
            temperature = temperature_element.get_text()
            print(f"Текущая температура в Астане (используя bs4): {temperature}")
        else:
            print("Не удалось найти информацию о температуре на странице.")

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе страницы {url}: {e}")

if __name__ == "__main__":
    accuweather_url = "https://www.accuweather.com/ru/kz/astana/222343/weather-forecast/222343"
    get_weather_with_split(accuweather_url)
    get_weather_with_bs4(accuweather_url)
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
"""
Импорт библиотек:
"""
import requests
from bs4 import BeautifulSoup
"""
Здесь мы импортируем библиотеки requests для отправки HTTP-запросов и BeautifulSoup для парсинга HTML-кода.
"""
"""
Определение функции get_weather_with_split:
"""
def get_weather_with_split(url):
""""
Эта функция принимает URL в качестве аргумента и использует метод split() для обработки HTML-кода.
""""
"""
Попытка выполнения запроса с использованием split():
"""
try:
    # аналогично предыдущему коду
    temperature_info = response.text[start_index + len(start_tag):end_index]
    print(f"Текущая температура в Астане (используя split()): {temperature_info}")
"""
Здесь мы используем метод split() для разделения текста страницы и извлечения информации о температуре.
"""
'''
Определение функции get_weather_with_bs4:
'''
def get_weather_with_bs4(url):
''''
Эта функция также принимает URL в качестве аргумента,
но использует библиотеку BeautifulSoup для более надежного парсинга HTML-кода.
''''
'''
Попытка выполнения запроса с использованием BeautifulSoup:
'''
try:
    # так-же аналогично предыдущему коду
    temperature_element = soup.find(class_='temp')
    if temperature_element:
        temperature = temperature_element.get_text()
        print(f"Текущая температура в Астане (используя bs4): {temperature}")
    else:
        print("Не удалось найти информацию о температуре на странице.")
'''
Здесь мы используем BeautifulSoup для поиска элемента с классом 'temp' и извлечения текстовой информации о температуре.
'''
'''
Обработка исключений:
'''
except requests.exceptions.RequestException as e:
    print(f"Ошибка при запросе страницы {url}: {e}")
'''
В случае возникновения исключения (например, при ошибке запроса), мы выводим сообщение об ошибке.
'''
'''
Основная часть программы:
'''
if __name__ == "__main__":
    accuweather_url = "https://www.accuweather.com/ru/kz/astana/222343/weather-forecast/222343"
    get_weather_with_split(accuweather_url)
    get_weather_with_bs4(accuweather_url)
'''
Здесь мы проверяем, выполняется ли код как самостоятельная программа,
и если да, вызываем обе функции для получения информации о температуре с использованием split() 
и BeautifulSoup соответственно.
'''

