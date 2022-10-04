# Crear una matriz de 5x5 randomizada con números enteros, encontrar secuencia de 4
# números consecutivos horizontal o vertical y si se encuentra mostrar la posición inicial y
# final.

import random;

def consecutivosEnMatriz():
    #crear la matriz de 5x5 randomizada
    matriz = [[random.randint(0,9) for j in range(5)] for i in range(5)]
    #iteramos la matriz para encontrar numeros consecutivos (4)
    for i in range(5):
        for j in range(5):
            #conseguir numeros consecutivos Horizontal
            if j < 2:
                if matriz[i][j] < matriz[i][j+1] < matriz[i][j+2] < matriz[i][j+3]:
                    print("Horizontal: ", matriz[i][j], matriz[i][j+1], matriz[i][j+2], matriz[i][j+3], "Posición: ", i, j, i, j+3);
            #conseguir numeros consecutivos Vertical
            elif i < 2:
                if matriz[i][j] < matriz[i+1][j] < matriz[i+2][j] < matriz[i+3][j]:
                    print("Vertical: ", matriz[i][j], matriz[i+1][j], matriz[i+2][j], matriz[i+3][j], "Posición: ", i, j, i+3, j);
    print(matriz)                
    
consecutivosEnMatriz();
