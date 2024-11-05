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

texto = """
<p style="text-align: justify;">
</b> No pré-processamento do dataset três dispositivos IoT foram selecionados para compor o dataset final. Os dados desses três dispositivos foram concatenados em um único dataset, com a criação de uma coluna denominada "attack" que indica a classe do tráfego: 0 para fluxo benigno, 1 para ataques Mirai e 2 para ataques Gafgyt. Em seguida, foi realizada uma análise de dados para identificar e tratar valores irrelevantes ou inválidos. Para garantir uma distribuição equilibrada entre as classes, foi realizado o balanceamento do dataset, resultando em um conjunto de dados com uma quantidade equivalente de amostras para cada classe (benign, Mirai e Gafgyt). Esse dataset balanceado foi, então, utilizado no treinamento do modelo, assegurando uma base homogênea e representativa para a tarefa de detecção de anomalias em dispositivos IoT.
</p>
"""
st.markdown(texto, unsafe_allow_html=True)

# Título da imagem centralizado
st.markdown("<p style='text-align: center;'><strong>Pré Processamento dos Dados</h3>", unsafe_allow_html=True)
# Exibe a imagem
st.image("PreProcess.JPG", use_column_width=True)
# Fonte da imagem centralizada
st.markdown("<p style='text-align: center;'><strong>Fonte:</strong> Do autor, 2024.</p>", unsafe_allow_html=True)

texto = """
<p style="text-align: justify;">
</b> O modelo RandomForestClassifier foi treinado em um loop de 8 iterações, variando o parâmetro "random_state" a cada execução para avaliar a consistência dos resultados. A configuração utilizada para o classificador incluiu 30 estimadores (n_estimators=30), com random_state inicial de 12, critério de entropia para divisão de nós (criterion="entropy"), número máximo de características igual à raiz quadrada do total de atributos (max_features="sqrt"), profundidade máxima de 3 (max_depth=3) e o mínimo de amostras para divisão de nós em 3 (min_samples_split=3). Conforme observado na imagem, o modelo apresentou uma média de acurácia de aproximadamente 99% tanto nos dados de treino quanto nos dados de teste, indicando uma capacidade de generalização efetiva e minimização de overfitting. Além disso, o F1-score também se manteve próximo de 99%, reforçando a robustez do modelo em relação à precisão na classificação dos dados. Esses resultados sugerem que o modelo é altamente eficiente para a tarefa de detecção de ataques em dispositivos IoT, mantendo uma performance consistente e precisa em múltiplas execuções com variações de estado aleatório.
</p>
"""
st.markdown(texto, unsafe_allow_html=True)

# Título da imagem centralizado
st.markdown("<p style='text-align: center;'><strong>Métricas do Modelo - Random Forest </h3>", unsafe_allow_html=True)
# Exibe a imagem
st.image("MetricasModelo.png", use_column_width=True)
# Fonte da imagem centralizada
st.markdown("<p style='text-align: center;'><strong>Fonte:</strong> Do autor, 2024.</p>", unsafe_allow_html=True)

with open("model.py") as f:
    exec(f.read())

st.markdown("""
**Referência:** 

**N-BaIoT—Network-Based Detection of IoT Botnet Attacks Using Deep Autoencoders.**
Yair Meidan, Michael Bohadana, Yael Mathov, Yisroel Mirsky, Dominik Breitenbacher, A. Shabtai, Y. Elovici. 2018.

https://arxiv.org/pdf/1805.03409
""")
