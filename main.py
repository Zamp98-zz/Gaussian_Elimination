def anulaColunaInferior(matriz, i):
    if(matriz[i][i] != 0):
        for a in range(i+1, len(matriz)):
            linha = matriz[a]
            if(linha[i] != 0):
                coeficiente = (linha[i]/matriz[i][i])
                for b in range(len(linha)):
                    linha[b] = linha[b] - coeficiente * matriz[i][b]

def trocaLinha(matriz, i):
    matrizNova=[]
    for a in range(len(matriz)):
        matriz[i][a] = -matriz[i][a]
    for a in range(i, len(matriz)):
        if matriz[a][i] != 0:
            matrizNova.append(matriz[a])
            for b in range(len(matriz[a])):
                temp = matriz[i][b]
                matriz[i][b] = matriz[a][b]
                matriz[a][b] = temp
            break

def gauss(matriz):
    for i in range(len(matriz)):
        if matriz[i][i] != 0:
            anulaColunaInferior(matriz, i)
        else:
            trocaLinha(matriz, i)
            anulaColunaInferior(matriz, i)
    return matriz

def determinante(matriz):
    resultado = 1
    for a in range(len(matriz)):
        resultado = resultado * matriz[a][a]
    return resultado

def main():
    entrada = True
    d = 0
    while(entrada):
        d = int(input("Digite a dimensão da matriz:"))
        if (d < 5 and d > 0):
            entrada = False
        else:
            entrada = True
    matriz = []
    i = 0
    while i < d:
        print("Digite a linha ",i," da matriz:")
        linha = input().split()
        for j in range (len(linha)):
            linha[j] = int(linha[j])
        if (len(linha) == d):
            matriz.append(linha)
            i += 1
        else:
            print("Linha digitada com tamanho incorreto")
    matriz = gauss(matriz)
    for a in matriz:
        print(a)
    print("Determinante: ", round(determinante(matriz), 1))
main()