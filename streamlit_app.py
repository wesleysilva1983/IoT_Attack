import streamlit as st

st.markdown("""
### Pós-graduação em Ciência da Computação - UEL
**Projeto:** Detecção de Ataques no Tráfego de Dispositivos IoT.
            
**Disciplina:** 2COP507 Reconhecimento de Padrões.
                    
**Docentes:** Dr.  Bruno Bogaz Zarpelão, Dr. Sylvio Barbon Junior.
            
**Discente:** Wesley Candido da Silva.
            
**Dataset:** N-BaIoT Dataset to Detect IoT Botnet Attacks

**Link:** https://www.kaggle.com/datasets/mkashifn/nbaiot-dataset
""")

texto = """
<p style="text-align: justify;">
<b>Resumo:</b> O presente projeto tem como objetivo a predição de ataques em dispositivos IoT, utilizando o dataset "N-BaIoT Dataset to Detect IoT Botnet Attacks". Esse conjunto de dados abrange 115 atributos relacionados ao tráfego de rede desses dispositivos, incluindo informações detalhadas sobre o fluxo de rede de nove dispositivos IoT comerciais que foram submetidos a ataques DDoS, utilizando dois dos botnets mais comuns: Mirai e Gafgyt (também conhecido como BASHLITE). Entre os atributos do dataset, incluem-se informações como IP, jitter (variação temporal entre pacotes) e socket (portas TCP/UDP). A partir desses atributos, foram extraídas diversas estatísticas, incluindo peso, média, desvio padrão, raio, magnitude, covariância e coeficiente de correlação de Pearson, utilizadas para caracterizar o comportamento normal do tráfego e identificar anomalias associadas a atividades de botnets. Devido ao grande volume de dados, totalizando aproximadamente 1,7 GB, a análise e o desenvolvimento do modelo de detecção foram focados em três dispositivos IoT selecionados para o treinamento e teste do modelo. Posteriormente, para validação e verificação da capacidade de generalização, os dados dos demais dispositivos IoT foram utilizados para predição dos ataques. Os resultados foram satisfatórios, com o modelo sendo capaz de prever corretamente a ocorrência de ataques e identificar o tipo específico de ataque DDoS em execução.
</p>
"""
st.markdown(texto, unsafe_allow_html=True)

# Título da imagem centralizado
st.markdown("<p style='text-align: center;'><strong>Arquitetura da coleta de dados</h3>", unsafe_allow_html=True)
# Exibe a imagem
st.image("Arquitetura.jpg", use_column_width=True)
# Fonte da imagem centralizada
st.markdown("<p style='text-align: center;'><strong>Fonte:</strong> Yair Meidan, 2018.</p>", unsafe_allow_html=True)

# Título da imagem centralizado
st.markdown("<p style='text-align: center;'><strong>Pré Processamento dos Dados</h3>", unsafe_allow_html=True)
# Exibe a imagem
st.image("PreProcess.JPG", use_column_width=True)
# Fonte da imagem centralizada
st.markdown("<p style='text-align: center;'><strong>Fonte:</strong> Do autor, 2024.</p>", unsafe_allow_html=True)

# Título da imagem centralizado
st.markdown("<p style='text-align: center;'><strong>Métricas do Modelo - Random Forest </h3>", unsafe_allow_html=True)
# Exibe a imagem
st.image("MetricasModelo.png", use_column_width=True)
# Fonte da imagem centralizada
st.markdown("<p style='text-align: center;'><strong>Fonte:</strong> Do autor, 2024.</p>", unsafe_allow_html=True)

with open("model.py") as f:
    exec(f.read())
