print('===== QUESTÃO 13 =====')

def getLinha(matriz, n):
    return [i for i in matriz[n]]

def getColuna(matriz, n):
    return [i[n] for i in matriz]

mat1 = [[2, 3, 7], [4, 6, 8], [8, 5, 2]]
mat1lin = len(mat1)
mat1col = len(mat1[0])

mat2 = [[1, 3, 0], [2, 1, 1], [9, 6, 1]]
mat2lin = len(mat2)
mat2col = len(mat1[0])

matRes = []
for i in range(mat1lin):
    matRes.append([])

    for j in range(mat2col):
        listMult = [x*y for x, y in zip(getLinha(mat1, i), getColuna(mat2, j))]
        matRes[i].append(sum(listMult))

print(matRes)
