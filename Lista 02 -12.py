print('===== QUESTÃO 12 =====')
s1 = str(input('Digite uma palavra: '))
s2 = str(input('Digite uma palavra do mesmo tamanho: '))

def Anagrama(s1, s2):
    umalista1 = list(s1)
    umalista2 = list(s2)

    umalista1.sort()
    umalista2.sort()

    pos = 0
    formam = True

    while pos < len(s1) and formam:
        if umalista1[pos] == umalista2[pos]:
            pos = pos + 1
        else:
            formam = False

    return formam

print('FORMAM UM ANAGRAMA?')
print(Anagrama(s1, s2))