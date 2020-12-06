print('===== QUESTÃO 14 =====')
a1 = int(input('Digite a medida do angulo: '))
a2 = int(input('Digite a medida do angulo: '))
a3 = int(input('Digite a medida do angulo: '))
if a1 == 90 or a2 == 90 or a3 == 90:
    print('O triangulo é Retangulo')
if a1 > 90 or a2 > 90 or a3 > 90:
    print('O triangulo é Obtusangulo')
if a1 < 90 and a2 < 90 and a3 < 90:
    print('O triangulo é Acutangulo')