# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
"""""
Дата выполнения ДОМАШНЕЙ РАБОТЫ: 01 МАРТА - 02 МАРТА 2024 года.
"""""
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
                                            Домашняя работа

                                            Курс: Разработка Web-приложений на Python, с применением Фреймворка Django
                                                                         Дисциплина: Основы программирования на Python

Домашняя работа №37: Парсинг данных. Библиотеки - beatifulsoup4 и selenium


                                            Выполните следующие задания:


Задание №1

а) Получить курс валют с динамического сайта (курс валют), используя selenium.
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
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Установите путь к ChromeDriver
chrome_path = r'I:/IT/PY/LESSON_№37/chromedriver-win64/chromedriver-win64/chromedriver.exe'  # Укажите путь к вашему ChromeDriver

url = 'https://www.currency.me.uk/convert/usd/rub'

# Настройки Chrome
chrome_options = ChromeOptions()
chrome_options.add_argument('--headless')  # Опционально: запуск в фоновом режиме

# Запускаем браузер с помощью Selenium
service = ChromeService(executable_path=chrome_path)
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get(url)

# Ждем, пока элемент с классом "mini ccyrate" станет видимым
curs_element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".mini.ccyrate"))
)

# Получаем текст из элемента
curs = curs_element.text

# Закрываем браузер
driver.quit()

print(curs)
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
Подробнее о коде шаг - за - шагом:
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
1. Импорт библиотек:
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
'''
webdriver: основной класс для взаимодействия с браузером.
By: используется для указания метода поиска элементов.
ChromeService: служит для настройки сервиса, например, пути к драйверу.
ChromeOptions: позволяет настроить параметры Chrome, такие как режим "без головы".
WebDriverWait: ожидание элементов для выполнения действий.
expected_conditions: условия ожидания, такие как видимость элемента.
'''
'''
2. Установка пути к ChromeDriver:
'''
chrome_path = r'I:/IT/PY/LESSON_№37/chromedriver-win64/chromedriver-win64/chromedriver.exe'
'''
Указывает путь к исполняемому файлу ChromeDriver.
'''
'''
3. URL и настройка Chrome:
'''
url = 'https://www.currency.me.uk/convert/usd/rub'

chrome_options = ChromeOptions()
chrome_options.add_argument('--headless')
'''
Задает целевой URL и опции Chrome, включая режим "без головы".
'''
'''
4. Запуск браузера:
'''
service = ChromeService(executable_path=chrome_path)
driver = webdriver.Chrome(service=service, options=chrome_options)
'''
Создает сервис Chrome и запускает браузер с указанными опциями.
'''
'''
5. Открытие страницы:
'''
driver.get(url)
'''
Переходит по указанному URL.
'''
'''
6. Ожидание видимости элемента:
'''
curs_element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".mini.ccyrate"))
)
'''
Использует WebDriverWait для ожидания видимости элемента с CSS-селектором ".mini.ccyrate" в течение 10 секунд.
'''
'''
7. Получение текста из элемента:
'''
curs = curs_element.text
'''
Извлекает текст из найденного элемента.
'''
'''
8. Закрытие браузера:
'''
driver.quit()
'''
Завершает работу браузера после выполнения задачи.
'''
'''
9. Вывод результата:
'''
print(curs)
'''
Выводит полученный курс валюты.
'''