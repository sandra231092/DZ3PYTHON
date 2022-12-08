#Реализуйте алгоритм перемешивания списка.

import random
list = ["Саша", "Маша", 67, 90]
for i in range(len(list)):
    index_a = random.randint(0, len(list) - 1)
    list[i],list[index_a] = list[index_a],list[i]
print(list)