#1.	Создать список, состоящий из кубов нечётных чисел от 1 до 1000:

create_list = list(range(1, 1000))
cube_list = []
for i in range(len(create_list)):
    if create_list[i] % 2 != 0:
        cube_list.append(create_list[i] ** 3)
print(cube_list)

#2.	Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
#Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. Внимание: использовать только арифметические операции!

# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
all_summ = 0
seven_list = []
for i in cube_list:
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

new_list = []
for i in range(len(cube_list)):
    new_list.append(cube_list[i] + 17)
print(new_list)

all_summ_2 = 0
seven_list_2 = []
for i in new_list:
    post = i
    num_summ_2 = 0
    while i > 0:
        num_summ_2 += i % 10
        i = i // 10
    if num_summ_2 % 7 == 0:
        seven_list_2.append(post)
        all_summ_2 += post

print(all_summ_2)
print(seven_list_2)