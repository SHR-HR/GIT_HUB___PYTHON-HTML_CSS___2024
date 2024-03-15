# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
"""""
Дата выполнения ДОМАШНЕЙ РАБОТЫ: 16 МАРТА 2024 года.
"""""
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
                                            Домашнее задание

                                            Курс: Разработка Web-приложений на Python, с применением Фреймворка Django
                                                                         Дисциплина: Основы программирования на Python

                Домашнее задание №40: Работа с большими данными - pandas, numpy, mathplotlib


                                            Выполните следующие задания:


                    Задание №1
                    а) Создайте массив данных, например с продажей товаров, для будущего анализа.
                    б) Отобразите основные показатели в виде графиков и статистики.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Урок от 15.03.2024
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Вариант кода 1
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
import numpy as np
import matplotlib.pyplot as plt

# Создание массива данных о продажах товаров
sales_data = np.random.randint(100, 1000, size=12)

# Вывод массива данных
print("Массив данных о продажах товаров:")
print(sales_data)

# Отображение графика продаж по месяцам
months = np.arange(1, 13)
plt.plot(months, sales_data, marker='o', linestyle='-')
plt.title('Продажи товаров по месяцам')
plt.xlabel('Месяц')
plt.ylabel('Продажи')
plt.grid(True)
plt.show()

# Вычисление основных статистических показателей
mean_sales = np.mean(sales_data)
max_sales = np.max(sales_data)
min_sales = np.min(sales_data)
range_sales = max_sales - min_sales

# Вывод статистических показателей
print("\nСтатистические показатели:")
print(f"Среднее значение продаж: {mean_sales}")
print(f"Максимальное значение продаж: {max_sales}")
print(f"Минимальное значение продаж: {min_sales}")
print(f"Разница между максимальным и минимальным значениями продаж: {range_sales}")
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Шаг 1: Создание массива данных о продажах товаров
'''
sales_data = np.random.randint(100, 1000, size=12)
"""
Мы используем функцию numpy.random.randint() для генерации случайных целых чисел в диапазоне от 100 до 1000.
Размер массива данных установлен на 12 элементов (для 12 месяцев).
"""
'''
Шаг 2: Вывод массива данных
'''
print("Массив данных о продажах товаров:")
print(sales_data)
"""
С помощью print() мы выводим массив данных о продажах на экран.
"""
'''
Шаг 3: Отображение графика продаж по месяцам
'''
months = np.arange(1, 13)
plt.plot(months, sales_data, marker='o', linestyle='-')
plt.title('Продажи товаров по месяцам')
plt.xlabel('Месяц')
plt.ylabel('Продажи')
plt.grid(True)
plt.show()
"""
Мы создаем массив months, содержащий номера месяцев от 1 до 12 с помощью np.arange(1, 13).
С помощью plt.plot() строится график, где по оси X отображаются месяцы, а по оси Y - продажи.
marker='o' задает маркеры точек на графике, linestyle='-' указывает на сплошную линию.
plt.title(), plt.xlabel() и plt.ylabel() устанавливают заголовок, подпись оси X и подпись оси Y соответственно.
plt.grid(True) включает сетку на графике.
plt.show() отображает график на экране.
"""
'''
Шаг 4: Вычисление основных статистических показателей
'''
mean_sales = np.mean(sales_data)
max_sales = np.max(sales_data)
min_sales = np.min(sales_data)
range_sales = max_sales - min_sales
'''
Мы используем функции np.mean(), np.max() и np.min() для вычисления среднего значения,
максимального и минимального значений продаж соответственно.
Разница между максимальным и минимальным значением вычисляется и сохраняется в переменной range_sales.
'''
"""
Шаг 5: Вывод статистических показателей
"""
print("\nСтатистические показатели:")
print(f"Среднее значение продаж: {mean_sales}")
print(f"Максимальное значение продаж: {max_sales}")
print(f"Минимальное значение продаж: {min_sales}")
print(f"Разница между максимальным и минимальным значениями продаж: {range_sales}")
'''
Мы выводим статистические показатели на экран с помощью print().
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Вариант кода 2
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
import numpy as np
import matplotlib.pyplot as plt

def generate_product_names(num_products):
    """Генерация случайных названий продуктов."""
    products = ["Телефон", "Планшет", "Ноутбук", "Фитнес-трекер", "Камера", "Телевизор", "Наушники",
                "Принтер", "Умные часы", "Игровая консоль"]
    return np.random.choice(products, size=num_products)

def generate_sales_data(num_products, num_months):
    """Генерация случайных данных о продажах товаров."""
    return np.random.randint(100, 1000, size=(num_products, num_months))

def calculate_statistics(data):
    """Вычисление статистических показателей."""
    mean_sales = np.mean(data)
    weighted_mean_sales = np.average(data, weights=np.random.rand(*data.shape))
    max_sales = np.max(data)
    min_sales = np.min(data)
    range_sales = max_sales - min_sales
    return mean_sales, weighted_mean_sales, max_sales, min_sales, range_sales


def print_results(mean_sales, weighted_mean_sales, max_sales, min_sales, range_sales):
    """Вывод результатов вычислений."""
    print("\nСтатистические показатели:")
    print(f"Среднее значение продаж: {mean_sales}")
    print(f"Средневзвешенное значение продаж: {weighted_mean_sales}")
    print(f"Максимальное значение продаж: {max_sales}")
    print(f"Минимальное значение продаж: {min_sales}")
    print(f"Разница между максимальным и минимальным значениями продаж: {range_sales}")

def plot_sales_histogram(data):
    """Построение гистограммы продаж."""
    plt.hist(data.flatten(), bins=20, color='skyblue', edgecolor='black')
    plt.title('Распределение продаж')
    plt.xlabel('Сумма продаж')
    plt.ylabel('Частота')
    plt.grid(True)
    plt.show()

def main():
    num_products = 10  # Количество продуктов
    num_months = 12    # Количество месяцев

    # Генерация случайных названий продуктов
    product_names = generate_product_names(num_products)
    print("Случайные названия продуктов:")
    print(product_names)

    # Генерация данных о продажах
    sales_data = generate_sales_data(num_products, num_months)

    # Вывод массива данных о продажах
    print("\nМассив данных о продажах товаров:")
    print(sales_data)

    # Вычисление статистических показателей
    mean_sales, weighted_mean_sales, max_sales, min_sales, range_sales = calculate_statistics(sales_data)

    # Вывод результатов вычислений
    print_results(mean_sales, weighted_mean_sales, max_sales, min_sales, range_sales)

    # Построение гистограммы продаж
    plot_sales_histogram(sales_data)

if __name__ == "__main__":
    main()
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
"""
Шаг 1: Определение функции generate_product_names(num_products)
"""
def generate_product_names(num_products):
    """Генерация случайных названий продуктов."""
    products = ["Телефон", "Планшет", "Ноутбук", "Фитнес-трекер", "Камера", "Телевизор", "Наушники", "Принтер", "Умные часы", "Игровая консоль"]
    return np.random.choice(products, size=num_products)
'''
Функция generate_product_names(num_products) генерирует случайные названия продуктов.
Она принимает аргумент num_products, который определяет количество случайных названий продуктов,
которые нужно сгенерировать. Внутри функции определен список products, содержащий названия продуктов.
С помощью функции numpy.random.choice() из этого списка случайным образом выбираются num_products названий продуктов.
'''
"""
Шаг 2: Определение функции generate_sales_data(num_products, num_months)
"""
def generate_sales_data(num_products, num_months):
    """Генерация случайных данных о продажах товаров."""
    return np.random.randint(100, 1000, size=(num_products, num_months))
'''
Функция generate_sales_data(num_products, num_months) генерирует случайные данные о продажах товаров.
Она принимает два аргумента: num_products - количество продуктов, и num_months - количество месяцев.
Функция использует функцию numpy.random.randint() для генерации случайных целых чисел в диапазоне от 100 до 1000.
Результат представляет собой массив размером (num_products, num_months), где каждый элемент - это случайное число,
обозначающее объем продаж.
'''
"""
Шаг 3: Определение функции calculate_statistics(data)
"""
def calculate_statistics(data):
    """Вычисление статистических показателей."""
    mean_sales = np.mean(data)
    weighted_mean_sales = np.average(data, weights=np.random.rand(*data.shape))
    max_sales = np.max(data)
    min_sales = np.min(data)
    range_sales = max_sales - min_sales
    return mean_sales, weighted_mean_sales, max_sales, min_sales, range_sales
'''
Функция calculate_statistics(data) вычисляет различные статистические показатели для данных о продажах товаров.
Входной аргумент data - это массив данных о продажах. 
Функция использует функции np.mean(), np.average(), np.max(), np.min() для вычисления среднего значения,
средневзвешенного значения, максимального и минимального значений, а также разницы между максимальным и минимальным
значениями.
'''
"""
Шаг 4: Определение функции print_results(mean_sales, weighted_mean_sales, max_sales, min_sales, range_sales)
"""
def print_results(mean_sales, weighted_mean_sales, max_sales, min_sales, range_sales):
    """Вывод результатов вычислений."""
    print("\nСтатистические показатели:")
    print(f"Среднее значение продаж: {mean_sales}")
    print(f"Средневзвешенное значение продаж: {weighted_mean_sales}")
    print(f"Максимальное значение продаж: {max_sales}")
    print(f"Минимальное значение продаж: {min_sales}")
    print(f"Разница между максимальным и минимальным значениями продаж: {range_sales}")
'''
Функция print_results(mean_sales, weighted_mean_sales, max_sales, min_sales, range_sales) 
выводит результаты вычислений статистических показателей на экран.
'''
"""
Шаг 5: Определение функции plot_sales_histogram(data)
"""
def plot_sales_histogram(data):
    """Построение гистограммы продаж."""
    plt.hist(data.flatten(), bins=20, color='skyblue', edgecolor='black')
    plt.title('Распределение продаж')
    plt.xlabel('Сумма продаж')
    plt.ylabel('Частота')
    plt.grid(True)
    plt.show()
'''
Функция plot_sales_histogram(data) строит гистограмму распределения продаж. 
Она принимает в качестве аргумента массив данных о продажах data. Функция plt.hist() 
используется для построения гистограммы. Настройки заголовка, подписей осей и сетки задаются с 
помощью функций plt.title(), plt.xlabel(), plt.ylabel() и plt.grid().
'''
"""
Шаг 6: Определение функции main()
"""
def main():
    num_products = 10  # Количество продуктов
    num_months = 12    # Количество месяцев

    # Генерация случайных названий продуктов
    product_names = generate_product_names(num_products)
    print("Случайные названия продуктов:")
    print(product_names)

    # Генерация данных о продажах
    sales_data = generate_sales_data(num_products, num_months)

    # Вывод массива данных о продажах
    print("\nМассив данных о продажах товаров:")
    print(sales_data)

    # Вычисление статистических показателей
    mean_sales, weighted_mean_sales, max_sales, min_sales, range_sales = calculate_statistics(sales_data)

    # Вывод результатов вычислений
    print_results(mean_sales, weighted_mean_sales, max_sales, min_sales, range_sales)

    # Построение гистограммы продаж
    plot_sales_histogram(sales_data)

if __name__ == "__main__":
    main()
'''
Функция main() представляет собой основную часть программы. 
Здесь вызываются все остальные функции для выполнения последовательности операций: 
генерация названий продуктов, генерация данных о продажах, вычисление статистических показателей, 
вывод результатов вычислений и построение гистограммы продаж.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Вариант кода 3
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Функция для генерации случайных данных о продажах товаров
def generate_sales_data(num_products, num_months):
    # Список продуктов
    products = ["Телефон", "Планшет", "Ноутбук", "Фитнес-трекер", "Камера", "Телевизор", "Наушники", "Принтер", "Умные часы", "Игровая консоль"]
    # Генерация случайных данных о продажах
    sales_data = np.random.randint(100, 1000, size=(num_products, num_months))
    # Создание DataFrame с данными о продажах и названиями продуктов в качестве индексов
    return pd.DataFrame(sales_data, columns=[f"Месяц {i+1}" for i in range(num_months)], index=products)

# Функция для визуализации основных показателей в виде графиков и статистики
def visualize_statistics(sales_data):
    # График суммарных продаж по месяцам
    sales_data.sum(axis=0).plot(kind='bar', figsize=(10, 6))
    plt.title('Общие продажи по месяцам')
    plt.xlabel('Месяц')
    plt.ylabel('Общие продажи')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.show()

    # Вывод статистики
    print("\nСтатистика:")
    print(sales_data.describe())

def main():
    num_products = 10  # Количество продуктов
    num_months = 12    # Количество месяцев

    # Генерация данных о продажах
    sales_data = generate_sales_data(num_products, num_months)

    # Визуализация статистики
    visualize_statistics(sales_data)

if __name__ == "__main__":
    main()
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
"""
Шаг 1: Определение функции generate_sales_data(num_products, num_months)
"""
def generate_sales_data(num_products, num_months):
    # Список продуктов
    products = ["Телефон", "Планшет", "Ноутбук", "Фитнес-трекер", "Камера", "Телевизор",
                "Наушники", "Принтер", "Умные часы", "Игровая консоль"]
    # Генерация случайных данных о продажах
    sales_data = np.random.randint(100, 1000, size=(num_products, num_months))
    # Создание DataFrame с данными о продажах и названиями продуктов в качестве индексов
    return pd.DataFrame(sales_data, columns=[f"Месяц {i+1}" for i in range(num_months)], index=products)
"""
Функция generate_sales_data(num_products, num_months) генерирует случайные данные о продажах товаров.
Внутри функции определяется список products, содержащий названия продуктов.
Затем с помощью функции np.random.randint() создается массив случайных чисел размером (num_products, num_months)
в диапазоне от 100 до 1000.
Данные о продажах и названия продуктов используются для создания DataFrame с помощью библиотеки pandas. 
Названия продуктов устанавливаются в качестве индексов.
"""
"""
Шаг 2: Определение функции visualize_statistics(sales_data)
"""
def visualize_statistics(sales_data):
    # График суммарных продаж по месяцам
    sales_data.sum(axis=0).plot(kind='bar', figsize=(10, 6))
    plt.title('Общие продажи по месяцам')
    plt.xlabel('Месяц')
    plt.ylabel('Общие продажи')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.show()

    # Вывод статистики
    print("\nСтатистика:")
    print(sales_data.describe())
"""
Функция visualize_statistics(sales_data) используется для визуализации основных
статистических показателей и графиков продаж.

С помощью метода sum(axis=0) суммируются значения по столбцам, то есть по месяцам. 
Затем создается столбчатая диаграмма с помощью plot(kind='bar').

Заголовок, подписи осей, вращение подписей на оси X и сетка на графике 
задаются соответствующими функциями библиотеки matplotlib.pyplot.

Статистика данных выводится с помощью метода describe() для DataFrame.
"""
"""
Шаг 3: Определение функции main()
"""
def main():
    num_products = 10  # Количество продуктов
    num_months = 12    # Количество месяцев

    # Генерация данных о продажах
    sales_data = generate_sales_data(num_products, num_months)

    # Визуализация статистики
    visualize_statistics(sales_data)
"""
Функция main() представляет собой основную часть программы.
В ней определены переменные num_products и num_months, обозначающие количество продуктов и количество месяцев.
Затем генерируются данные о продажах с помощью функции generate_sales_data().
После этого вызывается функция visualize_statistics() для визуализации статистики продаж.
"""
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Вариант кода 4
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Создаем массив данных с продажами товаров
products = ['Телефон', 'Планшет', 'Ноутбук', 'Наушники', 'Телевизор']
sales_data = np.random.randint(100, 1000, size=(len(products), 12))

# Преобразуем массив в DataFrame для удобства работы с данными
sales_df = pd.DataFrame(sales_data, index=products, columns=[f'Месяц {i+1}' for i in range(12)])

# Отображаем графики продаж для каждого товара
sales_df.T.plot(kind='line', figsize=(10, 6))
plt.title('Продажи товаров по месяцам')
plt.xlabel('Месяц')
plt.ylabel('Количество продаж')
plt.grid(True)
plt.legend(title='Товары')
plt.show()

# Выводим статистику по продажам
print('Статистика продаж:\n', sales_df.describe())
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
"""
Шаг 1: Создание массива данных с продажами товаров и преобразование его в DataFrame
"""
# Создаем массив данных с продажами товаров
products = ['Телефон', 'Планшет', 'Ноутбук', 'Наушники', 'Телевизор']
sales_data = np.random.randint(100, 1000, size=(len(products), 12))

# Преобразуем массив в DataFrame для удобства работы с данными
sales_df = pd.DataFrame(sales_data, index=products, columns=[f'Месяц {i+1}' for i in range(12)])
'''
Создается список products, содержащий названия товаров.
С помощью функции np.random.randint() генерируется массив случайных данных о продажах.
Размер массива соответствует количеству товаров (длина списка products) и количеству месяцев (12).
Полученный массив данных преобразуется в DataFrame с помощью pd.DataFrame(). 
Названия товаров устанавливаются в качестве индексов, а названия месяцев формируются с помощью генератора списков.
'''
"""
Шаг 2: Отображение графиков продаж для каждого товара
"""
# Отображаем графики продаж для каждого товара
sales_df.T.plot(kind='line', figsize=(10, 6))
plt.title('Продажи товаров по месяцам')
plt.xlabel('Месяц')
plt.ylabel('Количество продаж')
plt.grid(True)
plt.legend(title='Товары')
plt.show()
'''
Для отображения графиков продаж используется метод plot() объекта DataFrame.
С атрибутом kind='line' указывается тип графика (линейный).
Для того чтобы на графике отображались данные по месяцам, используется транспонирование DataFrame (sales_df.T).
Заголовок графика, подписи осей, наличие сетки и легенда устанавливаются с помощью 
соответствующих функций библиотеки matplotlib.pyplot.
'''
"""
Шаг 3: Вывод статистики по продажам
"""
# Выводим статистику по продажам
print('Статистика продаж:\n', sales_df.describe())
'''
Для вывода статистики по продажам используется метод describe() объекта DataFrame.
Этот метод выводит основные статистические показатели: количество наблюдений, 
среднее значение, стандартное отклонение, минимальное и максимальное значения, а также квартили данных.
'''