# ⌚ Identificador de Relógios com Inteligência Artificial

## Sobre o projeto

Projeto desenvolvido para estudar Inteligência Artificial, Machine Learning e integração de APIs utilizando Python.

O aplicativo permite enviar fotografias de relógios e utiliza o Google Gemini para tentar identificar marcas, linhas e modelos.

Conta com uma interface visual criada em Streamlit.

## Tecnologias utilizadas

- Python
- Google Gemini API
- Streamlit
- Google GenAI SDK
- scikit-learn
- Machine Learning
- Pydantic

## Funcionalidades

- Upload de fotografias JPG, PNG e WEBP.
- Visualização da fotografia no navegador.
- Identificação da marca e linha do relógio.
- Sugestão de modelo ou referência.
- Identificação do tipo de relógio.
- Descrição das características visuais.
- Indicação de incerteza na identificação.

## Como executar

1. Instale o Python.
2. Baixe este repositório.
3. Abra a pasta no VS Code.
4. Instale as dependências:

    python -m pip install -r requirements.txt

5. Crie um arquivo .env na pasta do projeto.
6. Configure sua chave de API:

    GEMINI_API_KEY=SUA_CHAVE_AQUI

7. Execute o aplicativo:

    python -m streamlit run app.py

8. Abra o endereço local informado no terminal.

## Outros arquivos

- app.py: interface visual com Streamlit.
- identificar_relogio_foto.py: análise de fotografias pelo terminal.
- classificador_relogios.py: exemplo educativo de classificação KNN com quatro modelos.

## Resultados

O aplicativo foi testado com uma fotografia de relógio Montblanc.

A IA conseguiu gerar uma análise estruturada, incluindo marca, linha provável, tipo de relógio e características visuais.

O modelo exato não foi identificado nesse teste.

## Limitações

- A identificação por fotografia é uma estimativa.
- A IA pode confundir marcas e modelos semelhantes.
- O programa não comprova autenticidade de relógios.
- A análise depende da disponibilidade da API Gemini.
- O classificador KNN utiliza somente quatro exemplos.
- O aplicativo não possui uma avaliação formal de precisão.

## Objetivo

Desenvolver conhecimentos práticos em Inteligência Artificial, Python, processamento de imagens por modelos multimodais e integração com APIs.

## Autor

Felipe Talassi Honora Filho

Estudante de Sistemas de Informação na Faculdade Impacta de Tecnologia.

Projeto desenvolvido para estudo e portfólio profissional.