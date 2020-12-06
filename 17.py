print('==== QUESTÃO 17 =====')
kmi = int(input('Digite a quilometragem inicial: '))
kmf = int(input('Digite a quilometragem final: '))
comb = int(input('Digite quantos litros de combustivel foram gastos: '))
din = float(input('Digite o valor arrecadado no dia: '))
medcomb = (kmf - kmi)/comb
print('A média de consumo de combustivel é de {:.1f}Km/L'.format(medcomb))
print('O lucro do dia foi R${:.2f}'.format(din - (comb * 1.90)))