import pygame
import random
import niveis_iniciais

def niveis():
    Endgame = False
    tela = pygame.display.set_mode([1024, 768])
    frames = pygame.time.Clock()
    azul_fundo = (51,216,230)
    verde_ganhou = (120,218,122)
    vermelho_perdeu = (193,30,30)
    verde_grama = (23,115,30)
    marrom_claro = (210,180,140)
    
    lvl01 = False
    if lvl01 == False:
    #Lose game rect
        #QUARTEL
     local_quartel = (700,528)
     ret1nv_quartel = pygame.Rect(700,528,150,120)
     quartel = pygame.image.load(r'imagens\quartel.png')
        #ESTABULO
     local_estabulo = (215,420)
     ret2nv_estabulo = pygame.Rect(215,420,150,120)
     estabulo = pygame.image.load(r'imagens\estabulo.png')
        #CAMPO DE TREINAMENTO
     local_camp_treino = (520,400)
     ret3num_soldados = pygame.Rect(520,400,150,120)
     camp_treino = pygame.image.load(r'imagens\camp_treino.jpg')
        #EMBAIXADA
     local_embaixada = (250,300)
     ret4diplomacia = pygame.Rect(250,300,150,120)
     embaixada = pygame.image.load(r'imagens\embaixada.png')
     ret5Sair = pygame.Rect(950,100,50,50)
     ret6edificio = pygame.Rect(600,240,150,120)
     edificio = pygame.image.load(r'imagens\edificio.png')
     aldeia = pygame.image.load(r'imagens\aldeia.jpg')
     lvl_up = pygame.image.load(r'imagens\lvl_up.png')

     #600,240 = edificio principal
     
     while lvl01 == False: 
              
      frames.tick(120)
      tela.blit(aldeia, (0,0))
      tela.blit(quartel, local_quartel)
      tela.blit(estabulo, local_estabulo)
      tela.blit(camp_treino, local_camp_treino)
      tela.blit(embaixada, local_embaixada)
      pygame.draw.rect(tela,marrom_claro, ret5Sair)
      pygame.display.update()
      mouseclick = pygame.mouse.get_pos()
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
             pygame.quit()
         if event.type == pygame.MOUSEBUTTONDOWN:
          if event.button == 1:
           if ret1nv_quartel.collidepoint(mouseclick):
            tela.blit(lvl_up, mouseclick)
            pygame.display.update()
            print("voce evoluiu o Quartel em 1")
            niveis_iniciais.nv_quartel +=1
           if ret2nv_estabulo.collidepoint(mouseclick):
            tela.blit(lvl_up, mouseclick)
            pygame.display.update()
            print("voce evoluiu o Estabulo em 1")
            niveis_iniciais.nv_estabulo +=1
           if ret3num_soldados.collidepoint(mouseclick):
            tela.blit(lvl_up, mouseclick)
            pygame.display.update()
            print("voce treinou 10 novos soldados")
            niveis_iniciais.num_soldados +=10
           if ret4diplomacia.collidepoint(mouseclick):
            tela.blit(lvl_up, mouseclick)
            pygame.display.update()
            print("voce fez amizade com 1 novo feudo")
            niveis_iniciais.diplomacia +=1
           if ret5Sair.collidepoint(mouseclick):
            print("Saindo")
            Endgame = True
            break
           if ret6edificio.collidepoint(mouseclick):
            print(niveis_iniciais.nv_quartel)
            print(niveis_iniciais.nv_estabulo)
            print(niveis_iniciais.num_soldados)
            print(niveis_iniciais.diplomacia)
            
      if Endgame == True:
        from menu import startmenu
        startmenu()
        break
    
