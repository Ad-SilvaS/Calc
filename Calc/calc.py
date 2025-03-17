results = []

def menu():
    print('\nOperações')
    print('1 - Soma')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')

def soma(a, b):
    return a+b

def sub(a, b):
    return a-b

def mult(a, b):
    return a*b

def div(a, b):
    return a/b

def num(message):
    while True:
        try:
            num = input(message).strip()
            if num == '':
                print("\nPor favor, insira um número válido!")
                continue
            return float(num)
        except ValueError:
            print("Por favor, digite um número válido!")

while True:
    menu()
    while True:
        op = input('\nSelecione a operação desejada: ').lower().strip()
        if op not in ['1', 'soma', '2', 'subtração', '3', 'multiplicação', '4', 'divisão']:
            print('\nSelecione uma operação válida!')
            continue
        else:
            break
    
    num1 = num('\nDigite o primeiro número: ')
    num2 = num('\nDigite o segundo número: ')

    if op == '1' or op == 'soma':
        result = soma(num1, num2)
    elif op == '2' or op == 'subtração':
        result = sub(num1, num2)
    elif op == '3' or op == 'multiplicação':
        result = mult(num1, num2)
    elif op == '4' or op == 'divisão':
        if num2 == 0:
            print('\nNão é possível dividir por ZERO!')
            continue
        else:
            result = div(num1, num2)
    if result == int(result):
        result = int(result)
    else:
        result = round(result, 2)
        
    results.append(result)

    print(f'\nResultado: {result}')

    while True:
        cont = input('\nDeseja realizar outra operação: (S/N) ').lower().strip()
        if cont == 'n':
            print(f'\nResultados salvos: {results}')
            exit()
        elif cont == 's':
            break
        else:
            print('\nDigite "s" para realiar outra operação ou "n" para sair!')
