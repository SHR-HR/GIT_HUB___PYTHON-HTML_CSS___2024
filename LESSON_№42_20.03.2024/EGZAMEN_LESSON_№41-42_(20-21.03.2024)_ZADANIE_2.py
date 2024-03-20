# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
"""""
Дата выполнения ЭКЗАМЕНАЦИОННОЙ РАБОТЫ: 20 и 21 МАРТА 2024 года.
"""""
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
                                                    ЭКЗАМЕН

                                            Курс: Разработка Web-приложений на Python, с применением Фреймворка Django
                                                                         Дисциплина: Основы программирования на Python

                                            Тема занятия №41-42 : Экзамен


                                            Выполните следующие задания:


Выполните следующие задания:

1. Используйте ООП

Пиццерия предлагает клиентам три вида пиццы: Пепперони, Барбекю и Дары Моря,
каждая из которых определяется тестом, соусом и начинкой.

Требуется спроектировать и реализовать приложение для терминала, позволяющее обеспечить обслуживание посетителей.

Дополнительная информация

В бизнес-процессе работы пиццерии в контексте задачи можно выделить 3 сущности (объекта):

Терминал: отвечает за взаимодействие с пользователем:
вывод меню на экран;
прием команд от пользователя (выбор пиццы, подтверждение заказа, оплата и др.);

Заказ: содержит список заказанных пицц, умеет подсчитывать свою стоимость;

Пицца: содержит заявленные характеристики пиццы, 
а также умеет себя подготовить (замесить тесто, собрать ингредиенты), испечь, порезать и упаковать.

Пиццерия реализует несколько видов пиццы, которые различаются характеристиками, 
логично будет сделать общий класс Пицца, а в дочерних классах (например, классе ПиццаБарбекю) 
уточнить характеристики конкретной пиццы.



Алгоритм работы пользователя с терминалом может выглядеть следующим образом:

Терминал отображает список меню.
Терминал создает новый заказ.
Клиент вводит номер пиццы из меню.
Заказ добавляет в список выбранную пиццу.
Действия 3-4 повторяются до подтверждения или отмены.

Клиент подтверждает заказ (или отменяет).
Терминал выставляет счет, отображая информацию о заказе.
Терминал принимает оплату.
Заказ отдается на выполнение.




2. Используйте процедурное программирование:

Игра: камень, ножницы, бумага.

Алгоритм работы пользователя с терминалом может выглядеть следующим образом:

Поприветствуйте игрока и попросите ввести его.
Получить случайный компьютерный ввод.
Проверьте два друг против друга.
Спросите, хочет ли игрок снова сыграть.




3. Реализуйте следующие игры:

1. Виселица
2. Угадывание числа
3. Викторина
4. Змейка
5. Генератор MadLibs

Помните ту игру, в которую мы играли в детстве? 
Игра, в которой мы вставляли глупые слова в пробелы и истерически смеялись, когда нам их зачитывали?

С генератором Mad Libs вы можете пережить эти весёлые моменты заново.
Этот генератор позволяет вам работать над широким спектром навыков Python. 
Используемые навыки: строки, переменные, конкатенация, печать.
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
Урок от 20.03.2024
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
'''
                                                        # ЗАДАНИЕ №2
'''
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
import random

def play_rock_paper_scissors():
    choices = ["камень", "ножницы", "бумага"]
    print("Добро пожаловать в игру Камень, Ножницы, Бумага!")

    while True:
        user_choice = input("Выберите камень, ножницы или бумага (или 'выход' для завершения игры): ").lower()
        if user_choice == 'выход':
            break
        if user_choice not in choices:
            print("Неверный выбор, попробуйте снова.")
            continue

        computer_choice = random.choice(choices)
        print(f"Ваш выбор: {user_choice}. Выбор компьютера: {computer_choice}.")

        if user_choice == computer_choice:
            print("Ничья!")
        elif (user_choice == "камень" and computer_choice == "ножницы") or \
             (user_choice == "ножницы" and computer_choice == "бумага") or \
             (user_choice == "бумага" and computer_choice == "камень"):
            print("Вы выиграли!")
        else:
            print("Вы проиграли.")

        play_again = input("Хотите сыграть еще раз? (да/нет): ").lower()
        if play_again != "да":
            break

    print("Спасибо за игру!")


play_rock_paper_scissors()
"""                              # ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #                             """
'''
Как мне кажется, мой код отвечает основным требованиям задания на 100%.

Код для игры "Камень, Ножницы, Бумага" хорошо структурирован и кажется полностью соответствует заданию,
используя процедурное программирование. Он выполняет все основные требования задания:

1. Приветствует игрока: Игра начинается с приветствия.

2. Получает ввод от пользователя и случайный выбор компьютера: Вы используете input для получения выбора 
пользователя и random.choice для выбора компьютера.

3. Сравнивает вводы и определяет победителя: Ваш алгоритм корректно обрабатывает все возможные исходы игры.

4. Спрашивает пользователя о желании сыграть снова: После каждой игры предлагает пользователю 
возможность сыграть еще раз.


'''
"""                              # ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #                             """
'''
Импорты
'''
import random
'''
random: 
Модуль используется для генерации случайных чисел, в данном случае для выбора жеста компьютера из списка choices.
'''
'''
Функция play_rock_paper_scissors
'''
'''
Основная функция игры, не принимающая аргументов. Организует игровой процесс.
'''
'''
Переменные внутри функции
choices: Список с возможными вариантами выбора в игре: "камень", "ножницы", "бумага".
'''
'''
Приветствие
'''
print("Добро пожаловать в игру Камень, Ножницы, Бумага!")
'''
Эта строка выводится один раз при запуске функции, приветствуя пользователя.
'''
'''
Основной игровой цикл
'''
while True:
    ...
'''
Бесконечный цикл, который продолжается до тех пор, пока пользователь явно не решит выйти, введя 'выход'.
'''
'''
Ввод пользователя
'''
user_choice = input("Выберите камень, ножницы или бумага (или 'выход' для завершения игры): ").lower()
'''
Запрашивает у пользователя ввод и приводит его к нижнему регистру для удобства сравнения.

Условия игры

Если пользователь вводит 'выход', игра печатает прощальное сообщение и прерывает цикл через break.
Если ввод неверен (не содержится в списке choices), игра просит пользователя попробовать снова.
В противном случае выбирается случайный выбор для компьютера из списка choices с помощью random.choice(choices).
'''
'''
Сравнение выборов

Сначала проверяется ничья — если выбор пользователя совпадает с выбором компьютера.
Затем проверяются условия победы пользователя:
"камень" побеждает "ножницы",
"ножницы" побеждают "бумага",
"бумага" побеждает "камень".
Во всех остальных случаях объявляется поражение пользователя.
'''
'''
Пример игрового процесса

1. Программа приветствует пользователя.
2. Запрашивает выбор: камень, ножницы, бумага или 'выход' для завершения.
3. Сравнивает выбор пользователя с выбором компьютера, случайно выбранным из тех же вариантов.
4. Объявляет результат раунда: ничья, победа пользователя или победа компьютера.
5. Продолжается, пока пользователь не решит выйти, вводя 'выход'.
'''
'''
Запуск игры
'''
'''
Чтобы игра начала работать, нужно вызвать функцию play_rock_paper_scissors().
В коде это уже реализовано в последней строке, которая не закомментирована.

Вспоминая прошедшие задания и уроки, я подумал и вспомнил, что этот код — хороший пример (Как Вы нам говорили ранее) 
простой текстовой игры на Python, демонстрирующий использование циклов, условных операторов, ввода/вывода и работы 
со случайными числами.
'''

