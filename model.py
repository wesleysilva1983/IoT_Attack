import streamlit as st
import joblib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

# Título do aplicativo
st.subheader("Classificação de ataque RF [Benign, Mirai e Gafgyt]")

# Passo 1: Carregar o modelo salvo
@st.cache_resource  # Cache para evitar recarregar o modelo a cada execução
def load_model():
    return joblib.load('rf_model.joblib')

rf_classifier_loaded = load_model()

# Mapeamento das classes
class_mapping = {0: "Benign", 1: "Attack Mirai", 2: "Attack Gafgyt"}

# Função para exibir gráfico de barras
def plot_prediction_distribution(predictions):
    pred_counts = pd.Series(predictions).value_counts().reindex(class_mapping.values(), fill_value=0)
    plt.figure(figsize=(8, 6))
    pred_counts.plot(kind='bar')
    plt.title("Distribuição das Predições por Classe")
    plt.xlabel("Classe")
    plt.ylabel("Quantidade")
    plt.xticks(rotation=45)
    st.pyplot(plt)

# Função para exibir a matriz de confusão
def plot_confusion_matrix(y_true, y_pred):
    cm = confusion_matrix(y_true, y_pred, labels=class_mapping.keys())
    cm_df = pd.DataFrame(cm, index=class_mapping.values(), columns=class_mapping.values())
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm_df, annot=True, fmt="d", cmap="Blues")
    plt.title("Matriz de Confusão")
    plt.xlabel("Classe Prevista")
    plt.ylabel("Classe Real")
    st.pyplot(plt)

# Opção 1: Carregar um arquivo CSV personalizado para predição
st.write("**Opção 1: Envie um arquivo CSV personalizado para predições:**")
uploaded_file = st.file_uploader("Envie um arquivo CSV para fazer predições", type=["csv"])

if uploaded_file is not None:
    try:
        data = pd.read_csv(uploaded_file)
        st.write("Visualização dos dados carregados:")
        st.write(data.head())
        
        # Assumindo que os dados contêm uma coluna 'Classe' com as classes reais
        if 'Classe' in data.columns:
            y_true = data['Classe'].map({v: k for k, v in class_mapping.items()})  # Mapeia as classes reais para os valores numéricos
            X_data = data.drop(columns=['Classe'])
            
            # Fazer a predição
            y_pred = rf_classifier_loaded.predict(X_data)
            y_pred_mapped = [class_mapping[pred] for pred in y_pred]
            
            st.write("Predições para o novo conjunto de dados (com nomes das classes):")
            st.write(y_pred_mapped)
            
            # Exibir gráfico de barras com a distribuição das predições
            st.write("**Gráfico de Distribuição das Predições:**")
            plot_prediction_distribution(y_pred_mapped)
            
            # Exibir matriz de confusão
            st.write("**Matriz de Confusão das Predições:**")
            plot_confusion_matrix(y_true, y_pred)

            # Exibir as previsões junto com os dados de entrada
            result_df = data.copy()
            result_df['Previsão'] = y_pred_mapped
            st.write("Dados com Previsões:")
            st.write(result_df)

            # Permitir download do resultado com previsões
            csv = result_df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Baixar resultados com previsões",
                data=csv,
                file_name='predicoes.csv',
                mime='text/csv'
            )
        else:
            st.write("Erro: A coluna 'Classe' com as classes reais não foi encontrada no arquivo.")
        
    except Exception as e:
        st.write("Erro ao fazer predições. Verifique se o arquivo possui o formato correto.")
        st.write(e)

# Opção 2: Selecionar um arquivo de exemplo pré-definido
st.write("**Opção 2: Escolha um dos arquivos de exemplo para fazer predições:**")
file_options = {
    "IOT_Device_Ennio.csv": "5 Benign e 5 Attack Mirai",
    "IOT_Device_PT838.csv": "3 Attack Gafgyt - 4 Benign - 4 Attack Mirai",
    "IOT_Device_SNH1011.csv": "3 Benign - 5 Attack Gafgyt - 3 Attack Mirai"
}

selected_file = st.selectbox("Selecione o arquivo de exemplo", options=["Nenhum"] + list(file_options.keys()))

if selected_file != "Nenhum":
    st.write(f"**Classificação esperada:** *{file_options[selected_file]}*")

    try:
        data = pd.read_csv(selected_file)
        st.write("**Visualização dos dados carregados:**")
        st.write(data.head())

        if 'Classe' in data.columns:
            y_true = data['Classe'].map({v: k for k, v in class_mapping.items()})
            X_data = data.drop(columns=['Classe'])
            
            y_pred = rf_classifier_loaded.predict(X_data)
            y_pred_mapped = [class_mapping[pred] for pred in y_pred]
            
            st.write("**Classes das predições para o conjunto de dados:**")
            st.write(y_pred_mapped)
            
            st.write("### Gráfico de Distribuição das Predições:")
            plot_prediction_distribution(y_pred_mapped)
            
            st.write("**Matriz de Confusão das Predições:**")
            plot_confusion_matrix(y_true, y_pred)
            
            result_df = data.copy()
            result_df['Previsão'] = y_pred_mapped
            st.write("**Dados com as Predições:**")
            st.write(result_df)

            csv = result_df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Baixar resultados com previsões",
                data=csv,
                file_name='predicoes.csv',
                mime='text/csv'
            )
        else:
            st.write("Erro: A coluna 'Classe' com as classes reais não foi encontrada no arquivo.")
        
    except Exception as e:
        st.write("Erro ao fazer predições. Verifique se o arquivo possui o formato correto.")
        st.write(e)