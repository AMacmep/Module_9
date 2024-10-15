# Домашнее задание по теме "Декораторы"
def is_prime(func_summ):
    def wrapper(*args):
        result=func_summ(*args)
        #проверка на простое/составное из module_2_4
        prime = True
        for N in range(2, result):
            if result == 1:
                continue
            if result % N == 0:
                prime = False
                break
        if prime:
            print('Простое')
        else:
            print('Составное')
        return result
    return wrapper

@is_prime
def sum_three(*args):
    result = sum(args)
    return result

result = sum_three(2, 3, 6)
print(result)