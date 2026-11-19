import requests

indicadores = {
    "PIB crescimento (%)": "NY.GDP.MKTP.KD.ZG",
    "Inflacao (%)": "FP.CPI.TOTL.ZG",
    "Cambio (MZN/USD)": "PA.NUS.FCRF",
}

def baixar(codigo):
    url = f"https://api.worldbank.org/v2/country/MZ/indicator/{codigo}"
    r = requests.get(url, params={"format": "json", "per_page": 100}, timeout=30)
    dados = r.json()[1]
    return {int(d["date"]): d["value"] for d in dados if d["value"] is not None}

series = {nome: baixar(cod) for nome, cod in indicadores.items()}

# Mostra os últimos 10 anos de cada indicador
for nome, serie in series.items():
    print("\n" + nome)
    for ano in sorted(serie)[-10:]:
        print(ano, round(serie[ano], 2))

# Estatísticas simples
def media(v): return sum(v) / len(v)
def desvio(v):
    m = media(v)
    return (sum((x - m) ** 2 for x in v) / (len(v) - 1)) ** 0.5

print("\n--- Estatísticas (todos os anos disponíveis) ---")
for nome, serie in series.items():
    v = list(serie.values())
    print(f"{nome}: média={media(v):.2f}  desvio={desvio(v):.2f}  n={len(v)}")