# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
"""""
Дата выполнения ДОМАШНЕЙ РАБОТЫ: 14 МАРТА 2024 года.
"""""
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
                                            Домашнее задание

                                            Курс: Разработка Web-приложений на Python, с применением Фреймворка Django
                                                                         Дисциплина: Основы программирования на Python

                Домашнее задание №39: Работа с большими данными - pandas, numpy, mathplotlib


                                            Выполните следующие задания:


                    Задание №1
                    а) Создайте массив данных, например с продажей товаров, для будущего анализа.
                    б) Используйте стандартные математические методы из библиотек для анализа данных:
                        среднее, средневзвешенное, максимальное-минимальное и другие.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Урок от 13.03.2024
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
import numpy as np

def generate_product_names(num_products):
    """Генерация случайных названий продуктов."""
    products = ["Наушники", "Планшет", "Телефон", "Игровая консоль", "Телевизор", "Ноутбук", "Принтер",
                "Чайник", "Пылесос", "Камера"]
    return np.random.choice(products, size=num_products)

def generate_sales_data(product_names, num_months):
    """Генерация случайных данных о продажах товаров."""
    num_products = len(product_names)
    return np.random.randint(100, 1000, size=(num_products, num_months))

def print_sales_data(product_names, sales_data):
    """Отображение массива данных о продажах товаров."""
    print("Массив данных о продажах товаров:")
    for i, product in enumerate(product_names):
        print(f"{product} - {sales_data[i]}")

def print_results(mean_sales, weighted_mean_sales, max_sales, min_sales, range_sales):
    """Вывод результатов вычислений."""
    print("\nСтатистические показатели:")
    print(f"Среднее значение продаж: {mean_sales}")
    print(f"Средневзвешенное значение продаж: {weighted_mean_sales}")
    print(f"Максимальное значение продаж: {max_sales}")
    print(f"Минимальное значение продаж: {min_sales}")
    print(f"Разница между максимальным и минимальным значениями продаж: {range_sales}")

def main():
    num_products = 10  # Количество продуктов
    num_months = 12    # Количество месяцев

    # Генерация случайных названий продуктов
    product_names = generate_product_names(num_products)
    print("Случайные названия продуктов:")
    print(product_names)

    # Генерация данных о продажах
    sales_data = generate_sales_data(product_names, num_months)

    # Вывод массива данных о продажах
    print_sales_data(product_names, sales_data)

    # Вычисление статистических показателей
    mean_sales = np.mean(sales_data)
    weights = np.random.rand(*sales_data.shape)  # Случайные веса для каждого продукта
    weighted_mean_sales = np.average(sales_data, weights=weights)
    max_sales = np.max(sales_data)
    min_sales = np.min(sales_data)
    range_sales = max_sales - min_sales

    # Вывод результатов вычислений
    print_results(mean_sales, weighted_mean_sales, max_sales, min_sales, range_sales)

if __name__ == "__main__":
    main()
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Для начала нужен импорт библиотек:
'''
import numpy as np
'''
Далее уже стандартно......
'''
'''
Шаг №1: Генерация случайных названий продуктов.
'''
def generate_product_names(num_products):
    """Генерация случайных названий продуктов."""
    products = ["Наушники", "Планшет", "Телефон", "Игровая консоль",
                "Телевизор", "Ноутбук", "Принтер", "Чайник", "Пылесос", "Камера"]
    return np.random.choice(products, size=num_products)
'''
Эта функция создает случайные названия продуктов из списка products. 
Она принимает аргумент num_products, указывающий количество продуктов для генерации. 
Затем она возвращает массив случайно выбранных названий продуктов. 
В данном случае использована функция numpy.random.choice, которая выбирает случайные элементы из заданного массива.
'''
'''
Шаг №2: Генерация случайных данных о продажах товаров.
'''
def generate_sales_data(product_names, num_months):
    """Генерация случайных данных о продажах товаров."""
    num_products = len(product_names)
    return np.random.randint(100, 1000, size=(num_products, num_months))
'''
Эта функция создает случайные данные о продажах товаров.
Она принимает аргументы product_names - массив с названиями продуктов и num_months - количество месяцев,
за которое предполагается собрать данные о продажах. 
Функция сначала определяет количество продуктов по длине массива product_names, 
затем генерирует случайные данные о продажах с помощью функции numpy.random.randint, 
которая возвращает случайные целые числа в заданном диапазоне (от 100 до 1000) для каждого месяца и продукта.
'''
'''
Шаг №3: Отображение массива данных о продажах товаров.
'''
def print_sales_data(product_names, sales_data):
    """Отображение массива данных о продажах товаров."""
    print("Массив данных о продажах товаров:")
    for i, product in enumerate(product_names):
        print(f"{product} - {sales_data[i]}")
'''
Эта функция принимает массив с названиями продуктов product_names и массив с данными о продажах sales_data.
Она отображает каждый продукт и соответствующие ему данные о продажах. Используется цикл for,
чтобы перебрать каждый элемент массива product_names и соответствующий ему элемент в массиве sales_data.
'''
'''
Шаг №4: Вывод результатов вычислений.
'''
def print_results(mean_sales, weighted_mean_sales, max_sales, min_sales, range_sales):
    """Вывод результатов вычислений."""
    print("\nСтатистические показатели:")
    print(f"Среднее значение продаж: {mean_sales}")
    print(f"Средневзвешенное значение продаж: {weighted_mean_sales}")
    print(f"Максимальное значение продаж: {max_sales}")
    print(f"Минимальное значение продаж: {min_sales}")
    print(f"Разница между максимальным и минимальным значениями продаж: {range_sales}")
'''
Эта функция принимает статистические данные о продажах: среднее значение mean_sales,
средневзвешенное значение weighted_mean_sales, максимальное значение max_sales, минимальное
значение min_sales и разницу между максимальным и минимальным значениями range_sales. 
Она выводит эти данные для анализа.
'''
'''
Шаг №5: Главная функция программы.
'''
def main():
    num_products = 10  # Количество продуктов
    num_months = 12    # Количество месяцев

    # Генерация случайных названий продуктов
    product_names = generate_product_names(num_products)
    print("Случайные названия продуктов:")
    print(product_names)

    # Генерация данных о продажах
    sales_data = generate_sales_data(product_names, num_months)

    # Вывод массива данных о продажах
    print_sales_data(product_names, sales_data)

    # Вычисление статистических показателей
    mean_sales = np.mean(sales_data)
    weights = np.random.rand(*sales_data.shape)  # Случайные веса для каждого продукта
    weighted_mean_sales = np.average(sales_data, weights=weights)
    max_sales = np.max(sales_data)
    min_sales = np.min(sales_data)
    range_sales = max_sales - min_sales

    # Вывод результатов вычислений
    print_results(mean_sales, weighted_mean_sales, max_sales, min_sales, range_sales)

if __name__ == "__main__":
    main()
'''
Эта функция является главной функцией программы. 
Она определяет количество продуктов и количество месяцев, затем вызывает функции для генерации 
случайных названий продуктов и данных о продажах. После этого вычисляет статистические 
показатели продаж и выводит результаты.
'''