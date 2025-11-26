from pytubefix import YouTube
import streamlit as st
import os 
# Importação desnecessária, mantida apenas para garantir que o script funcione no ambiente Streamlit
# import math 
# from moviepy.editor import VideoFileClip 

# A lista de hashtags virais não é mais necessária para o download simples.
# HASHTAGS_VIRAIS = [...]

def baixar_video_para_servidor(link):
    """
    Baixa o vídeo do YouTube na melhor qualidade progressiva MP4 disponível 
    para o servidor (ambiente Streamlit/Docker).
    Retorna o caminho local e o título.
    """
    try:
        # Inicializa o objeto YouTube
        yt = YouTube(link)

        # Filtra pela melhor stream progressiva (vídeo+áudio juntos) em MP4
        stream = (yt.streams
                  .filter(progressive=True, file_extension='mp4')
                  .order_by('resolution')
                  .desc()
                  .first())
        
        if not stream:
            return None, None, "Erro: Nenhuma stream progressiva MP4 encontrada."

        st.info(f"Iniciando download de '{yt.title}' no servidor...")
        
        # O Streamlit/Docker salva o arquivo no diretório de trabalho do container.
        # O pytubefix retorna o caminho completo onde o arquivo foi salvo.
        arquivo_path = stream.download()

        return arquivo_path, yt.title, f"Download de '{yt.title}' concluído no servidor. Preparando o link para o cliente."

    except Exception as e:
        return None, None, f"Erro ao baixar o vídeo: {e}"

def main():
    """
    Função principal do aplicativo Streamlit, que agora usa st.download_button 
    para enviar o arquivo do servidor para o cliente.
    """
    st.set_page_config(layout="centered")
    st.title("Downloader de Vídeos do YouTube")
    st.markdown("Insira o link para baixar o vídeo completo diretamente para o seu computador.")

    url = st.text_input("Insira o link do vídeo do YouTube:")

    # Um placeholder para exibir o botão de download após o processamento
    download_placeholder = st.empty()
    
    # Armazena o caminho do arquivo temporário para poder removê-lo
    # e o Streamlit poder exibi-lo novamente se necessário.
    if 'arquivo_temp_path' not in st.session_state:
        st.session_state.arquivo_temp_path = None
    if 'titulo_video' not in st.session_state:
        st.session_state.titulo_video = ""

    if st.button("Baixar Vídeo Completo"):
        if url:
            # Limpa estados anteriores
            st.session_state.arquivo_temp_path = None
            st.session_state.titulo_video = ""
            
            # 1. Baixar o arquivo no servidor
            arquivo_path, titulo_video, msg = baixar_video_para_servidor(url)
            st.write(msg)
            
            if arquivo_path:
                st.session_state.arquivo_temp_path = arquivo_path
                st.session_state.titulo_video = titulo_video
                st.success("Download pronto! Clique no botão abaixo para salvar em seu PC.")
                
            else:
                st.error("Não foi possível processar o download. Verifique o link.")

    # 2. Exibir o botão de download para o cliente, se o arquivo estiver pronto no servidor
    if st.session_state.arquivo_temp_path:
        arquivo_path = st.session_state.arquivo_temp_path
        titulo = st.session_state.titulo_video
        
        try:
            # 3. Ler o arquivo temporário como bytes
            with open(arquivo_path, "rb") as file:
                video_bytes = file.read()

            # 4. Criar o nome do arquivo para o cliente (incluindo o título original)
            nome_original = os.path.basename(arquivo_path)
            
            # 5. Usar st.download_button para transferir os bytes para o cliente
            download_placeholder.download_button(
                label=f"⬇️ Salvar: {nome_original}",
                data=video_bytes,
                file_name=nome_original,
                mime="video/mp4",
                key="video_download_button"
            )
            
        except Exception as e:
            st.error(f"Erro ao preparar o download para o cliente: {e}")
        finally:
            # 6. Limpar o arquivo temporário do servidor
            if os.path.exists(arquivo_path):
                os.remove(arquivo_path)
                st.session_state.arquivo_temp_path = None # Limpa o estado
                st.session_state.titulo_video = ""
                st.info("Arquivo temporário no servidor removido com sucesso.")

if __name__ == "__main__":
    main()