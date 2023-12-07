def sum(a, b):
    return a + b

def processar_numeros(first_num, second_num, callback):
    return callback(first_num, second_num)

print(processar_numeros(5, 7, sum))