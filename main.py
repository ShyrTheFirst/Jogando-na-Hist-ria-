import pygame
import random
import sys
from intro import intro



################################
# Variaveis                    #
################################
lista_medidor = (0,1,2,3,4,5)
medidor_paz = random.choice(lista_medidor)
medidor_guerra = random.choice(lista_medidor)

################################
# Classe do jogador            #
################################
class Lord:
    def __init__(self, name):
     if Sexo == "Homem" or Sexo == "H":
         self.name = "Senhor" + " "  + name
     if Sexo == "Mulher" or Sexo == "M":
         self.name = "Senhora" + " " + name
    
################################
# Definição dos medidores      #
################################
    def medidor(self):
     self.medidor = print("Seu medidor de paz está em : ", medidor_paz, "/", "Seu Medidor de guerra está em : ", medidor_guerra)

################################
# Preparar para guerra ou paz  #
################################     
    def guerra_ou_paz(self):
        guerra = False
        if medidor_guerra > medidor_paz:
            if medidor_guerra > 3:
                guerra = True
            elif medidor_guerra < 2:
                guerra = False
        elif medidor_guerra > 3:
            x = medidor_guerra - medidor_paz
            if x > 2:
                guerra = True
            else:
                guerra = False

        if guerra == True:
            print("Você precisa se preparar pra guerra!")
        else:
            print("Aproveite a paz! Evolua suas fazendas")

            



 
 
             
#pra lembrar sobre rect: (horizontal lugar, vertical lugar, horizontal tamanho, vertical tamanho)


intro()
