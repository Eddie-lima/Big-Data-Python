import pandas as pd

def processar_csv_por_nome_coluna(arquivo_csv, nome_coluna):

    df = pd.read_csv(arquivo_csv)

    df[nome_coluna] = pd.to_numeric(df[nome_coluna], errors='coerce')

    df = df.sort_values(by=nome_coluna)

    amplitude = df[nome_coluna].max() - df[nome_coluna].min()

    print(f"A amplitude da coluna {nome_coluna} é: {amplitude}")

arquivo = "lavouratemporaria_valordaproducao.csv"
coluna_ordernar =  "Valor da produção - Abacaxi (mil reais) 2010"

processar_csv_por_nome_coluna(arquivo, coluna_ordernar)