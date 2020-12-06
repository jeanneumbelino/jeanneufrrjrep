print('==== QUESTÃO 15 =====')
from math import ceil
p = int(input('Digite a potencia da lampada: '))
c = float(input('Digite o comprimento do cômodo: '))
l = float(input('Digite a largura do cômodo: '))
lampada = ((c * l) * 18) / p
print('Você precisara de {} lampadas para esse comodo.'.format(ceil(lampada)))
