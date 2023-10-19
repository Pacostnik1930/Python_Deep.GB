input_list = [1, 2, 3, 2, 4, 3, 5, 6, 5]

output_list = list(set([x for x in input_list if input_list.count(x) > 1]))

print(output_list)

import re
from collections import Counter

text = """
Python is an interpreted high-level programming language for general-purpose programming. 
Created by Guido van Rossum and first released in 1991, Python has a design philosophy 
that emphasizes code readability, notably using significant whitespace. It provides 
constructs that enable clear programming on both small and large scales.
"""


words = re.findall('\w+', text.lower())


word_counts = Counter(words)


top_words = word_counts.most_common(10)
print(top_words)

def knapsack(items, max_weight):
    # сортируем вещи по убыванию их массы
    items = sorted(items, key=lambda x: x[1], reverse=True)
    # создаем список для хранения выбранных вещей
    selected_items = []
    # проходим по всем вещам и добавляем их в список, если они помещаются в рюкзак
    for item in items:
        if item[1] <= max_weight:
            selected_items.append(item)
            max_weight -= item[1]
    # возвращаем список выбранных вещей
    return selected_items

# пример использования функции
items = [("Книга", 1), ("Ноутбук", 3), ("Фотоаппарат", 2), ("Футболка", 1), ("Шорты", 1)]
max_weight = 5
selected_items = knapsack(items, max_weight)
print(selected_items)