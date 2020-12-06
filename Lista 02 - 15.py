print('===== QUESTÃO 15 =====')
n1 = int(input('Digite o inicio: '))
n2 = int(input('Digite o final: '))


def obter_divisores(n):
    lista_divisores = list()
    for i in range(1, n + 1):
        if (n % i == 0):
            lista_divisores.append(i)
    return lista_divisores


def eh_numero_perfeito(n):
    divisores = obter_divisores(n)
    soma_divisor = 0
    for divisor in divisores:
        if (divisor < n):
            soma_divisor += divisor
    return (soma_divisor == n)


def obter_numeros_perfeitos(n1, n2):
    lista_numeros_perfeitos = list()
    for k in range(n1, n2 + 1):
        if (eh_numero_perfeito(k)):
            lista_numeros_perfeitos.append(k)
    return lista_numeros_perfeitos


print(obter_numeros_perfeitos(n1, n2))