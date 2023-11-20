# Dicionário expandido com países e suas capitais
capitais = {
    "Brasil": "Brasília",
    "Estados Unidos": "Washington, D.C.",
    "França": "Paris",
    "Japão": "Tóquio",
    "Reino Unido": "Londres",
    "Alemanha": "Berlim",
    "Índia": "Nova Delhi",
    "Rússia": "Moscou",
    "Canadá": "Ottawa",
    "Austrália": "Camberra",
    "Itália": "Roma",
    "Espanha": "Madri",
    "China": "Pequim",
    "México": "Cidade do México"
}

# Perguntar ao usuário o nome do país
pais = input("Digite o nome de um país para saber sua capital: ").strip()

# Buscar a capital no dicionário
capital = capitais.get(pais)

# Exibir a capital ou uma mensagem de erro
if capital:
    print(f"A capital do {pais} é {capital}.")
else:
    print(f"Desculpe, o país '{pais}' não está no nosso dicionário.")
