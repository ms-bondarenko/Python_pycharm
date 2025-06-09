rate_as_string= input("Оцените работу оператора от 1 до 5:")
rate = int(rate_as_string)

if (rate <1):
    rate=1
if (rate > 5):
    rate = 5
print(rate)

feedback = ''

if (rate ==1):
    feedback = input("Расскажите что нам улучшить")
elif rate == 2:
    feedback = input("Расскажите что вам не понравилось")
elif rate == 3:
    feedback = input("Расскажите как нам стать суперменами")
elif rate == 4:
    feedback = input("Расскажите почему не 5")
else: feedback = input("Расскажите чем отблагодарить шефа")

print(feedback)