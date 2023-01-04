#Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

number = input('введите числа через пробел ')

list_number = number.split(' ')

print(list_number)

result_array = []

for i in list_number:

    if i not in result_array:

        result_array.append(i)

print(result_array)


