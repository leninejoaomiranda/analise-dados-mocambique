# Análise de Indicadores Económicos de Moçambique

Projecto em Python que descarrega dados económicos públicos de Moçambique e calcula estatísticas descritivas básicas.

## O que o projecto faz

- Obtém dados directamente da API do Banco Mundial, sem ficheiros manuais.
- Analisa três indicadores:
  - Crescimento do PIB (% ao ano)
  - Inflação (% ao ano)
  - Taxa de câmbio (meticais por dólar)
- Mostra os últimos 10 anos de cada indicador.
- Calcula a média e o desvio padrão de cada série.

## Como executar

```bash
pip install requests
python analise_economia.py
```

## Fonte dos dados

Banco Mundial, World Development Indicators (https://data.worldbank.org).

## Observações da análise

- O PIB teve queda em 2020 (-1,22%), no contexto da pandemia.
- A inflação esteve acima de 15% em 2016 e 2017, desceu para menos de 4% em 2018 e 2019, e voltou a subir em 2022 (10,28%).
- O câmbio passou de cerca de 40 para 63 MZN/USD entre 2015 e 2016 e manteve-se relativamente estável desde então.
- Cada série tem um número diferente de anos (n), por isso as médias cobrem períodos distintos.
- A média do câmbio sobre toda a série histórica não é representativa, porque inclui o período anterior à redenominação do metical. Uma melhoria prevista é calcular as estatísticas apenas a partir de 2010.

## Próximos passos

- Restringir as estatísticas ao período desde 2010.
- Adicionar gráficos com matplotlib.
- Calcular a correlação entre inflação e câmbio.

## Autor

Lenine João Miranda
Licenciado em Matemática (Estatística) | Análise de dados com Python | Moçambique