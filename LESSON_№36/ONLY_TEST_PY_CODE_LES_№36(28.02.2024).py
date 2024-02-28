import requests
from bs4 import BeautifulSoup

def get_weather_with_split(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()


        start_tag = '<span class="temp">'
        end_tag = '</span>'
        start_index = response.text.find(start_tag)
        end_index = response.text.find(end_tag, start_index + len(start_tag))

        if start_index != -1 and end_index != -1:
