print('==== QUESTÃO 08 =====')
c = float(input('Digite a temperatura em °C: '))
f = ((c * 9) / 5) + 32
k = c + 273
print('A temperatura {}°C convertida para °F é igual a {:.1f}°F e para °K é igual a {:.1f}°K'.format(c, f, k))
