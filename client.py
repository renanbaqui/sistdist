import xmlrpclib
import os
import sys
import time

proxy = xmlrpclib.ServerProxy('http://localhost:9000', allow_none=True)

def list_imgs(rootdir):
	for current, directories, files in os.walk(rootdir):
		for f in files:
			with open(current + '/' + f, "rb") as handle:
				binary_data = xmlrpclib.Binary(handle.read())
			proxy.server_receive_file(binary_data, f)
	print "Imagens enviadas pelo client com sucesso! Aguardando o inicio do image splitting and merging bands pelo servidor."
	start = sucuri(int(sys.argv[1]))

def sucuri(nprocs):
	proxy.sucuri(nprocs)
	print "Processamento das imagens iniciado. Aguardando o termino do image splitting and merging bands pelo servidor."

t0 = time.time()
imagePath = list_imgs(sys.argv[2])
t1 = time.time()
print "Processamento terminado. Tempo total do processamento das imagens = %.3f" %(t1-t0)
