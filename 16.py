print('==== QUESTÃO 16 =====')
from math import ceil
c = float(input('Digite o comprimento da cozinha: '))
l = float(input('Digite a largura da cozinha: '))
h = float(input('Digite a altura da cozinha: '))
a = (2*(c * h) + 2*(l * h)) / 1.52
print('Você precisará de {} azulejos'.format(ceil(a)))

