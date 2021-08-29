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
     ret1nv_quartel = pygame.Rect(700,528,50,50)
     quartel = pygame.image.load(r'C:\Users\sokir\Desktop\Jogando na História\imagens\quartel.png')
        #ESTABULO
     local_estabulo = (300,452)
     ret2nv_estabulo = pygame.Rect(300,452,50,50)
     estabulo = pygame.image.load(r'C:\Users\sokir\Desktop\Jogando na História\imagens\estabulo.png')
        #CAMPO DE TREINAMENTO
     local_camp_treino = (600,452)
     ret3num_soldados = pygame.Rect(600,452,50,50)
     camp_treino = pygame.image.load(r'C:\Users\sokir\Desktop\Jogando na História\imagens\camp_treino.jpg')
        #EMBAIXADA
     local_embaixada = (300,332)
     ret4diplomacia = pygame.Rect(300,332,50,50)
     embaixada = pygame.image.load(r'C:\Users\sokir\Desktop\Jogando na História\imagens\embaixada.png')
     ret5Sair = pygame.Rect(950,100,50,50)
     aldeia = pygame.image.load(r'C:\Users\sokir\Desktop\Jogando na História\imagens\aldeia.jpg')
     
     while lvl01 == False: 
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
             pygame.quit()
         
      frames.tick(120)
      tela.blit(aldeia, (0,0))
      pygame.draw.rect(tela,marrom_claro, ret1nv_quartel)
      tela.blit(quartel, local_quartel)
      pygame.draw.rect(tela,marrom_claro, ret2nv_estabulo)
      tela.blit(estabulo, local_estabulo)
      pygame.draw.rect(tela,marrom_claro, ret3num_soldados)
      tela.blit(camp_treino, local_camp_treino)
      pygame.draw.rect(tela,marrom_claro, ret4diplomacia)
      tela.blit(embaixada, local_embaixada)
      pygame.draw.rect(tela,marrom_claro, ret5Sair)
      pygame.display.update()
      mouseclick = pygame.mouse.get_pos()
      if pygame.mouse.get_pressed() == (1,0,0):
       if ret1nv_quartel.collidepoint(mouseclick):
            print("voce evoluiu o Quartel em 1")
            niveis_iniciais.nv_quartel +=1
       if ret2nv_estabulo.collidepoint(mouseclick):
            print("voce evoluiu o Estabulo em 1")
            niveis_iniciais.nv_estabulo +=1
       if ret3num_soldados.collidepoint(mouseclick):
            print("voce treinou 10 novos soldados")
            niveis_iniciais.num_soldados +=10
       if ret4diplomacia.collidepoint(mouseclick):
            print("voce fez amizade com 1 novo feudo")
            niveis_iniciais.diplomacia +=1
       if ret5Sair.collidepoint(mouseclick):
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
