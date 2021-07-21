second_now = int(input("Введите число:"))

if second_now < 60:
    print(second_now, ' секунд')
elif second_now < 3600:
    minut = second_now // 60
    second = second_now % 60
    print(minut, 'минут', second, 'секунд')
elif second_now < 86400:
    hours = second_now // 3600
    minut = second_now % 3600 // 60
    second = second_now % 60
    print(hours, 'часов', minut, 'минут', second, 'секунд')
else:
    days = second_now // 86400
    hours = second_now % 86400 // 3600
    minut = second_now % 3600 // 60
    second = second_now % 60
    print(days, 'дней', hours, 'часов', minut, 'минут', second, 'секунд')