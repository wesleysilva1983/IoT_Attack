import streamlit as st
import joblib
import pandas as pd

# Título do aplicativo
st.subheader("Classificação de ataque RF [Benign, Mirai e Gafgyt]")

# Passo 1: Carregar o modelo salvo
@st.cache_resource  # Cache para evitar recarregar o modelo a cada execução
def load_model():
    return joblib.load('rf_model.joblib')

rf_classifier_loaded = load_model()

# Mapeamento das classes
class_mapping = {0: "Benign", 1: "Attack Mirai", 2: "Attack Gafgyt"}

# Passo 2: Selecionar um arquivo CSV pré-definido
st.write("### Escolha um dos arquivos para fazer predições:")
file_options = {
    "IOT_Device_Ennio.csv": "5 Benign e 5 Attack Mirai",
    "IOT_Device_PT838.csv": "3 Attack Gafgyt - 4 Benign - 4 Attack Mirai",
    "IOT_Device_SNH1011.csv": "3 Benign - 5 Attack Gafgyt - 3 Attack Mirai"
}

# Criando um seletor de arquivos
selected_file = st.selectbox("Selecione o arquivo CSV", options=list(file_options.keys()))

# Exibindo a legenda correspondente ao arquivo selecionado
st.write("### Legenda do arquivo selecionado:")
st.write(file_options[selected_file])

# Carregar o arquivo selecionado para predição
if selected_file:
    try:
        # Carregar os dados do arquivo CSV selecionado
        data = pd.read_csv(selected_file)
        
        # Visualizar as primeiras linhas do arquivo
        st.write("Visualização dos dados carregados:")
        st.write(data.head())  # Mostra as primeiras linhas do arquivo
        
        # Passo 4: Fazer a predição
        y_pred_new = rf_classifier_loaded.predict(data)
        
        # Converter as previsões para os nomes das classes
        y_pred_mapped = [class_mapping[pred] for pred in y_pred_new]
        
        # Exibir as previsões com os nomes das classes
        st.write("Predições para o novo conjunto de dados (com nomes das classes):")
        st.write(y_pred_mapped)
        
        # Opcional: Exibir as previsões junto com os dados de entrada
        result_df = data.copy()
        result_df['Previsão'] = y_pred_mapped
        st.write("Dados com Previsões:")
        st.write(result_df)

        # Opcional: Permitir download do resultado com previsões
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
else:
    st.write("Por favor, selecione um arquivo para fazer predições.")    