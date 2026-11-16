import os
import streamlit as st
from dotenv import load_dotenv
from google import genai
from google.genai import types
from pydantic import BaseModel

load_dotenv()

class Relogio(BaseModel):
    marca: str
    linha: str
    modelo_provavel: str
    tipo: str
    identificacao: str
    caracteristicas: str

st.set_page_config(
    page_title="Identificador de Relógios",
    page_icon="⌚",
    layout="wide"
)

st.title("⌚ Identificador de Relógios com IA")
st.write("Descubra a marca e o modelo provável pela fotografia.")

foto = st.file_uploader(
    "Escolha uma foto do relógio",
    type=["jpg", "jpeg", "png", "webp"]
)

if foto:
    esquerda, direita = st.columns(2)

    with esquerda:
        st.image(foto, width="stretch")

    with direita:
        if st.button("🔎 Identificar relógio", type="primary"):
            chave = os.getenv("GEMINI_API_KEY")

            if not chave:
                st.error("Configure a chave no arquivo .env")
                st.stop()

            formatos = {
                "jpg": "image/jpeg",
                "jpeg": "image/jpeg",
                "png": "image/png",
                "webp": "image/webp"
            }

            extensao = foto.name.rsplit(".", 1)[-1].lower()

            pergunta = """
            Analise a fotografia deste relógio.

            Identifique:
            - Marca
            - Linha ou coleção
            - Modelo provável ou referência
            - Tipo de relógio
            - Características visuais
            - Identificação: exata, provável ou inconclusiva

            Não invente referências ou marcas.
            Se não souber algum campo, escreva
            "Não identificado".

            Não afirme que um relógio é autêntico
            apenas pela fotografia.

            Responda em português.
            """

            try:
                with st.spinner("Analisando relógio..."):
                    client = genai.Client(api_key=chave)

                    resposta = client.models.generate_content(
                        model="gemini-3.1-flash-lite",
                        contents=[
                            types.Part.from_bytes(
                                data=foto.getvalue(),
                                mime_type=formatos[extensao]
                            ),
                            pergunta
                        ],
                        config=types.GenerateContentConfig(
                            response_mime_type="application/json",
                            response_schema=Relogio
                        )
                    )

                    resultado = resposta.parsed

                if resultado is None:
                    st.warning("Não foi possível interpretar a resposta.")
                else:
                    st.subheader("🧠 Resultado da IA")
                    st.write("**Marca:**", resultado.marca)
                    st.write("**Linha:**", resultado.linha)
                    st.write(
                        "**Modelo provável:**",
                        resultado.modelo_provavel
                    )
                    st.write("**Tipo:**", resultado.tipo)
                    st.write(
                        "**Identificação:**",
                        resultado.identificacao
                    )
                    st.write("**Características:**")
                    st.write(resultado.caracteristicas)

            except Exception as erro:
                st.error("Não foi possível analisar a imagem.")
                st.code(str(erro))
