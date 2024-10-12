# Домашнее задание по теме "Создание функций на лету"
from random import choice

first = 'Мама мыла раму'
second = 'Рамена мало было'
result = list(map(lambda a, b: a == b, first, second))


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open('example.txt', 'a', encoding='UTF-8') as file:
            for n in data_set:
                file.write(str(n) + "\n")
    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


class MysticBall:
    def __init__(self, *word):
        self.words = word

    def __call__(self):
        word = choice(self.words)
        return word


print(result)

print

first_ball = MysticBall('Да', 'Нет', 'Наверное', 'Возможно', "Вероятно", "Врядли")
print(first_ball())
print(first_ball())
print(first_ball())
