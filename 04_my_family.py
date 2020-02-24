#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = []
my_family.append('мама')
my_family.append('папа')
my_family.append('дочь')

# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    ['мама', 170],
    ['папа', 180],
    ['дочь', 130]
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
print('Heigt father - '+ str(my_family_height[1][1]))

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см

height_general = 0
for number in my_family_height:
    height_general = height_general + number[1]

print(height_general)