import pandas as pd

def processar_csv_por_nome_coluna(arquivo_csv, nome_coluna):

    df = pd.read_csv(arquivo_csv)

    df = df.sort_values(by=nome_coluna)

    mediana = df[nome_coluna].median()

    print(f"Média da coluna {nome_coluna} é: {mediana}")

arquivo = "lavouratemporaria_valordaproducao.csv"
coluna_ordernar =  "Valor da produção - Abacaxi (mil reais) 2014"

processar_csv_por_nome_coluna(arquivo, coluna_ordernar)