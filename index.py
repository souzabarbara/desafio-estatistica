import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import seaborn as sns

caminho_arquivo = 'data-enem.json'

df = pd.read_json(caminho_arquivo, orient='records')
df_numeric = df.apply(pd.to_numeric, errors='coerce')

# Questão 1

amplitude_por_disciplina = df_numeric.max() - df_numeric.min()
disciplina_maior_amplitude = amplitude_por_disciplina.idxmax()

print("A disciplina com a maior amplitude de nota é:", disciplina_maior_amplitude)

# Questão 2

df_filled = df_numeric.fillna(df_numeric.mean())

dado_para_excluir = 'Sexo'
df_atualizado = df_filled.drop(columns=[dado_para_excluir])

media_por_disciplina = df_atualizado.mean()
mediana_por_disciplina = df_atualizado.median()

for disciplina in df_atualizado.columns:
    print(f"Disciplina: {disciplina}")
    print(f"Média: {media_por_disciplina[disciplina]}")
    print(f"Mediana: {mediana_por_disciplina[disciplina]}\n")

# Questão 3

pesos = {
    'Redação': 2,
    'Matemática e suas Tecnologias': 4,
    'Linguagens, Códigos e suas Tecnologias': 2,
    'Ciências Humanas e suas Tecnologias': 1,
    'Ciências da Natureza e suas Tecnologias': 1
}

df['Nota Ponderada'] = (df['Redação'] * pesos['Redação'] + 
                        df['Matemática'] * pesos['Matemática e suas Tecnologias'] +
                        df['Linguagens'] * pesos['Linguagens, Códigos e suas Tecnologias'] +
                        df['Ciências humanas'] * pesos['Ciências Humanas e suas Tecnologias'] +
                        df['Ciências da natureza'] * pesos['Ciências da Natureza e suas Tecnologias'])

df_top_500 = df.nlargest(500, 'Nota Ponderada')

media = np.mean(df_top_500['Nota Ponderada'])
desvio_padrao = np.std(df_top_500['Nota Ponderada'])

print("Média das notas dos 500 estudantes mais bem colocados:", media / 10)
print("Desvio padrão das notas dos 500 estudantes mais bem colocados:", desvio_padrao)

# Questão 4

df_ciencia_computacao = df_top_500.head(40)

media_ciencia_computacao = df_ciencia_computacao['Nota Ponderada'].mean()
variancia_ciencia_computacao = df_ciencia_computacao['Nota Ponderada'].var()

print("Média das notas dos estudantes de Ciência da Computação:", media_ciencia_computacao / 10)
print("Variância das notas dos estudantes de Ciência da Computação:", variancia_ciencia_computacao)

# Questão 5

q3_matematica = df['Matemática'].quantile(0.75)
q3_linguagens = df['Linguagens'].quantile(0.75)

teto_q3_matematica = math.ceil(q3_matematica)
teto_q3_linguagens = math.ceil(q3_linguagens)

print("Teto do terceiro quartil para a disciplina de Matemática:", teto_q3_matematica)
print("Teto do terceiro quartil para a disciplina de Linguagens:", teto_q3_linguagens)

# Questão 6

plt.figure(figsize=(10, 6))
plt.hist(df['Redação'], bins=range(0, 1020, 20), color='blue', edgecolor='black')
plt.title('Histograma de Redação')
plt.xlabel('Pontuação')
plt.ylabel('Frequência')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.hist(df['Linguagens'], bins=range(0, 1020, 20), color='green', edgecolor='black')
plt.title('Histograma de Linguagens')
plt.xlabel('Pontuação')
plt.ylabel('Frequência')
plt.grid(True)
plt.show()

# Questão 7

plt.figure(figsize=(10, 6))
plt.hist(df['Redação'], bins=range(0, 1020, 20), range=[0, 1000], color='blue', edgecolor='black')
plt.title('Histograma de Redação (Intervalo Fixo: 0-1000)')
plt.xlabel('Pontuação')
plt.ylabel('Frequência')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.hist(df['Linguagens'], bins=range(0, 1020, 20), range=[0, 1000], color='green', edgecolor='black')
plt.title('Histograma de Linguagens (Intervalo Fixo: 0-1000)')
plt.xlabel('Pontuação')
plt.ylabel('Frequência')
plt.grid(True)
plt.show()

# Questão 8

df_ciencias_redacao = df[['Ciências da natureza', 'Redação']]

plt.figure(figsize=(10, 6))
sns.boxplot(data=df_ciencias_redacao)
plt.title('Boxplot das Disciplinas de Ciências da Natureza e Redação (com outliers)')
plt.xlabel('Disciplina')
plt.ylabel('Pontuação')
plt.grid(True)
plt.show()

# Questão 9

media_nacional_antes = df['Nota Ponderada'].mean()

Q1 = df['Nota Ponderada'].quantile(0.25)
Q3 = df['Nota Ponderada'].quantile(0.75)
IQR = Q3 - Q1
limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR
df_sem_outliers = df[(df['Nota Ponderada'] >= limite_inferior) & (df['Nota Ponderada'] <= limite_superior)]

media_nacional_depois = df_sem_outliers['Nota Ponderada'].mean()

alteracao_percentual = ((media_nacional_depois - media_nacional_antes) / media_nacional_antes) * 100

if abs(alteracao_percentual) > 5:
    print("A remoção dos outliers alterou a média nacional significativamente.")
else:
    print("A remoção dos outliers não alterou significativamente a média nacional.")

print(f"Média nacional antes da remoção dos outliers: {media_nacional_antes}")
print(f"Média nacional após a remoção dos outliers: {media_nacional_depois}")
print(f"Alteração percentual na média nacional: {alteracao_percentual:.2f}%")

# Questão 10

media_substituida = df['Nota Ponderada'].fillna(df['Nota Ponderada'].mean())
moda_substituida = df['Nota Ponderada'].fillna(df['Nota Ponderada'].mode()[0])  
mediana_substituida = df['Nota Ponderada'].fillna(df['Nota Ponderada'].median())

media_antes = df['Nota Ponderada'].mean()
desvio_padrao_antes = df['Nota Ponderada'].std()

media_media = media_substituida.mean()
desvio_padrao_media = media_substituida.std()

media_moda = moda_substituida.mean()
desvio_padrao_moda = moda_substituida.std()

media_mediana = mediana_substituida.mean()
desvio_padrao_mediana = mediana_substituida.std()

print("Alterações na média geral e no desvio padrão após substituir os valores nulos:")
print("Média e desvio padrão antes da substituição:", media_antes, desvio_padrao_antes)
print("Média e desvio padrão após substituir com a média:", media_media, desvio_padrao_media)
print("Média e desvio padrão após substituir com a moda:", media_moda, desvio_padrao_moda)
print("Média e desvio padrão após substituir com a mediana:", media_mediana, desvio_padrao_mediana)
