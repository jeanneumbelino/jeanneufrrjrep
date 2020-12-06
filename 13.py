print('===== QUESTÃO 13 =====')
a = int(input('Digite o primeiro lado do triangulo: '))
b = int(input('Digite o segundo lado do triangulo: '))
c = int(input('Digite o terceiro lado do triangulo: '))
if a < b + c and b < a + c and c < b + a:
    if a == b == c:
        print('Esse é um triangulo equilatero')
    if a == b or a == c or b == c:
        print('Esse triangulo é isosceles')
    else:
        print('Esse triangulo é escaleno')
else:
    print('Não é possivel formar um triangulo')