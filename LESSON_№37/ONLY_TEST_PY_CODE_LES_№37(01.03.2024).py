from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time


def get_currency_rate(url):
    # Настройки для запуска браузера в фоновом режиме (headless mode)
    options = Options()
    options.add_argument('--headless')

    # Установка пользовательского User-Agent
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    ]
    options.add_argument(f'user-agent={random.choice(user_agents)}')

    # Запускаем браузер
    driver = webdriver.Chrome(options=options)

    try:
        # Заходим на страницу
        driver.get(url)

        # Ждем, пока данные полностью загрузятся (может потребоваться настройка)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.BNeawe.iBp4i.AP7Wnd')))

        # Получаем содержимое страницы
        page_source = driver.page_source

        # Теперь можно использовать BeautifulSoup для парсинга страницы
        # Примерно как в предыдущем коде

    finally:
        # Закрываем браузер в любом случае, даже если произошла ошибка
        driver.quit()


# Пример использования:
url = 'https://ru.investing.com/currencies/usd-kzt'
get_currency_rate(url)
