import requests
import os
from bs4 import BeautifulSoup

dir = "D:/Dev/Python/Py232e/Lesson37"
os.chdir(dir)

def getContentFromWebSite(url):
    content = requests.get(url)
    return content.text

html_doc = getContentFromWebSite('http://html.kz%27/)
soup = BeautifulSoup(html_doc, 'html.parser')
soup.prettify()


print(soup.title.string)