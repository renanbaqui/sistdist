# sistdist

# Processamento de Imagem com Sucuri

# Como Instalar

1) Run pip install Pillow
2) Download lfw from http://vis-www.cs.umass.edu/lfw/lfw.tgz (or any set of images you want to use)
3) Create "grayimgs" folder inside the folder you unziped this git
4) Criar uma pasta "dataReceived" e mudar o caminho da pasta dataReceived no codigo de server.py
5) Run python server.py to start the server
Deixar o servidor rodando em um terminal e abrir outro
6) Run python client.py 3 "path/to/the/image_set" (com as aspas) to start the transfer of images from client to server
7) Wait till the transfer is done and the face recognition will automatically start
8) Wait till the processing is done and the recognized faces images will appear inside recognizedFaces folder

Obs: The second parameter in step 5 is the number of processors you want to use, in my case was 3.
