import os
from collections import Counter
import re
import matplotlib.pyplot as plt

# Путь к файлу с текстом
file_path = "PIoIBaK.txt"


# Функция для чтения файла и возврата его содержимого
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


# Функция для анализа текста и вывода топ 5 слов
def analyze_text(text):
    # Приведем текст к нижнему регистру и разобьем его на слова
    words = re.findall(r'\b\w+\b', text.lower())
    # Подсчитаем количество упоминаний каждого слова
    word_counts = Counter(words)
    # Выведем топ 5 наиболее популярных слов
    top_words = word_counts.most_common(5)
    print(top_words)

    # Создаем списки для слов и их частот
    words = [word[0] for word in top_words]
    counts = [word[1] for word in top_words]

    # Строим график
    plt.figure(figsize=(10, 6))
    plt.bar(words, counts, color='skyblue')
    plt.title('Top 5 Words in the Text')
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Показываем график
    plt.show()


# Чтение файла и анализ текста
if os.path.exists(file_path):
    text = read_file(file_path)
    analyze_text(text)
else:
    print("Файл не найден.")
