def type_data(datum):
    if isinstance(datum, str):
        return datum.title()

    elif isinstance(datum, int):
        return datum ** 0.5

    elif isinstance(datum, list):
        return sum(datum)

    else:
        return "Tipo de dado não suportado"



first = type_data("python is awesome")
second = type_data([1, 2, 3, 4, 5])
third = type_data(4478)
fourth = type_data({'python': 'programming language', 'html': 'mark language'})

print(first)
print(second)
print(third)
print(fourth)