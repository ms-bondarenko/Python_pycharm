i=int(input("Введите число:"))
def fizz_buzz(i):
    for i in range(1,i +1):
        if i % 5 == 0 and i % 3 == 0:
            print(f"{i}-Fizz_Buzz")
        elif i % 5 == 0:
            print(f"{i}-Buzz")
        elif i % 3 == 0:
            print(f"{i}-Fizz")
        else:
            print(i)
fizz_buzz(i)