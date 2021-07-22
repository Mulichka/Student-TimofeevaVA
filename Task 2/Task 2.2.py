#Сформировать из обработанного списка строку: в "05" часов "17" минут температура воздуха была "+05" градусов


list_1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
list_2 = []
get_in = '5'
for i in list_1:
    if get_in in i:
        list_2.append(i.replace('5', '05'))
    else:
        list_2.append(i)

for i, el in enumerate(list_1):
if el.isdigit() == True and int(el) // 10 == 0:
            a = str(el)
            a = el.zfill(2)
            list_2.append(a)
        else:
            list_2.append(el)

list_2 = ' '.join(list_2)
print(list_2)


# list_2 = []
#     [x for x,y in enumerate(list_1) if "5" in y]
       # x = x.zfill(2)



#
#
# print(list_2)
# list_2 = ' '.join(list_2)
#
# print(list_2)

#print(f{"  "})