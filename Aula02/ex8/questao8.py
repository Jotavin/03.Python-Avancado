dados = [1, "dois", 3.0, [4, 5, 6]]

for item in dados:
    if isinstance(item, int):
        print(f"Inteiro encontrado: {item}")

    elif isinstance(item, str):
        print(f"String encontrada: {item}")

    elif isinstance(item, float):
        print(f"Float encontrado: {item}")

    elif isinstance(item, list):
        print(f"Lista encontrada: {item}")

    else:
        print("Tipo de dado não identificado")







