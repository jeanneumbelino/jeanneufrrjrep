print('===== QUESTÃO 14 =====')
mat1 = [1, 2], [6, 5]
mat2 = [6, 3], [9, 7]

def somar(mat1, mat2):
    matriz_soma = []
    quant_linhas = len(mat1)
    quant_colunas = len(mat1[0])
    for i in range(quant_linhas):
        matriz_soma.append([])
        for j in range(quant_colunas):
            soma = mat1[i][j] + mat2[i][j]
            matriz_soma[i].append(soma)
    return matriz_soma

def subtrair(mat1, mat2):
    matriz_subtraçao = []
    quant_linhas = len(mat1)
    quant_colunas = len(mat1[0])
    for i in range(quant_linhas):
        matriz_subtraçao.append([])
        for j in range(quant_colunas):
            soma = mat1[i][j] - mat2[i][j]
            matriz_subtraçao[i].append(soma)
    return matriz_subtraçao

def getLinha(matriz, n):
    return [i for i in matriz[n]]

def getColuna(matriz, n):
    return [i[n] for i in matriz]

mat1lin = len(mat1)
mat1col = len(mat1[0])

mat2lin = len(mat2)
mat2col = len(mat1[0])

matRes = []
for i in range(mat1lin):
    matRes.append([])
    for j in range(mat2col):
        listMult = [x*y for x, y in zip(getLinha(mat1, i), getColuna(mat2, j))]
        matRes[i].append(sum(listMult))
print('='*10, 'MULTIPLICAÇÃO', '='*10)
print(matRes)
print('='*10, 'SOMA', '='*19)
print(somar(mat1, mat2))
print('='*10, 'SUBTRAÇÃO', '='*14)
print(subtrair(mat1, mat2))
print('='*20)
