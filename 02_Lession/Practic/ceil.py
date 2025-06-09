import math
def min_boxes(items):
    return math.ceil(items/5)
items = input("Введите количество штук :")
items = int(items)
result = min_boxes(items)
print("Минимальное количество коробок :",result)
