# Домашнее задание по теме "Генераторы"
def all_variants(text):
    for len_text in range(len(text)):
        for first_simbol in range(len(text) - len_text):
            yield text[first_simbol:first_simbol + len_text + 1]


a = all_variants("abc")
for i in a:
    print(i)
