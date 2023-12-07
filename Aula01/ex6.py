def isTrue():
    print('Identiadade verdadeira. Operação realizada com sucesso!')

def isFalse():
    print('Identidade falsa. Operação bloqueada!')

def avaliar_condicao(num, callback_true, callback_false):
    if bool(num):
        callback_true()
    else:
        callback_false()

avaliar_condicao(0, isTrue, isFalse)