import streamlit as st
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Carregar e processar o arquivo rf_metric1.txt
with open("rf_metric1.txt", "r") as file:
    lines = file.readlines()

# Encontrar a linha onde começa a matriz de confusão e carregar os valores
matrix_lines = []
matrix_started = False
for line in lines:
    if "Matriz de Confusão:" in line:
        matrix_started = True
        continue
    if matrix_started:
        if line.strip():  # Ignora linhas vazias
            # Converter a linha em uma lista de inteiros e adicionar à lista
            row = list(map(int, line.strip().strip("[]").split()))
            matrix_lines.append(row)
        else:
            break  # Encerra a leitura ao encontrar uma linha vazia após a matriz

# Convertendo a lista de linhas em uma matriz numpy
confusion_matrix = np.array(matrix_lines)
df_cm = pd.DataFrame(confusion_matrix, index=[0, 1, 2], columns=[0, 1, 2])

# Título centralizado
st.markdown("<p style='text-align: center;'><strong>Matriz de Confusão dos dados de Teste - Random Forest </h3>", unsafe_allow_html=True)
# Exibir a Matriz de Confusão como um gráfico de calor
plt.figure(figsize=(6, 4))
sns.heatmap(df_cm, annot=True, fmt="d", cmap="Blues")
st.pyplot(plt)
# Fonte centralizada
st.markdown("<p style='text-align: center;'><strong>Fonte:</strong> Do autor, 2024.</p>", unsafe_allow_html=True)