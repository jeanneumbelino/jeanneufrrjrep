print('===== QUESTÃO 10 =====')
n = int(input('Digite um numero: '))
if n <= 10:
    if n == 1 or n == 2 or n == 3 or n == 5 or n == 7:
        print('Esse numero é primo!')
    else:
        print('Esse numero não é primo.')
else:
    print('Numero maior que 10 :(')