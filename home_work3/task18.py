# Требуется найти в массиве A[0..N-1] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел A[i]. 
# Последняя строка содержит число X
N = int(input())
lst = map(int, (input().split()))
x = int(input())
print(min(lst, key=lambda a:abs(a-x)))
