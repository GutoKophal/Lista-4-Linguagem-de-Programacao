def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

# Teste da função
numero = int(input("Digite um número para calcular o fatorial: "))
resultado = fatorial(numero)
print(f"O fatorial de {numero} é {resultado}")
