def process_divider():
    while True:
        try:
            divider = int(input('Digite o valordo divisor: '))
            print( 1 / divider )
            return
            
        except:
            print('ERROR: Invalid Number')
            print('Digite um número válido.')
            print('Prazer, me chamo João Victor.\n')

process_divider()