import pandas as pd
import numpy as np

def calcular_desvio_padrao_ordena(arquivo_csv, coluna):
    df = pd.read_csv(arquivo_csv)

    df = df.sort_values(by=coluna)
    
    desvio_padrao = round(np.std(df[coluna], ddof=1), 2)

    print(f"O desvio padrão amostral da coluna {coluna} é: {desvio_padrao}")



arquivo = "lavouratemporaria_valordaproducao.csv"
coluna =  "Valor da produção - Abacaxi (mil reais) 2018"

calcular_desvio_padrao_ordena(arquivo, coluna)