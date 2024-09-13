import pandas as pd
import numpy as np

def calcular_variancia_ordenar(arquivo_csv, coluna):

    df = pd.read_csv(arquivo_csv)

    df = df.sort_values(by=coluna)

    variancia = round(np.var(df[coluna], ddof=1), 2)

    print(f"A variância amostral da coluna {coluna} é: {variancia}")

arquivo = "lavouratemporaria_valordaproducao.csv"
coluna_ordernar =  "Valor da produção - Abacaxi (mil reais) 2018"

calcular_variancia_ordenar(arquivo, coluna_ordernar)