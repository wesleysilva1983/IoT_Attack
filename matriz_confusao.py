import streamlit as st
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Matriz de Confusão do arquivo
confusion_matrix = np.array([[37442, 0, 3], [0, 38286, 35], [67, 74, 34409]])
df_cm = pd.DataFrame(confusion_matrix, index=[0, 1, 2], columns=[0, 1, 2])

# Título centralizado
st.markdown("<p style='text-align: center;'><strong>Matriz de Confusão do Modelo - Random Forest </h3>", unsafe_allow_html=True)
# Exibir a Matriz de Confusão como um gráfico de calor
plt.figure(figsize=(8, 6))
sns.heatmap(df_cm, annot=True, fmt="d", cmap="Blues")
st.pyplot(plt)
# Fonte centralizada
st.markdown("<p style='text-align: center;'><strong>Fonte:</strong> Do autor, 2024.</p>", unsafe_allow_html=True)