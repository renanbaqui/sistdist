# Image Splitting and Merging Bands com Sucuri [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0) [![Terminal](https://badgen.net/badge/icon/terminal?icon=terminal&label)](https://www.microsoft.com/en-us/windows)

## Instalação

- Instalar a Python Imaging Library (https://pillow.readthedocs.io/en/stable/installation.html) 
- Instalar a Biblioteca Sucuri (https://www.youtube.com/watch?v=dOxD1VVdEGk)
- Criar o diretório "splitimgs" dentro da pasta desse git
- Criar uma pasta "dataReceived" e mudar o caminho da pasta dataReceived no código de server.py
- Criar o diretório "imagesHere" de onde ficarão as imagens a ser processadas
- Colocar as imagens dentro do diretório 
- Executar python server.py para iniciar o servidor
- Deixar o servidor sendo executado em um terminal e abrir outro
- Executar, por exemplo, python client.py 3 "caminho/para/imagesHere" (com as aspas) para iniciar a transferência do client para o servidor
- Esperar até que a transferência acabe e o splitting e merging bands das imagens irá começar
- Aguardar até que o processamento acabe e as imagens processadas estarão dentro da pasta "splitimgs"

> O segundo parâmetro no passo 8 é o número de processadores, nesse exemplo eram 3.

> Testado em distribuição Debian GNU/Linux 

Exemplo de tratamento de imagem:

![Antes e Depois](https://github.com/renanbaqui/sistdist/blob/main/processing.png)
