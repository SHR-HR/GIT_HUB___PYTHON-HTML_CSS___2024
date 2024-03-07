import requests
import csv
import time
from lxml import html


# проблема с 204 кодом решается добавлением хедеров
# делать задержку при парсинге рандомом в несколько секунд
# рандом хедеров
# пейджинация чуть хитрее, потому что несуществующие страницы отдают 200 код, а не 404
# сайт банит, даже если делаешь не много запросов, нужно пилить либо через прокси, либо через selenium
# если нет в наличии, ценник зелёным цветом и вёрстка меняется

# надо писать:
# 1. функция сбора урл +
# 2. функция парсинга каждого товара +
# 3. функция записи в csv +
# 4. функция работы через прокси - осталось доделать
headers = {
    'authority': 'https://www.google.com/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'referer': 'https://www.google.com/',
    'accept-language': 'ru-RU, ru;q=0.9',
}
url = 'https://www.pleer.ru/list_svetodiodnye-dizajnerskie-lampochki.html'
domain = 'https://www.pleer.ru/'
ALL_DATA = dict()
QUEUE_URL = set()


def add_to_csv_from_file(product_dict):
    # записывает по очереди данные, полученные из словаря со спаршенными значениями в виде словаря в csv-файл

    with open('data.csv', 'a', newline='') as csvfile:
        fieldnames = ["Name", "Price", "Id", "Title"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL)
        writer.writerow(product_dict)


def get_data(product_link):
    # принимает на вход один урл товара, парсит данные
    # она их никуда не записывает, возвращает список данных в виде словаря

    product = dict()
    r = requests.get(product_link, headers=headers)
    tree = html.fromstring(r.content)
    product_name = tree.xpath("//span[@class='product_title']")
    product_id = tree.xpath("//div[@class='product_id']")
    product_price = tree.xpath("//div[@class='product_price product_price_color4']"
                               "/div[@class='price']/div[@class='hide']")
    product_title = tree.findtext('.//title')
    product['Title'] = product_title
    for name in product_name:
        print(name.text)
        product['Name'] = name.text
    for price in product_price:
        print(price.text)
        product['Price'] = price.text
    for id in product_id:
        print(id.text)
        product['Id'] = id.text
    time.sleep(3)

    return product


def get_links(page_url):
    # функция принимает на вход урл, берёт все ссылки с него на товары из листинга, проходит по пейдижнации
    # складывает ссылки в множество QUEUE_URL

    first_url = page_url.split(".html")[0]
    pages_count = 0
    r = requests.get(page_url, headers=headers)
    tree = html.fromstring(r.content)
    # поставить условие, если не содержит основного контента - стоп и печать ошибки
    first_page_links = tree.xpath('//div[@class="product_link h3"]//a/@href')
    print('Код ответа корневого УРЛ: ', r.status_code)
    time.sleep(3)

    while True:
        pages_count += 1
        page_url = f'{first_url}_page{pages_count}.html'
        print("Проверяю доступность урл:", page_url)
        r = requests.get(url, headers=headers)
        tree = html.fromstring(r.content)
        # поставить условие, если не содержит основного контента - стоп и печать ошибки
        page_links = tree.xpath('//div[@class="product_link h3"]//a/@href')

        for one_link in page_links:

            QUEUE_URL.add(domain+one_link) # add to QUEUE

        print('Все ссылки со страниц добавил в очередь')

        if r.status_code == 404 or page_links == first_page_links:
            print('Останавливаю цикл, все страницы пейджинации спарсил')
            break

        time.sleep(3)


def main():
    with open('data.csv', 'a', newline='') as csvfile:
        fieldnames = ["Name", "Price", "Id", "Title"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL)
        writer.writeheader()

    get_links(url)

    while len(QUEUE_URL) != 0:
        current_url = QUEUE_URL.pop()
        add_to_csv_from_file(get_data(current_url))


if __name__ == '__main__':
    main()

    from bs4 import BeautifulSoupas

    soup
from urllib.request import urlopen as uReq

# Request from the webpage
myurl = "https://www.flipkart.com/search?q=iphones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

uClient = uReq(myurl)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, features="html.parser")

# print(soup.prettify(containers[0]))

# This variable held all html of webpage
containers = page_soup.find_all("div", {"class": "_3O0U0u"})
# container = containers[0]
# # print(soup.prettify(container))
#
# price = container.find_all("div",{"class": "col col-5-12 _2o7WAb"})
# print(price[0].text)
#
# ratings = container.find_all("div",{"class": "niH0FQ"})
# print(ratings[0].text)
#
# #
# # print(len(containers))
# print(container.div.img["alt"])

# Creating CSV File that will store all data
filename = "product1.csv"
f = open(filename, "w")

headers = "Product_Name,Pricing,Ratings\n"
f.write(headers)

for container in containers:
    product_name = container.div.img["alt"]

    price_container = container.find_all("div", {"class": "col col-5-12 _2o7WAb"})
    price = price_container[0].text.strip()

    rating_container = container.find_all("div", {"class": "niH0FQ"})
    ratings = rating_container[0].text

    # print("product_name:"+product_name)
    # print("price:"+price)
    # print("ratings:"+ str(ratings))

    edit_price = ''.join(price.split(','))
    sym_rupee = edit_price.split("?")
    add_rs_price = "Rs" + sym_rupee[1]
    split_price = add_rs_price.split("E")
    final_price = split_price[0]

    split_rating = str(ratings).split(" ")
    final_rating = split_rating[0]

    print(product_name.replace(",", "|") + "," + final_price + "," + final_rating + "\n")
f.write(product_name.replace(",", "|") + "," + final_price + "," + final_rating + "\n")

f.close()

import unittest

# First we import the class which we want to test.
import Person1 as PerClass


class Test(unittest.TestCase):
    """
    The basic class that inherits unittest.TestCase
    """
    person = PerClass.Person()  # instantiate the Person Class
    user_id = []  # This variable stores the obtained user_id
    user_name = []  # This variable stores the person name

    # It is a test case function to check the Person.set_name function
    def test_0_set_name(self):
        print("Start set_name test\n")

        for i in range(4):
            # initialize a name
            name = 'name' + str(i)
            # put the name into the list variable
            self.user_name.append(name)
            # extraxt the user id obtained from the function
            user_id = self.person.set_name(name)
            # check if the obtained user id is null or not
            self.assertIsNotNone(user_id)
            # store the user id to the list
            self.user_id.append(user_id)
        print("The length of user_id is = ", len(self.user_id))
        print(self.user_id)
        print("The length of user_name is = ", len(self.user_name))
        print(self.user_name)
        print("\nFinish set_name test\n")

        # Second test case function to check the Person.get_name function

    def test_1_get_name(self):
        print("\nStart get_name test\n")

        # total number of stored user information
        length = len(self.user_id)
        print("The length of user_id is = ", length)
        print("The lenght of user_name is = ", len(self.user_name))
        for i in range(6):
            # if i not exceed total length then verify the returned name
            if i < length:
                # if the two name not matches it will fail the test case
                self.assertEqual(self.user_name[i], self.person.get_name(self.user_id[i]))
            else:
                print("Testing for get_name no user test")
                # if length exceeds then check the 'no such user' type message
                self.assertEqual('There is no such user', self.person.get_name(i))
        print("\nFinish get_name test\n")


if __name__ == '__main__':
    # begin the unittest.main()
    unittest.main()
