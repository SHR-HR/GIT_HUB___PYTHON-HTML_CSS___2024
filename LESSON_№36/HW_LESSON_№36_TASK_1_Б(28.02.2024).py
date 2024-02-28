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
Выполнение задания: б)
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
КОД:
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
import requests
from bs4 import BeautifulSoup

def get_weather_with_bs4(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                                 ' Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        temperature_element = soup.find(class_='temp')

        if temperature_element:
            temperature = temperature_element.get_text()
            print(f"Текущая температура в Астане: {temperature}")
        else:
            print("Не удалось найти информацию о температуре на странице.")

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе страницы {url}: {e}")

if __name__ == "__main__":
    accuweather_url = "https://www.accuweather.com/ru/kz/astana/222343/weather-forecast/222343"
    get_weather_with_bs4(accuweather_url)
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
"""
Этот скрипт позволяет получить текущую температуру в Астане с веб-страницы AccuWeather с использованием
парсинга HTML с помощью библиотеки BeautifulSoup.
"""
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
1. Импорт библиотек:
'''
import requests
from bs4 import BeautifulSoup
'''
Здесь мы импортируем две библиотеки: requests для выполнения HTTP-запросов и BeautifulSoup для парсинга HTML.
'''
'''
2. Определение функции get_weather_with_bs4:
'''
def get_weather_with_bs4(url):
''''
Эта функция принимает URL в качестве параметра и использует requests для получения HTML-кода страницы.
''''
'''
3. Установка заголовков (headers) для HTTP-запроса:
'''
headers = {'User-Agent': 'Mozilla/5.0 '
                         '(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                         ' Chrome/91.0.4472.124 Safari/537.36'}
'''
Здесь мы создаем словарь заголовков, который эмулирует браузер.
Это может быть полезно для предотвращения блокировки запросов от веб-сервера.
'''
'''
4. Отправка HTTP-запроса и создание объекта BeautifulSoup:
'''
response = requests.get(url, headers=headers)
response.raise_for_status()
soup = BeautifulSoup(response.text, 'html.parser')
'''
Мы отправляем GET-запрос с использованием указанных заголовков, проверяем, не возникла ли ошибка,
и создаем объект BeautifulSoup для парсинга HTML-кода страницы.
'''
'''
5. Поиск элемента с классом 'temp':
'''
temperature_element = soup.find(class_='temp')
'''
Мы используем метод find для поиска элемента с классом 'temp' (который, вероятно, содержит информацию о температуре).
'''
'''
6. Извлечение и вывод информации о температуре:
'''
if temperature_element:
    temperature = temperature_element.get_text()
    print(f"Текущая температура в Астане: {temperature}")
else:
    print("Не удалось найти информацию о температуре на странице.")
'''
Если элемент с классом 'temp' найден, мы извлекаем текст из этого элемента и выводим текущую температуру.
В противном случае выводится сообщение об ошибке.
'''
'''
7. Обработка исключений:
'''
except requests.exceptions.RequestException as e:
    print(f"Ошибка при запросе страницы {url}: {e}")
'''
Если при запросе возникает исключение (например, ошибка HTTP или сетевая ошибка),
оно будет обработано, и будет выведено сообщение с ошибкой.
'''
'''
8. Вызов функции при запуске программы:
'''
if __name__ == "__main__":
    accuweather_url = "https://www.accuweather.com/ru/kz/astana/222343/weather-forecast/222343"
    get_weather_with_bs4(accuweather_url)
'''
Функция get_weather_with_bs4 вызывается с URL AccuWeather при запуске программы.
'''