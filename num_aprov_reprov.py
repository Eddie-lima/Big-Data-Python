import pandas as pd

data = pd.read_csv("situacaofinal2023_2.csv", skiprows=1, low_memory = False)

aprovados = data[data['situacao_nome'] == 'APROVADO'].shape[0]
reprovados = data[data['situacao_nome'] == 'REPROV P/  FALTA'].shape[0]
 
print("Número de aprovados: ", aprovados)
print("Número de reprovados por falta: ", reprovados)