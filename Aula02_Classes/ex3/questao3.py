def select_day() -> None:
    day = int(input('Digite o dia desejado (1 a 4): '))

    if day == 1:
        print('O dia escolhido foi Segunda-Feira!')

    elif day == 2:
        print('O dia escolhido foi Terça-Feira!')

    elif day == 3:
        print('O dia escolhido foi Quarta-Feira!')

    elif day == 4:
        print('O dia escolhido foi Quinta-Feira!')

    else:
        print('O dia escolhido é inválido!!')

select_day()