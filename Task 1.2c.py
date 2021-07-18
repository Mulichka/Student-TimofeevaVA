#1.	Создать список, состоящий из кубов нечётных чисел от 1 до 1000:

create_list = list(range(1, 1000))
cube_list = []
for i in range(len(create_list)):
    if create_list[i] % 2 != 0:
        cube_list.append(create_list[i] ** 3)
print(cube_list)

#2.	Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
#Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. Внимание: использовать только арифметические операции!
#c.	* Решить задачу под пунктом b, не создавая новый список.

all_summ = 0
seven_list = []
for i in cube_list:
    i = i + 17
    post = i
    num_summ = 0
    while i > 0:
        num_summ += i % 10
        i = i // 10
    if num_summ % 7 == 0:
        seven_list.append(post)
        all_summ += post

print(all_summ)
print(seven_list)