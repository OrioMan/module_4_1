from true_math import true_divide as td


def fake_divide(first, second):
    if second == 0:
        return 'Ошибка'
    else:
        return first / second


result1 = fake_divide(69, 3)
result2 = fake_divide(3, 0)
print(result1)
print(result2)
print(td(49, 7))
print(td(15, 0))
