🎥 Downloader Simples de Vídeos do YouTube (Streamlit/Docker)

Este projeto é um aplicativo web simples construído com Streamlit e Python, utilizando a biblioteca pytubefix, para baixar vídeos do YouTube em sua qualidade original MP4 diretamente para o computador do usuário, sem cortes ou redimensionamentos.

💻 1. Estrutura do Projeto

O repositório contém os seguintes arquivos principais:

Arquivo

Descrição

dowloand_youtube.py

O código principal do Streamlit que gerencia o download.

requirements.txt

Lista de dependências Python necessárias (streamlit, pytubefix).

Dockerfile

Define o ambiente para criar a imagem Docker do aplicativo.

.gitignore

Lista arquivos e pastas (como vídeos baixados e caches) a serem ignorados pelo Git.

🛠️ 2. Pré-requisitos

Para rodar este projeto, você precisa ter instalado:

Python 3.8+

Docker (Para a abordagem de deploy)

🚀 3. Instalação e Execução (Modo Local)

Se você quiser rodar o aplicativo diretamente no seu ambiente Python (sem Docker):

Clone o repositório:

git clone [SEU_LINK_DO_REPOSITORIO]
cd [NOME_DO_REPOSITORIO]


Instale as dependências:

pip install -r requirements.txt


Execute o aplicativo Streamlit:

streamlit run dowloand_youtube.py


O aplicativo será aberto automaticamente no seu navegador, geralmente em http://localhost:8501.

🐳 4. Deploy com Docker (Recomendado para Produção)

Para criar um ambiente isolado e pronto para o deploy (por exemplo, em um servidor na nuvem), use o Docker:

4.1. Construir a Imagem

O comando a seguir constrói a imagem Docker, baseada no Dockerfile, instalando todas as dependências:

docker build -t meu-downloader-yt .


4.2. Rodar e Ativar o Container

Este comando inicia o container em segundo plano (-d) e mapeia a porta 8501 do container para a porta 8501 da sua máquina, tornando o servidor acessível:

docker run -d -p 8501:8501 meu-downloader-yt


4.3. Acesso

O aplicativo Streamlit estará acessível em: http://localhost:8501.

4.4. Comandos Úteis do Docker

Comando

Descrição

docker ps

Lista os containers ativos.

docker stop [ID_DO_CONTAINER]

Para um container específico.

docker logs [ID_DO_CONTAINER]

Exibe os logs de execução do Streamlit.

docker rm [ID_DO_CONTAINER]

Remove um container parado.

docker rmi meu-downloader-yt

Remove a imagem localmente.

🚫 5. Configuração do .gitignore

O arquivo .gitignore foi configurado para ignorar caches do Python/Streamlit e, criticamente, qualquer arquivo de vídeo baixado (*.mp4, *.webm, etc.), garantindo que seu repositório Git permaneça limpo e leve.

Verifique o conteúdo do arquivo .gitignore para detalhes completos.