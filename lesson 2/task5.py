'''5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. 
У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы
 с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].'''
def rating(x):
    pass
a = [7, 5, 3, 3, 2, 1]
a.sort(reverse = True)
print(a)
# x = int(input())
# print(rating(x))

# if __name__ == '__main__':
#     print("Example:")
#     print(rating([4, 6, 2, 2, 6, 4, 4, 4]))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert list(rating([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
#     assert list(rating(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
#     assert list(rating([17, 99, 42])) == [17, 99, 42]
#     assert list(rating([])) == []
#     assert list(rating([1])) == [1]
#     print("Coding complete!")