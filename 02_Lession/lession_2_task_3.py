import math

a=input("Введите длину стороны:")
a=a.replace(",",".")
a=float(a)
s = a * a
def square(s):
    return math.ceil(s)
result=square(s)
print("Площадь квадрата равна :", result)
