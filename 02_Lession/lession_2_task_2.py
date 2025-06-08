def is_year_leap(y):
    return "False" if y % 4 != 0 else "True"

y=int(input("Введите пожалуйста год:"))
result= is_year_leap(y)
print("Год :", y , result)