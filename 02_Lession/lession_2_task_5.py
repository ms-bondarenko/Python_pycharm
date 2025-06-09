

def mouth_to_season(n):
    if n==1: print("Зима")
    elif n==2: print("Зима")
    elif n==3: print("Весна")
    elif n==4: print("Весна")
    elif n==5: print("Весна")
    elif n==6: print("Лето")
    elif n==7: print("Лето")
    elif n==8: print("Лето")
    elif n==9: print("Осень")
    elif n==10: print("Осень")
    elif n==11: print("Осень")
    elif n==12: print("Зима")
    else: print("Некорректный номер месяца")

try:
    n = int(input("Введите номер месяца :"))
    mouth_to_season(n)
except ValueError:
    print("Введите корректное число")

