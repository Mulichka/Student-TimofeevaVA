#Известно, что имя сотрудника всегда в конце строки. Сформировать из этих имён и вывести на экран фразы вида:
# 'Привет, Игорь!' Подумать, как получить имена сотрудников из элементов списка, как привести их к корректному виду.
# Можно ли при этом не создавать новый список?

list1 = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
list2 = []

for i in list1:
   n = i.split(' ')
   n = n[len(n)-1].title()
   list2.append('Привет! ' + n)
print(list2)