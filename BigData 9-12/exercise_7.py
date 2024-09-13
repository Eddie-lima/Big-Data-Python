import pandas as pd
import numpy as np

df = pd.read_csv('lavouratemporaria_valordaproducao.csv')    

coluna_ordernar = df["Valor da produção - Algodão herbáceo (em caroço) (mil reais) 2013"]

coluna_ordenada = coluna_ordernar.sort_values()

q1 = np.percentile(coluna_ordenada, 25)
q2 = np.percentile(coluna_ordenada, 50)
q3 = np.percentile(coluna_ordenada, 75)
    
print("Q1: ", q1)
print("Q2: ", q2)
print("Q3: ", q3)

