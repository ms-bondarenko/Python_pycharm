# print("Кратно ли число трем")
#num = input("Введите число :")
#num = int(num)
#if (num % 3 == 0):
    #print("Да")
#else:
 #   print("Нет")
#print("Завершено")

def dev_by_three(num):
    return "Нет" if num % 3 != 0 else "Да"
num = input("Ведите число : ")
num = int(num)
result = dev_by_three(num)
print("Делится ли число на три:" , result)
