import os
import re
import matplotlib.pyplot as plt
import streamlit as st

# Configurações do Streamlit
st.title("Random Forest")
st.subheader("Loop de treinamento[8x]")

# Caminho local onde estão os arquivos de métricas no Codespaces
path = "./"  # Ajuste para o diretório atual onde os arquivos estão

# Lista dos arquivos de métricas
metric_files = [f"rf_metric{i}.txt" for i in range(1, 9)]  # Lista de nomes dos arquivos

# Dicionário para armazenar as métricas
metrics = {
    "Acurácia (Teste)": [],
    "F1-Score (Teste)": [],
    "Acurácia (Treino)": [],
    "F1-Score (Treino)": []
}

# Regex para capturar as métricas do arquivo
pattern = r"(Acurácia \(Teste\):|F1-Score \(Teste\):|Acurácia \(Treino\):|F1-Score \(Treino\):) (\d+\.\d+)"

# Lendo cada arquivo de métrica e extraindo as métricas
for file_name in metric_files:
    # Caminho completo do arquivo
    file_path = os.path.join(path, file_name)
    
    # Abrindo e lendo o conteúdo do arquivo
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            
            # Encontrando as métricas com regex
            matches = re.findall(pattern, content)
            
            for metric_name, value in matches:
                metric_name = metric_name.replace(":", "").strip()  # Remove dois pontos e espaços
                if metric_name in metrics:
                    metrics[metric_name].append(float(value))
                else:
                    st.write(f"Chave inesperada encontrada: '{metric_name}'")
    except FileNotFoundError:
        st.write(f"Arquivo {file_name} não encontrado.")

# Gerando o boxplot com 'tick_labels' atualizado
fig, ax = plt.subplots(figsize=(10, 6))
ax.boxplot(metrics.values(), tick_labels=metrics.keys())
ax.set_title("Boxplot das Métricas do Modelo")
ax.set_ylabel("Valores das Métricas")
ax.set_xticklabels(metrics.keys(), rotation=15)

# Exibindo o gráfico no Streamlit
st.pyplot(fig)