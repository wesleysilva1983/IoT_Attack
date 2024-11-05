import streamlit as st
import joblib
import pandas as pd
import matplotlib.pyplot as plt

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
    # Contar a quantidade de predições por classe
    pred_counts = pd.Series(predictions).value_counts().reindex(class_mapping.values(), fill_value=0)

    # Configuração do estilo do gráfico
    plt.figure(figsize=(8, 5))
    sns.set_style("whitegrid")  # Define um estilo de grade leve
    colors = sns.color_palette("viridis", len(pred_counts))  # Paleta de cores

    # Criar o gráfico de barras
    ax = pred_counts.plot(kind='bar', color=colors, edgecolor='black')
    #plt.title("Distribuição das Predições por Classe", fontsize=16, weight='bold')
    #plt.xlabel("Classe", fontsize=14)
    plt.ylabel("Quantidade", fontsize=10)
    plt.xticks(rotation=45, fontsize=10)
    plt.yticks(fontsize=10)

    # Exibir os valores no topo das barras
    for i, v in enumerate(pred_counts):
        ax.text(i, v + 0.5, str(v), ha='center', va='bottom', fontsize=12, fontweight='bold', color='black')

    st.pyplot(plt)

# Opção 1: Carregar um arquivo CSV personalizado para predição
st.write("**Opção 1: Envie um arquivo CSV personalizado para predições:**")
uploaded_file = st.file_uploader("Envie um arquivo CSV para fazer predições", type=["csv"])

if uploaded_file is not None:
    try:
        # Carregar os dados do arquivo CSV enviado pelo usuário
        data = pd.read_csv(uploaded_file)
        
        # Visualizar as primeiras linhas do arquivo
        st.write("Visualização dos dados carregados:")
        st.write(data.head())  # Mostra as primeiras linhas do arquivo
        
        # Fazer a predição
        y_pred_new = rf_classifier_loaded.predict(data)
        y_pred_mapped = [class_mapping[pred] for pred in y_pred_new]
        
        # Exibir as previsões com os nomes das classes
        st.write("Predições para o novo conjunto de dados (com nomes das classes):")
        st.write(y_pred_mapped)
        
        # Exibir gráfico de barras com a distribuição das predições
        st.write("**Gráfico de Distribuição das Predições:**")
        plot_prediction_distribution(y_pred_mapped)
        
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
        # Carregar os dados do arquivo CSV selecionado
        data = pd.read_csv(selected_file)
        
        # Visualizar as primeiras linhas do arquivo
        st.write("**Visualização dos dados carregados:**")
        st.write(data.head())  # Mostra as primeiras linhas do arquivo
        
        # Fazer a predição
        y_pred_new = rf_classifier_loaded.predict(data)
        y_pred_mapped = [class_mapping[pred] for pred in y_pred_new]
        
        # Exibir as previsões com os nomes das classes
        st.write("**Classes das predições para o conjunto de dados:**")
        pred_counts = pd.Series(y_pred_mapped).value_counts()
        st.write(pred_counts)
        
        # Exibir gráfico de barras com a distribuição das predições
        st.write("**Gráfico de Distribuição das Predições:**")
        plot_prediction_distribution(y_pred_mapped)
        
        # Exibir as previsões junto com os dados de entrada
        result_df = data.copy()
        result_df['Previsão'] = y_pred_mapped
        st.write("**Dados com as Predições:**")
        st.write(result_df)

        # Permitir download do resultado com previsões
        csv = result_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Baixar resultados com previsões",
            data=csv,
            file_name='predicoes.csv',
            mime='text/csv'
        )
        
    except Exception as e:
        st.write("Erro ao fazer predições. Verifique se o arquivo possui o formato correto.")
        st.write(e)
