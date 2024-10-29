import pandas as pd

# Código para transformar o dataset em .csv novamente
file_path = "diamonds.csv"
df = pd.read_csv(file_path)

print(df.head())