import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

chave = os.getenv("GEMINI_API_KEY")

if not chave:
    print("Configure sua chave no arquivo .env")
    raise SystemExit

client = genai.Client(api_key=chave)

print("=== IDENTIFICADOR DE RELOGIOS COM IA ===")

caminho = input("Caminho da foto do relogio: ")
caminho = caminho.strip().strip('"').strip("'")

arquivo = Path(caminho)

formatos = {
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".webp": "image/webp"
}

tipo = formatos.get(arquivo.suffix.lower())

if not arquivo.is_file() or not tipo:
    print("Imagem nao encontrada ou formato invalido.")
    raise SystemExit

pergunta = """
Analise a fotografia deste relógio.

Identifique, se possível:
1. Marca
2. Linha ou coleção
3. Modelo ou referência
4. Tipo de relógio
5. Características visuais importantes

Não invente números de referência.
Se não conseguir identificar o modelo exato,
diga que é uma identificação aproximada.
Se houver dúvida, apresente a incerteza.
Responda em português.
"""

try:
    imagem = arquivo.read_bytes()

    resposta = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=[
            types.Part.from_bytes(
                data=imagem,
                mime_type=tipo
            ),
            pergunta
        ]
    )

    print("\n=== RESULTADO DA ANALISE ===")
    print(resposta.text or "Sem resposta da IA.")

except Exception as erro:
    print("Nao foi possivel analisar a imagem.")
    print(f"Detalhes: {erro}")
