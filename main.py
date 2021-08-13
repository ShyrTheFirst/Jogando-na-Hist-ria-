import random
from intro import intro
import config
from config import fase_01
from config import fase_02
from config import fase_03
from config import fase_04
from config import fase_05
from config import fase_final

intro("start")

################################
# Variaveis                    #
################################
lista_medidor = (0,1,2,3,4,5)
medidor_paz = random.choice(lista_medidor)
medidor_guerra = random.choice(lista_medidor)
################################
# Dados do jogador             #
################################
Nome = input("Digite seu nome aqui: ")
Sexo = input("Você é (H)omem OU (M)ulher? ")
################################
# Caso escolha sexo errado     #
################################
Continuar = False
while Continuar == False:
 if Sexo == "Homem" or Sexo == "H" :
    Continuar = True
 elif Sexo == "Mulher" or Sexo == "M" :
    Continuar = True
 else:
    Sexo= input("Digite Homem ou Mulher, ou ainda H ou M, para continuar. (H/M) :")
    Continuar = False

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
            
      

################################
# Inicio do jogo!              #
# Definição da Classe do PJ    #
################################
personagem = Lord(Nome)
################################
# Info inicial para o PJ       #
################################
print(personagem.name)
personagem.medidor()
personagem.guerra_ou_paz()

from teste_objetivo import testar_objetivo

################################
#Primeiro Teste de Objetivo    #
################################
testar_objetivo()

################################
#Inicio do Jogo                #
################################
iniciar_jogo = True
while iniciar_jogo == True:
    fase_01()
    fase_02()
    fase_03()
    fase_04()
    fase_05()
    fase_final()
    print("final")
    
    
    iniciar_jogo = False

