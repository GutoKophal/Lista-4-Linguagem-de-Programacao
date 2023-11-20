import numpy as np

# Define o tamanho da matriz
n = 8

# Cria uma matriz 8x8 com valores inteiros aleatórios entre 0 e 9
matrix = np.random.randint(10, size=(n, n))

print("Matriz Inicial:")
print(matrix)

# Copia o conteúdo do quadrante superior esquerdo (4x4) para o quadrante inferior direito
matrix[n//2:, n//2:] = matrix[:n//2, :n//2]

print("\nMatriz Modificada:")
print(matrix)
