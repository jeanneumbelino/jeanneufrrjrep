print('===== QUESTÃO 09 =====')
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
if n1 == n2:
    print('Os numeros sao iguais!')
else:
    print('O maoir numero é {}'.format(max(n1,n2)))