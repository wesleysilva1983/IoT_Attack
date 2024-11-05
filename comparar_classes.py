import pandas as pd
import sys
from sklearn.metrics import confusion_matrix, classification_report
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Mapeamento das classes
class_mapping = {0: "Benign", 1: "Attack Mirai", 2: "Attack Gafgyt"}

# Função para carregar o modelo
def load_model():
    return joblib.load('rf_model.joblib')

# Carregar o modelo salvo
rf_classifier_loaded = load_model()

# Dicionário de arquivos para predições e classes reais
prediction_files = {
    "IOT_Device_Ennio.csv": "IOT_Device_Ennio_y.csv",
    "IOT_Device_PT838.csv": "IOT_Device_PT838_y.csv",
    "IOT_Device_SNH1011.csv": "IOT_Device_SNH1011_y.csv"
}

# Função para plotar matriz de confusão
def plot_confusion_matrix(cm, classes):
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=classes, yticklabels=classes)
    plt.xlabel("Predições")
    plt.ylabel("Classes Reais")
    plt.title("Matriz de Confusão")
    st.pyplot(plt)

# Verificar se o nome do arquivo de predição foi passado como parâmetro
if len(sys.argv) < 2:
    st.write("Por favor, forneça o nome do arquivo de predição como parâmetro.")
else:
    selected_pred_file = sys.argv[1]  # Arquivo de predição passado como argumento

    # Verificar se o arquivo de predição está no dicionário
    if selected_pred_file not in prediction_files:
        st.write("Arquivo de predição não encontrado.")
    else:
        real_file = prediction_files[selected_pred_file]  # Arquivo de classes reais correspondente
        
        try:
            # Carregar dados para predição e classes reais
            pred_data = pd.read_csv(selected_pred_file)
            real_data = pd.read_csv(real_file)
            
            # Verificar se as dimensões dos dados correspondem
            if len(pred_data) != len(real_data):
                st.write(f"Dimensões incompatíveis entre {selected_pred_file} e {real_file}.")
            else:
                # Fazer predições
                y_pred = rf_classifier_loaded.predict(pred_data)
                
                # Obter classes reais
                y_true = real_data.values.flatten()  # Supondo que esteja em uma única coluna
                
                # Gerar matriz de confusão e relatório de classificação
                cm = confusion_matrix(y_true, y_pred)
                report = classification_report(y_true, y_pred, target_names=class_mapping.values())
                
                # Exibir os resultados
                st.write(f"**Resultados para {selected_pred_file} em comparação com {real_file}**")
                st.write("Relatório de Classificação:")
                st.text(report)
                
                # Plotar matriz de confusão
                st.write("**Matriz de Confusão:**")
                plot_confusion_matrix(cm, classes=class_mapping.values())
        
        except Exception as e:
            st.write("Erro ao carregar arquivos ou realizar predições.")
            st.write(e)
