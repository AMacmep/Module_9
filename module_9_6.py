# Домашнее задание по теме "Генераторы"
def all_variants(text):
    for len_text in range(len(text)):
        for first_simbol in range(len(text) - len_text):
            # text_result = text[first_simbol:first_simbol + len_text + 1]
            # print(text_result)
            yield text[first_simbol:first_simbol + len_text + 1]


a = all_variants("abc")
for i in a:
    print(i)

test_text = all_variants('123456')
print(all_variants(test_text))
for n in test_text:
    print(n)
