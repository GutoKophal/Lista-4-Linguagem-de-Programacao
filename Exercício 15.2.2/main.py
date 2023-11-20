import numpy as np

# Criar uma matriz 10x10 com valores inteiros aleatórios entre 0 e 9
matriz = np.random.randint(0, 10, (10, 10))

print("Matriz Original:")
print(matriz)

# Copiar o conteúdo da linha 2 para a linha 4
matriz[3, :] = matriz[1, :]

# Copiar o conteúdo da coluna 1 para a coluna 8
matriz[:, 7] = matriz[:, 0]

print("\nMatriz Modificada:")
print(matriz)
