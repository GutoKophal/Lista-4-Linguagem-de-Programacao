imc = 0
def calculaIMC(peso, altura):
    global imc
    imc = peso / (altura * altura)  # Corrigido para usar a fórmula correta do IMC

calculaIMC(100, 2)
print(imc)