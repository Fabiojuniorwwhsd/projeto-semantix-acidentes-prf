import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Ajuste os caminhos abaixo
CAMINHO_PRF = "data/acidentes_prf.csv"
CAMINHO_POP = "data/populacao_ibge.xlsx"

# 1. Leitura
df = pd.read_csv(CAMINHO_PRF, sep=';', encoding='utf-8', low_memory=False)

# 2. Padronização inicial
df.columns = [c.strip().lower() for c in df.columns]

# 3. Exemplos de limpeza
for col in ['uf', 'municipio', 'tipo_acidente', 'causa_acidente']:
    if col in df.columns:
        df[col] = df[col].astype(str).str.strip()

# 4. Tratamento de datas
if 'data_inversa' in df.columns:
    df['data_inversa'] = pd.to_datetime(df['data_inversa'], errors='coerce')
    df['ano'] = df['data_inversa'].dt.year
    df['mes'] = df['data_inversa'].dt.month

# 5. Variável alvo sugerida
if 'classificacao_acidente' in df.columns:
    severas = {'Com Vítimas Fatais', 'Com Vítimas Feridas'}
    df['acidente_severo'] = df['classificacao_acidente'].isin(severas).astype(int)

# 6. Estatísticas básicas
print("Linhas:", len(df))
print("Colunas:", len(df.columns))
print(df.head())

# 7. Exemplos de agregação
if {'ano'}.issubset(df.columns):
    acidentes_ano = df.groupby('ano').size().reset_index(name='qtd_acidentes')
    print(acidentes_ano.head())

if {'uf'}.issubset(df.columns):
    acidentes_uf = df.groupby('uf').size().reset_index(name='qtd_acidentes').sort_values('qtd_acidentes', ascending=False)
    print(acidentes_uf.head())

# 8. Exemplo de exportação
# acidentes_ano.to_csv("outputs/acidentes_por_ano.csv", index=False)
# acidentes_uf.to_csv("outputs/acidentes_por_uf.csv", index=False)
