#1:  Даны два произвольные списка.
# Удалите из первого списка элементы присутствующие во втором списке.
#Примечание. Списки создайте вручную, например так:

#my_list_1 = {2, 5, 8, 2, 12, 12, 4}
#my_list_2 = {2, 7, 12, 3}
#print(my_list_1 & my_list_2)

# = [1, 1, 1, 2,2,2,3,4]
#b = [2,4,5]
#for number in a[:]:
#    if number in b:
#        a.remove(number)
#print(a)

#2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача — вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

#date = '02.11.2013'
#d, m, y = date.split('.')
#print(d,m,y)
#month = {
#    '01': 'января',
#    '11': 'ноября'
#}
#days = {
#    '01': 'первое',
#    '02': 'второе'
#}
#result = f'{days[d]} {month[m]} {y} года.'
#print(result)

#3: Дан список заполненный произвольными целыми числами.
#Получите новый список, элементами которого будут только уникальные элементы исходного.
#    Примечание. Списки создайте вручную, например так:
#my_list_1 = [2, 2, 5, 12, 8, 2, 12]
#В этом случае ответ будет:
#[5, 8]

#my_list_1 = [2, 2, 5, 12, 8, 2, 12]
#my_list_2 = []
#my_list_1.remove(2)
#print(my_list_1)
#my_list_1.remove(2)
#my_list_1.remove(12)
#my_list_1.remove(2)
#my_list_1.remove(12)
#print(my_list_1)

numbers = [1,1,2,3,3,4,4,4,5,1,2,7]
result = []
for number in numbers:
    if numbers.count(number) ==1:
        result.append(number)
print(result)