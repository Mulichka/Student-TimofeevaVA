#	*(вместо задачи 2) Решить задачу 2 не создавая новый список (как говорят, in place). Эта задача намного серьёзнее, чем может сначала показаться.

list_1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

c = 0
for i in list_1:
    # if i.isdigit():
    if i.isnumeric():
        if int(i) // 10 > 0:
            list_1[c] = '"' + list_1[c] + '"'
        else:
            list_1[c] = '"' + '0' + list_1[c] + '"'
    else:
        (i.find('+') >= 0)
        list_1[c] = list_1[c].replace('+5', '"+05"')
    c += 1
print(list_1)
sentence = " ".join(list_1)
print(sentence)
