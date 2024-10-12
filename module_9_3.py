# Домашнее задание по теме "Создание потоков".
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
first_result = (len(a) - len(b) for a, b in zip(first, second) if len(a) != len(b))

second_result = (len(first[n]) == len(second[n]) for n in range(len(first)))

print(list(first_result))
print(list(second_result))
