import math

def raiz_e_quadrado(numero):
    raiz_quadrada = math.sqrt(numero)
    quadrado = numero ** 2
    return raiz_quadrada, quadrado

# Testando a função
numero = 4
raiz, quad = raiz_e_quadrado(numero)
print(f"A raiz quadrada de {numero} é {raiz} e o quadrado é {quad}.")
