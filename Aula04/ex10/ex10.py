list = [10, 20, 30, -5, 40, 50]

def error_function(list):
    for i in list:
        if i < 0:
            raise ValueError("Número negativo encontrado!")
        yield i

try:
    for item in error_function(list):
        print(item)
except ValueError as e:
    print(f"Exceção capturada: {e}")


'''
    No exemplo a função retorna (com o "yield") os números de uma lista (parâmetro list), que se o item dessa lista for negativo, um erro é chamado.
'''