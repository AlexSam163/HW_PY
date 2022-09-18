# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

def not_repeat_numbers(array):
    s_array = set(array)  
    empty_array = [] 
    for num_s in s_array:
        count = 0
        for num in array:
            if num == num_s:
                count += 1
        if count == 1:
            empty_array.append(num_s)
    return empty_array

list = [1, 2, 2, 3, 89, 56, 1, 99, 13, 3]
print(f' Последовательность чисел', list)
print(f' Неповторяющиеся элементы', not_repeat_numbers(list))