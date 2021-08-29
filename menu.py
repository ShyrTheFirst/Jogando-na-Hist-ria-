import pygame
import sys
from config import niveis

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
 botao_iniciar = pygame.image.load(r'imagens\botao_iniciar.jpg')
 retExit = pygame.Rect(50,390,100,30)
 botao_sair = pygame.image.load(r'imagens\botao_sair.jpg')
#Define the screen and screen color
 tela = pygame.display.set_mode([800, 600])
 tela_intro = pygame.image.load(r'imagens\capa_jogo.jpg')
 tela.blit(tela_intro, (0,0))
#draw rect of buttons
 pygame.draw.rect(tela,(27,109,37), retStart)
 tela.blit(botao_iniciar, (50,270))
 pygame.draw.rect(tela,(27,109,37), retExit)
 tela.blit(botao_sair, (50,390))
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
              pygame.display.quit()
              sys.exit()
