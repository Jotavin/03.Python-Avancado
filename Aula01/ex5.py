def sqrt(n):
    return n**1/2

def inverso(n):
    return 1/n

def executar_operacao(num, func): 
    resultado = func(num)
    print(resultado)

executar_operacao(5, sqrt)
executar_operacao(5, inverso)