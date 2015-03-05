import socket
import webapp 
import urllib
import string


class cachecontenidos(webapp.webApp):

    def parse(self,peticion):

        
        try:
            paquete = peticion.split()[1][1:] 
            print paquete
            lista = paquete.split('/') 
        except ValueError:
            return None
       
        return lista[0]

    def process(self,parsedRequest):

        peticion = parsedRequest
        url = "http://" + peticion
        fd = urllib.urlopen(url)
        resultado = fd.read()

        principio = resultado.find("<body")
        final = resultado.find(">",principio)
     
        resultado = resultado[:(final+1)] + "HOLA" + resultado[final+1:]
       


        return ("200 OK", "<html><body><h1>" + resultado + "</body></html>")
        

if __name__ == "__main__" :
    serv = cachecontenidos(socket.gethostname(), 1236)