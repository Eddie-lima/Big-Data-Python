import pandas as pd

def processar_csv_por_nome_coluna(arquivo_csv, nome_coluna):

    df = pd.read_csv(arquivo_csv)

    df = df.sort_values(by=nome_coluna)

    contagem_valores = df[nome_coluna].value_counts()

    moda = contagem_valores.idxmax()

    print(f"A moda da coluna {nome_coluna} é: {moda}")

arquivo = "lavouratemporaria_valordaproducao.csv"
coluna_ordernar =  "Valor da produção - Abacaxi (mil reais) 2012"

processar_csv_por_nome_coluna(arquivo, coluna_ordernar)