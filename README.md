# Análise de Indicadores Económicos de Moçambique

Projecto em Python que descarrega dados económicos públicos de Moçambique e calcula estatísticas descritivas básicas.

## O que o projecto faz

- Obtém dados directamente da API do Banco Mundial, sem ficheiros manuais.
- Analisa três indicadores: crescimento do PIB, inflação e taxa de câmbio (MZN por USD).
- Mostra os últimos 10 anos de cada indicador.
- Calcula a média e o desvio padrão de cada série, a partir de 2010.

## Como executar

```bash
pip install requests
python analise_economia.py
```

## Fonte dos dados

Banco Mundial, World Development Indicators (https://data.worldbank.org).

## Resultados (2010 em diante)

| Indicador | Média | Desvio padrão | Anos (n) |
|---|---|---|---|
| Crescimento do PIB (%) | 4,33 | 2,88 | 16 |
| Inflação (%) | 6,97 | 4,80 | 16 |
| Câmbio (MZN/USD) | 51,26 | 16,47 | 15 |

## Observações da análise

- O PIB teve queda em 2020 (-1,22%), no contexto da pandemia, e voltou a ficar negativo em 2025 (-0,52%).
- A inflação esteve acima de 15% em 2016 e 2017, desceu para menos de 4% em 2018 e 2019, e voltou a subir em 2022 (10,28%).
- O câmbio passou de cerca de 40 para 63 MZN/USD entre 2015 e 2016 e manteve-se relativamente estável desde então.
- A média do câmbio (51,26) e o desvio (16,47) são afectados pelos anos anteriores a 2016, quando a taxa era bem mais baixa. Para descrever o período estável, o corte mais adequado seria de 2016 em diante.
- Uma primeira versão calculava as estatísticas sobre toda a série histórica, o que dava resultados distorcidos (por exemplo, média do câmbio de 16,53). Por isso o período foi restringido.

## Próximos passos

- Calcular as estatísticas do câmbio apenas a partir de 2016.
- Adicionar gráficos com matplotlib.
- Calcular a correlação entre inflação e câmbio.

## Autor

Lenine João Miranda

Licenciado em Matemática (Estatística) 