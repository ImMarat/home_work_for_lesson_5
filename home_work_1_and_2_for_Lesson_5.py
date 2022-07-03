"""
1)
Написать генератор нечётных чисел от 1 до n (включительно),
используя ключевое слово yield
"""
num = int(input('Введите число:'))
def odd_nums(num):
    for num in range(1, num + 1, 2):
        yield num

for i in odd_nums(num):
    print(i)


'''
2
* (вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно),
не используя ключевое слово yield.
'''

print(*[num for num in range(1, int(input("Введите число:")) + 1, 2)])


