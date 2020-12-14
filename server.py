import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer
import logging
import os
import sys
import time
import cv2

sys.path.append(os.environ['PYDFHOME'])
from pyDF import *

from PIL import Image

save_dir = 'splitimgs'

# Logging
logging.basicConfig(level=logging.INFO)

server = SimpleXMLRPCServer(
    ('localhost', 9000),
    logRequests=True,
    allow_none=True
)
# Mudar este diretorio
dataReceivedFolder = "/home/osboxes/Downloads/Trabalho/sistdist-main/dataReceived"

def server_receive_file(self,directory):
        with open("dataReceived/"+directory, "wb") as handle:
            handle.write(self.data)
            return True


server.register_function(server_receive_file)

def list_imgs(rootdir):
    fnames = []

    for current, directories, files in os.walk(rootdir):
        for f in files:
        	fnames.append(current + '/' + f)
 
    fnames.sort()
    return fnames


def rgb2gray(args):
    fname = args[0]
    splitname = fname.split('/')[-1]
    img = Image.open(fname)
    
    red, green, blue = img.split()

    print(img.mode) # Output: RGB
    print(red.mode) # Output: L
    print(green.mode) # Output: L
    print(blue.mode) # Output: L

    new_image = Image.merge("RGB", (green, red, blue))

    splitname = save_dir + '/' +  splitname.split('.')[0]  + '.png'

    new_image.save(splitname)



    return splitname


def print_name(args):
    fname = args[0]

    print "Convertido %s" %fname



def sucuri(nprocs):
    nprocs = nprocs
    imagePath = list_imgs(dataReceivedFolder)

    graph = DFGraph()
    sched = Scheduler(graph, nprocs, mpi_enabled = False)



    feed_files = Source(imagePath)

    convert_file = FilterTagged(rgb2gray, 1)  

    pname = Serializer(print_name, 1)


    graph.add(feed_files)
    graph.add(convert_file)
    graph.add(pname)


    feed_files.add_edge(convert_file, 0)
    convert_file.add_edge(pname, 0)

    t0 = time.time()
    sched.start()
    t1 = time.time()
    print "Tempo de execucao: %.3f" %(t1-t0)

server.register_function(sucuri)

if __name__ == '__main__':
	# Inicia o servidor
	try:
	    print('Use Control-C para sair')
	    server.serve_forever()
	except KeyboardInterrupt:
	    print('Saindo')
