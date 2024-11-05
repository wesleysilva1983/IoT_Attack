import streamlit as st
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Matriz de Confusão do arquivo
confusion_matrix = np.array([[37442, 0, 3], [0, 38286, 35], [67, 74, 34409]])

# Título da aplicação
st.title("Matriz de Confusão do Modelo RF")

# Mostrar a Matriz de Confusão como tabela
st.subheader("Matriz de Confusão - Tabela")
df_cm = pd.DataFrame(confusion_matrix, index=[0, 1, 2], columns=[0, 1, 2])
st.write(df_cm)

# Exibir a Matriz de Confusão como um gráfico de calor
st.subheader("Matriz de Confusão - Gráfico de Calor")
plt.figure(figsize=(8, 6))
sns.heatmap(df_cm, annot=True, fmt="d", cmap="Blues")
st.pyplot(plt)