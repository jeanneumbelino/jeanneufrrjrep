print('===== QUESTÃO 11 =====')
a = int(input('Digite o primeiro lado do triangulo: '))
b = int(input('Digite o segundo lado do triangulo: '))
c = int(input('Digite o terceiro lado do triangulo: '))
if a < b + c and b < a + c and c < b + a:
    print('É possivel formar um triangulo!')
else:
    print('Não é possivel formar um triangulo.')