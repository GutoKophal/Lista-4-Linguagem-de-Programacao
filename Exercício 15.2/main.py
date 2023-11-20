import numpy as np

# Criando duas matrizes 3x3
matriz1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matriz2 = np.array([[10, 11, 12], [13, 14, 15], [16, 17, 18]])

# Concatenando as matrizes horizontalmente
matriz_concatenada = np.hstack((matriz1, matriz2))

print("Matriz Concatenada (3x6):")
print(matriz_concatenada)