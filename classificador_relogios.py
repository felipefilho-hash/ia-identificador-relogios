from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

relogios = [
    ("Casio", "F-91W-1", [35.2, 8.5, 1, 0]),
    ("Casio", "G-Shock DW-5600UE-1", [42.8, 13.4, 1, 0]),
    ("Seiko", "5 Sports SRPD55", [42.5, 13.4, 0, 1]),
    ("Orient", "Bambino RA-AC0M03S", [38.4, 12.5, 0, 1])
]

X = [relogio[2] for relogio in relogios]
y = list(range(len(relogios)))

normalizador = StandardScaler()
X_normalizado = normalizador.fit_transform(X)

modelo = KNeighborsClassifier(n_neighbors=1)
modelo.fit(X_normalizado, y)

print("=== IDENTIFICADOR DE RELÓGIOS COM IA ===")

try:
    largura = float(input("Largura da caixa (mm): ").replace(",", "."))
    espessura = float(input("Espessura da caixa (mm): ").replace(",", "."))
    digital = int(input("É digital? (1=Sim, 0=Não): "))
    aco = int(input("Caixa de aço? (1=Sim, 0=Não): "))

    if largura <= 0 or espessura <= 0:
        raise ValueError

    if digital not in (0, 1) or aco not in (0, 1):
        raise ValueError

    dados = [[largura, espessura, digital, aco]]
    dados_normalizados = normalizador.transform(dados)

    indice = modelo.predict(dados_normalizados)[0]
    marca, nome, _ = relogios[indice]

    print("\n=== RESULTADO DA IA ===")
    print(f"Marca: {marca}")
    print(f"Modelo mais semelhante: {nome}")
    print("Comparação feita com 4 modelos cadastrados.")

except ValueError:
    print("Dados inválidos. Execute novamente.")
