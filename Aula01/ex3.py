contador = 0

def incrementar_contador():
    aux = contador
    aux += 1
    return aux
print(incrementar_contador())

# def incrementar_contador():
#     global contador
#     contador += 1
#     return contador
# print(incrementar_contador())
print(contador)