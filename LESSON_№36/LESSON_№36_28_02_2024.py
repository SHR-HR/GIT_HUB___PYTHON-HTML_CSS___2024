import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_all_links(url, depth=1, max_depth=3):
    if depth > max_depth:
        return []

    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        links = [a['href'] for a in soup.find_all('a', href=True)]
        absolute_links = [urljoin(url, link) for link in links]

        for link in absolute_links:
            print(link)

            # Рекурсивный вызов для следующей страницы
            get_all_links(link, depth + 1, max_depth)

        return absolute_links

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе страницы {url}: {e}")
        return []

if __name__ == "__main__":
    starting_url = input("Введите начальный URL: ")
    get_all_links(starting_url)



