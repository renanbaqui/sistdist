# Image Splitting and Merging Bands com Sucuri

# Como Instalar

1) Instalar a Python Imaging Library (https://pillow.readthedocs.io/en/stable/installation.html) 
2) Instalar a biblioteca Sucuri (https://www.youtube.com/watch?v=dOxD1VVdEGk)
3) Criar o diretório "grayimgs" dentro da pasta desse git
4) Criar uma pasta "dataReceived" e mudar o caminho da pasta dataReceived no código de server.py
5) Colocar as imagens dentro do diretório 
6) Executar python server.py para iniciar o servidor
7) Deixar o servidor sendo executado em um terminal e abrir outro
8) Executar python client.py 3 "caminho/para/dataReceived" (com as aspas) para iniciar a transferência do client para o servidor
9) Esperar até que a transferência acabe e o splitting e merging bands das imagens irá começar
10) Esperar até que o processamento acabe e as imagens processadas estarão dentro da pasta "grayimgs"

Obs: O segundo parâmetro no passo 8 é o número de processadores, nesse caso eram 3.
