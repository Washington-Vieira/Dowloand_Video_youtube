# Usa a imagem oficial do Python como base
FROM python:3.11-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o arquivo de requisitos e o instala primeiro para aproveitar o cache do Docker
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o seu script principal (assumindo que você renomeou o 'downloader_simples.py' para 'dowloand_youtube.py')
COPY dowloand_youtube.py .

# Expõe a porta que o Streamlit usa (padrão 8501)
EXPOSE 8501

# Define o comando de entrada para rodar o Streamlit
# O comando usa a porta 8501 e desativa o navegador automático
CMD ["streamlit", "run", "dowloand_youtube.py", "--server.port", "8501", "--server.address", "0.0.0.0"]

# Sugestão de comandos para construir e rodar (Não faz parte do Dockerfile)
# 1. Construir: docker build -t meu-downloader-yt .
# 2. Rodar: docker run -p 8501:8501 meu-downloader-yt