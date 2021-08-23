import pygame
import random
from intro import intro
from config import niveis



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

            
def main():
    pygame.init()
    tela = pygame.display.set_mode([800, 600])
    pygame.display.set_caption("Primeiro Jogo")
    frames = pygame.time.Clock()

    sair = False
    while sair != True:
        for event in pygame.event.get():
         if event.type == pygame.QUIT:
             sair = True
         else:
             startmenu()
    pygame.quit()

def startmenu():
 
################################
# Dados do jogador             #
################################
#        Nome = input("Digite seu nome aqui: ")
#        Sexo = input("Você é (H)omem OU (M)ulher? ")
        
################################
# Caso escolha sexo errado     #
################################
#        Continuar = False
#        while Continuar == False:
#         if Sexo == "Homem" or Sexo == "H" :
#          Continuar = True
#         elif Sexo == "Mulher" or Sexo == "M" :
#          Continuar = True
#         else:
#          Sexo= input("Digite Homem ou Mulher, ou ainda H ou M, para continuar. (H/M) :")
#          Continuar = False
#Define the Buttons 
 retStart = pygame.Rect(50,270,100,30)
 retExit = pygame.Rect(50,390,100,30)
#Define the screen and screen color
 tela = pygame.display.set_mode([800, 600])
 tela.fill((10,10,10))
#draw rect of buttons
 pygame.draw.rect(tela,(27,109,37), retStart) 
 pygame.draw.rect(tela,(27,109,37), retExit)
#update screen
 pygame.display.update()
#detect if rect is being pressed
 if pygame.mouse.get_pressed() == (1,0,0):
             mouseposition = pygame.mouse.get_pos()
             if retStart.collidepoint(mouseposition):
              print("Let's Start")
              niveis()
             if retExit.collidepoint(mouseposition):
              print("We are leaving now?")
              pygame.quit()
 
 
             
#pra lembrar sobre rect: (horizontal lugar, vertical lugar, horizontal tamanho, vertical tamanho)








            
      



intro("start")
main()
