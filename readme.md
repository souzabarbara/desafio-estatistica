# Repositório: Desafio_ENEM_2023

Este repositório contém as respostas para o Desafio do ENEM 2023, utilizando dados fictícios para análises estatísticas.

## Arquivos no Repositório:

1. `codigo_desafio_enem_2023.ipynb`: Jupyter Notebook contendo o código Python com as respostas para cada uma das questões do desafio.
2. `enem_2023.json`: Arquivo JSON contendo os dados fictícios do ENEM 2023 utilizados para as análises.
3. `README.md`: Este arquivo README contendo informações sobre o repositório e instruções de uso.

## Instruções de Uso:

1. Clone este repositório em seu ambiente local.
2. Certifique-se de ter o ambiente Python configurado em sua máquina.
3. Abra o arquivo `codigo_desafio_enem_2023.ipynb` em um ambiente Jupyter Notebook.
4. Execute cada célula do notebook para obter as respostas para as questões do desafio.
5. Os resultados serão exibidos no próprio notebook.

## Perguntas do Desafio:

1. Qual das disciplinas tem a maior amplitude de nota?
2. Qual é a média e a mediana para cada uma das disciplinas? (Lembre-se de remover todos os valores nulos quando considerar a mediana)
3. Considerando o curso de Ciência da Computação da UFPE, onde o peso cada uma das disciplinas ponderado:
   a. Redação - 2
   b. Matemática e suas Tecnologias - 4
   c. Linguagens, Códigos e suas Tecnologias - 2
   d. Ciências Humanas e suas Tecnologias - 1
   e. Ciências da Natureza e suas Tecnologias - 1
   Qual o desvio padrão e média das notas dos 500 estudantes mais bem colocados considerando esses pesos?
4. Se todos esses estudantes aplicassem para ciência da computação e existem apenas 40 vagas, qual seria a variância e média da nota dos estudantes que entraram no curso de ciência da computação?
5. Qual o valor do teto do terceiro quartil para as disciplinas de matemática e linguagens?
6. Faça o histograma de Redação e Linguagens, de 20 em 20 pontos. Podemos dizer que são histogramas simétricos, justifique e classifique se não assimétricas?
7. Agora coloque um range fixo de 0 até 1000, você ainda tem a mesma opinião quanto a simetria? [plt.hist(dado, bins=_, range=[0, 1000])
8. Faça um boxplot do quartil de todas as disciplinas de ciências da natureza e redação. É possível enxergar outliers? Utilize o método IQR.
9. Remova todos os outliers e verifique se eles são passíveis de alterar a média nacional significativamente? (considere significativamente um valor acima de 5%)
10. Considerando valores nulos, tente encontrar qual seria a melhor medida de tendência que pode substituir as notas nulas. Média, moda ou mediana? Substitua o valor por todos os três e diga qual delas altera menos a média geral e o desvio padrão.

## Sobre o Desafio:

O Desafio do ENEM 2023 consiste em responder a uma série de perguntas relacionadas à análise estatística dos dados fictícios do ENEM 2023, abordando tópicos como amplitude de notas, média, mediana, pesos das disciplinas, desvio padrão, quartis, histogramas, boxplot e remoção de outliers.

## Referências:

Este desafio foi proposto como parte do curso de Estatística Frequências e Medidas, como uma oportunidade para aplicar os conceitos aprendidos em um contexto prático.

Para mais informações sobre o desafio, consulte o arquivo `codigo_desafio_enem_2023.ipynb`.
