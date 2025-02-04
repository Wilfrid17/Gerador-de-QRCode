# Importação das bibliotecas necessárias
import qrcode.constants  # Biblioteca para geração de QR Code
import streamlit as st   # Framework para criação de aplicações web interativas
import qrcode           # Biblioteca principal para criação de QR Codes
from PIL import Image   # Biblioteca para manipulação de imagens
import io               # Biblioteca para manipulação de fluxos de bytes

# Título do aplicativo Streamlit
st.title('Gerador de QrCode')

# Criação de um campo de entrada de texto para a URL
url = st.text_input('Cole sua URL aqui', placeholder='http://exemplo.com')

# Verifica se uma URL foi inserida
if url:
    # Configuração do objeto QR Code
    qr = qrcode.QRCode(
        version=1,      # Versão do QR Code (1-40)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Nível de correção de erro (Baixo)
        box_size=10,  # Tamanho de cada "caixa" do QR Code
        border=4,    # Tamanho da borda do QR Code
    )

    # Adiciona os dados (URL) ao QR Code
    qr.add_data(url) 
    # Gera o QR Code, ajustando automaticamente o tamanho
    qr.make(fit=True)

    # Cria a imagem do QR Code
    # Parâmetros de cor: preto para os dados, branco para o fundo
    img = qr.make_image(fill_color="black", back_color="white")

    # Obtém a imagem PIL (Python Imaging Library)
    pil_img = img.get_image()

    # Exibe a imagem no Streamlit
    st.image(pil_img, caption="Seu QrCode Gerado", use_column_width=True)

    # Prepara a imagem para download
    # Cria um buffer de bytes em memória
    buf = io.BytesIO()
    # Salva a imagem no buffer no formato PNG
    pil_img.save(buf, format="PNG")
    # Obtém os bytes da imagem
    byte_im = buf.getvalue()

    # Cria um botão de download no Streamlit
    st.download_button(
        label="Baixar QrCode",      # Texto do botão
        data=byte_im,               # Dados da imagem
        file_name="qrcode.png",     # Nome do arquivo para download
        mime="image/png"            # Tipo MIME do arquivo
    )