import pandas as pd

def calculo_porcent_situacao_falta(arquivo_csv, escola_especifica):
    
    df = pd.read_csv(arquivo_csv, skiprows = 1, low_memory = False)

    escola_selecionada = df[df['escola'] == escola_especifica]

    reprovados_por_falta = escola_selecionada[escola_selecionada['situacao_nome'] == 'REPROV P/  FALTA']

    aprovados = escola_selecionada[escola_selecionada['situacao_nome'] == 'APROVADO']

    total_alunos = len(escola_selecionada)
    total_aprovados = len(aprovados)
    total_reprovados_por_falta = len(reprovados_por_falta)

    #Cálculo de porcentagens

    porcentagem_reprovados = (total_reprovados_por_falta / total_alunos) * 100
    porcentagem_aprovados = (total_aprovados / total_alunos) * 100

    resultados = pd.DataFrame({'Situação': ['Aprovado', 'Reprovado por falta'],'Porcentagem %': [porcentagem_aprovados, porcentagem_reprovados]})
    
    return resultados

arquivo_csv = 'teste.csv'
escola = 'ESCOLA COMUNITARIA TOM E JERRY'
resultado = calculo_porcent_situacao_falta(arquivo_csv, escola)

print(resultado)