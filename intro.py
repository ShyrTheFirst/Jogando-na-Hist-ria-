import pygame
import sys
from menu import startmenu

################################
#Intro do Jogo                 #
################################
def intro():
    pygame.init()
    tela = pygame.display.set_mode([800, 600])
    pygame.display.set_caption("Primeiro Jogo")
    frames = pygame.time.Clock()
    #imagem da introdução
    introducao = pygame.image.load(r'imagens\intro.jpg')
    tela.blit(introducao, (0,0))
    #atualizar a tela, call to event queue e espera
    pygame.display.update()
    pygame.event.pump()
    #mudar espera para poder ler a intro!
    pygame.time.wait(3000)

    sair = False
    while sair != True:
        for event in pygame.event.get():
         if event.type == pygame.QUIT:
             sair = True
         else:
            startmenu()
    pygame.quit()
    pygame.display.quit()
    sys.exit()
    
