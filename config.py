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
    
    lvl01 = False
    if lvl01 == False:
    #Lose game rect
     ret1nv_quartel = pygame.Rect(100,100,50,50)
     ret2nv_estabulo = pygame.Rect(200,100,50,50)
     ret3num_soldados = pygame.Rect(300,100,50,50)
     ret4diplomacia = pygame.Rect(400,100,50,50)
     ret5Sair = pygame.Rect(500,100,50,50)
     
     while lvl01 == False: 
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
             pygame.quit()
         
      frames.tick(120)
      tela.fill(azul_fundo)
      pygame.draw.rect(tela,(235,11,0), ret1nv_quartel)
      pygame.draw.rect(tela,(235,11,0), ret2nv_estabulo)
      pygame.draw.rect(tela,(235,11,0), ret3num_soldados)
      pygame.draw.rect(tela,(235,11,0), ret4diplomacia)
      pygame.draw.rect(tela,(235,11,0), ret5Sair)
      pygame.display.update()
      mouseclick = pygame.mouse.get_pos()
      if pygame.mouse.get_pressed() == (1,0,0):
       if ret1nv_quartel.collidepoint(mouseclick):
            lvl01 = True
            print("voce evoluiu o Quartel em 1")
            niveis_iniciais.nv_quartel +=1
            Endgame = False
            break
       if ret2nv_estabulo.collidepoint(mouseclick):
            lvl01 = True
            print("voce evoluiu o Quartel em 1")
            niveis_iniciais.nv_estabulo +=1
            Endgame = False
            break
       if ret3num_soldados.collidepoint(mouseclick):
            lvl01 = True
            print("voce evoluiu o Quartel em 1")
            niveis_iniciais.num_soldados +=10
            Endgame = False
            break
       if ret4diplomacia.collidepoint(mouseclick):
            lvl01 = True
            print("voce evoluiu o Quartel em 1")
            niveis_iniciais.diplomacia +=1
            Endgame = False
            break
       if ret5Sair.collidepoint(mouseclick):
            lvl01 = True
            print("Saindo")
            Endgame = True
            break
            
      if Endgame == True:
        startmenu()
        
################################
#Editar essa parte             #
################################
print("Agora voce pode continuar expandindo seu imperio... mas antes vamos ver o que esta acontecendo por la")
#print(evento_aleatorio())
print(niveis_iniciais.nv_quartel)
print(niveis_iniciais.nv_estabulo)
print(niveis_iniciais.num_soldados)
print(niveis_iniciais.diplomacia)


