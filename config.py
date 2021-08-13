import random
import niveis_iniciais

################################
#Definições das fases          #
################################
def evento_aleatorio():
    lista_evento = ("ataque inesperado", "fome entre os servos", "doenças infecciosas")
    evento_escolhido = random.choice(lista_evento)
    return evento_escolhido
    
def fase_01():
 print("inicio da fase, texto de abertura")
 
################################
#Escolha 1 da fase 1           #
################################
 escolhendo ="fase01.1"
 while escolhendo =="fase01.1":
    escolha_01= int(input("O que você quer evoluir primeiro: 1 para quartel/2 para estabulo/3 para soldados/4 para buscar diplomacia "))
    if escolha_01 == 1:
    	print("voce evoluiu o Quartel em 1")
    	niveis_iniciais.nv_quartel +=1
    	escolhendo = "passou de fase"
    elif escolha_01 == 2:
    	print("voce evoluiu o Estabulo em 1")
    	niveis_iniciais.nv_estabulo +=1
    	escolhendo = "passou de fase"
    elif escolha_01 == 3:
    	print("voce contratou mais 10 soldados")
    	niveis_iniciais.num_soldados +=10
    	escolhendo = "passou de fase"
    elif escolha_01 == 4:
    	print("voce fez diplomacia com um novo país")
    	niveis_iniciais.diplomacia +=1
    	escolhendo = "passou de fase"
    elif escolha_01> 5 or escolha_01< 1:
        print("Digite um valor valido")
        escolhendo ="fase01.1"
        
################################
#Editar essa parte             #
################################
 print("Agora voce pode continuar expandindo seu imperio... mas antes vamos ver o que esta acontecendo por la")
 print(evento_aleatorio())

################################
#Escolha 2 da fase 1           #
################################
 escolhendo ="fase01.2"
 while escolhendo =="fase01.2":
    escolha_02= int(input("O que você quer evoluir primeiro: 1 para quartel/2 para estabulo/3 para soldados/4 para buscar diplomacia "))
    if escolha_02 == 1:
    	print("voce evoluiu o Quartel em 1")
    	niveis_iniciais.nv_quartel +=1
    	escolhendo = "passou de fase"
    elif escolha_02 == 2:
    	print("voce evoluiu o Estabulo em 1")
    	niveis_iniciais.nv_estabulo +=1
    	escolhendo = "passou de fase"
    elif escolha_02 == 3:
    	print("voce contratou mais 10 soldados")
    	niveis_iniciais.num_soldados +=10
    	escolhendo = "passou de fase"
    elif escolha_02 == 4:
    	print("voce fez diplomacia com um novo país")
    	niveis_iniciais.diplomacia +=1
    	escolhendo = "passou de fase"
    elif escolha_02> 5 or escolha_02< 1:
        print("Digite um valor valido")
        escolhendo ="fase01.2"
        
################################
#Editar essa parte             #
################################
 print("Agora voce pode continuar expandindo seu imperio... mas antes vamos ver o que esta acontecendo por la")
 print(evento_aleatorio())

def fase_02():
 print("inicio da fase, texto de abertura")
 
################################
#Escolha 1 da fase 2           #
################################
 escolhendo ="fase02.1"
 while escolhendo =="fase02.1":
    escolha_03= int(input("O que você quer evoluir primeiro: 1 para quartel/2 para estabulo/3 para soldados/4 para buscar diplomacia "))
    if escolha_03 == 1:
    	print("voce evoluiu o Quartel em 1")
    	niveis_iniciais.nv_quartel +=1
    	escolhendo = "passou de fase"
    elif escolha_03 == 2:
    	print("voce evoluiu o Estabulo em 1")
    	niveis_iniciais.nv_estabulo +=1
    	escolhendo = "passou de fase"
    elif escolha_03 == 3:
    	print("voce contratou mais 10 soldados")
    	niveis_iniciais.num_soldados +=10
    	escolhendo = "passou de fase"
    elif escolha_03 == 4:
    	print("voce fez diplomacia com um novo país")
    	niveis_iniciais.diplomacia +=1
    	escolhendo = "passou de fase"
    elif escolha_03> 5 or escolha_03< 1:
        print("Digite um valor valido")
        escolhendo ="fase02.1"
        
################################
#Editar essa parte             #
################################
 print("Agora voce pode continuar expandindo seu imperio... mas antes vamos ver o que esta acontecendo por la")
 print(evento_aleatorio())

################################
#Escolha 2 da fase 2           #
################################
 escolhendo ="fase02.2"
 while escolhendo =="fase02.2":
    escolha_04= int(input("O que você quer evoluir primeiro: 1 para quartel/2 para estabulo/3 para soldados/4 para buscar diplomacia "))
    if escolha_04 == 1:
    	print("voce evoluiu o Quartel em 1")
    	niveis_iniciais.nv_quartel +=1
    	escolhendo = "passou de fase"
    elif escolha_04 == 2:
    	print("voce evoluiu o Estabulo em 1")
    	niveis_iniciais.nv_estabulo +=1
    	escolhendo = "passou de fase"
    elif escolha_04 == 3:
    	print("voce contratou mais 10 soldados")
    	niveis_iniciais.num_soldados +=10
    	escolhendo = "passou de fase"
    elif escolha_04 == 4:
    	print("voce fez diplomacia com um novo país")
    	niveis_iniciais.diplomacia +=1
    	escolhendo = "passou de fase"
    elif escolha_04> 5 or escolha_04< 1:
        print("Digite um valor valido")
        escolhendo ="fase02.2"
        
################################
#Editar essa parte             #
################################
 print("Agora voce pode continuar expandindo seu imperio... mas antes vamos ver o que esta acontecendo por la")
 print(evento_aleatorio())

def fase_03():
 print("inicio da fase, texto de abertura")
 
################################
#Escolha 1 da fase 3           #
################################
 escolhendo ="fase03.1"
 while escolhendo =="fase03.1":
    escolha_05= int(input("O que você quer evoluir primeiro: 1 para quartel/2 para estabulo/3 para soldados/4 para buscar diplomacia "))
    if escolha_05 == 1:
    	print("voce evoluiu o Quartel em 1")
    	niveis_iniciais.nv_quartel +=1
    	escolhendo = "passou de fase"
    elif escolha_05 == 2:
    	print("voce evoluiu o Estabulo em 1")
    	niveis_iniciais.nv_estabulo +=1
    	escolhendo = "passou de fase"
    elif escolha_05 == 3:
    	print("voce contratou mais 10 soldados")
    	niveis_iniciais.num_soldados +=10
    	escolhendo = "passou de fase"
    elif escolha_05 == 4:
    	print("voce fez diplomacia com um novo país")
    	niveis_iniciais.diplomacia +=1
    	escolhendo = "passou de fase"
    elif escolha_05> 5 or escolha_05< 1:
        print("Digite um valor valido")
        escolhendo ="fase03.1"
        
################################
#Editar essa parte             #
################################
 print("Agora voce pode continuar expandindo seu imperio... mas antes vamos ver o que esta acontecendo por la")
 print(evento_aleatorio())

################################
#Escolha 2 da fase 3           #
################################
 escolhendo ="fase03.2"
 while escolhendo =="fase03.2":
    escolha_06= int(input("O que você quer evoluir primeiro: 1 para quartel/2 para estabulo/3 para soldados/4 para buscar diplomacia "))
    if escolha_06 == 1:
    	print("voce evoluiu o Quartel em 1")
    	niveis_iniciais.nv_quartel +=1
    	escolhendo = "passou de fase"
    elif escolha_06 == 2:
    	print("voce evoluiu o Estabulo em 1")
    	niveis_iniciais.nv_estabulo +=1
    	escolhendo = "passou de fase"
    elif escolha_06 == 3:
    	print("voce contratou mais 10 soldados")
    	niveis_iniciais.num_soldados +=10
    	escolhendo = "passou de fase"
    elif escolha_06 == 4:
    	print("voce fez diplomacia com um novo país")
    	niveis_iniciais.diplomacia +=1
    	escolhendo = "passou de fase"
    elif escolha_06> 5 or escolha_06< 1:
        print("Digite um valor valido")
        escolhendo ="fase03.2"
        
################################
#Editar essa parte             #
################################
 print("Agora voce pode continuar expandindo seu imperio... mas antes vamos ver o que esta acontecendo por la")
 print(evento_aleatorio())

def fase_04():
 print("inicio da fase, texto de abertura")
 
################################
#Escolha 1 da fase 4           #
################################
 escolhendo ="fase04.1"
 while escolhendo =="fase04.1":
    escolha_07= int(input("O que você quer evoluir primeiro: 1 para quartel/2 para estabulo/3 para soldados/4 para buscar diplomacia "))
    if escolha_07 == 1:
    	print("voce evoluiu o Quartel em 1")
    	niveis_iniciais.nv_quartel +=1
    	escolhendo = "passou de fase"
    elif escolha_07 == 2:
    	print("voce evoluiu o Estabulo em 1")
    	niveis_iniciais.nv_estabulo +=1
    	escolhendo = "passou de fase"
    elif escolha_07 == 3:
    	print("voce contratou mais 10 soldados")
    	niveis_iniciais.num_soldados +=10
    	escolhendo = "passou de fase"
    elif escolha_07 == 4:
    	print("voce fez diplomacia com um novo país")
    	niveis_iniciais.diplomacia +=1
    	escolhendo = "passou de fase"
    elif escolha_07> 5 or escolha_07< 1:
        print("Digite um valor valido")
        escolhendo ="fase04.1"
        
################################
#Editar essa parte             #
################################
 print("Agora voce pode continuar expandindo seu imperio... mas antes vamos ver o que esta acontecendo por la")
 print(evento_aleatorio())

################################
#Escolha 2 da fase 4           #
################################
 escolhendo ="fase04.2"
 while escolhendo =="fase04.2":
    escolha_08= int(input("O que você quer evoluir primeiro: 1 para quartel/2 para estabulo/3 para soldados/4 para buscar diplomacia "))
    if escolha_08 == 1:
    	print("voce evoluiu o Quartel em 1")
    	niveis_iniciais.nv_quartel +=1
    	escolhendo = "passou de fase"
    elif escolha_08 == 2:
    	print("voce evoluiu o Estabulo em 1")
    	niveis_iniciais.nv_estabulo +=1
    	escolhendo = "passou de fase"
    elif escolha_08 == 3:
    	print("voce contratou mais 10 soldados")
    	niveis_iniciais.num_soldados +=10
    	escolhendo = "passou de fase"
    elif escolha_08 == 4:
    	print("voce fez diplomacia com um novo país")
    	niveis_iniciais.diplomacia +=1
    	escolhendo = "passou de fase"
    elif escolha_08> 5 or escolha_08< 1:
        print("Digite um valor valido")
        escolhendo ="fase04.2"
        
################################
#Editar essa parte             #
################################
 print("Agora voce pode continuar expandindo seu imperio... mas antes vamos ver o que esta acontecendo por la")
 print(evento_aleatorio())

def fase_05():
 print("inicio da fase, texto de abertura")
 
################################
#Escolha 1 da fase 5           #
################################
 escolhendo ="fase05.1"
 while escolhendo =="fase05.1":
    escolha_09= int(input("O que você quer evoluir primeiro: 1 para quartel/2 para estabulo/3 para soldados/4 para buscar diplomacia "))
    if escolha_09 == 1:
    	print("voce evoluiu o Quartel em 1")
    	niveis_iniciais.nv_quartel +=1
    	escolhendo = "passou de fase"
    elif escolha_09 == 2:
    	print("voce evoluiu o Estabulo em 1")
    	niveis_iniciais.nv_estabulo +=1
    	escolhendo = "passou de fase"
    elif escolha_09 == 3:
    	print("voce contratou mais 10 soldados")
    	niveis_iniciais.num_soldados +=10
    	escolhendo = "passou de fase"
    elif escolha_09 == 4:
    	print("voce fez diplomacia com um novo país")
    	niveis_iniciais.diplomacia +=1
    	escolhendo = "passou de fase"
    elif escolha_09> 5 or escolha_09< 1:
        print("Digite um valor valido")
        escolhendo ="fase05.1"
        
################################
#Editar essa parte             #
################################
 print("Agora voce pode continuar expandindo seu imperio... mas antes vamos ver o que esta acontecendo por la")
 print(evento_aleatorio())

################################
#Escolha 2 da fase 5           #
################################
 escolhendo ="fase05.2"
 while escolhendo =="fase05.2":
    escolha_10= int(input("O que você quer evoluir primeiro: 1 para quartel/2 para estabulo/3 para soldados/4 para buscar diplomacia "))
    if escolha_10 == 1:
    	print("voce evoluiu o Quartel em 1")
    	niveis_iniciais.nv_quartel +=1
    	escolhendo = "passou de fase"
    elif escolha_10 == 2:
    	print("voce evoluiu o Estabulo em 1")
    	niveis_iniciais.nv_estabulo +=1
    	escolhendo = "passou de fase"
    elif escolha_10 == 3:
    	print("voce contratou mais 10 soldados")
    	niveis_iniciais.num_soldados +=10
    	escolhendo = "passou de fase"
    elif escolha_10 == 4:
    	print("voce fez diplomacia com um novo país")
    	niveis_iniciais.diplomacia +=1
    	escolhendo = "passou de fase"
    elif escolha_10> 5 or escolha_10< 1:
        print("Digite um valor valido")
        escolhendo ="fase05.2"
        
################################
#Editar essa parte             #
################################
 print("Agora voce pode continuar expandindo seu imperio... mas antes vamos ver o que esta acontecendo por la")
 print(evento_aleatorio())

def fase_final():
 print("inicio da fase, texto de abertura")
 
################################
#Escolha 1 da fase final       #
################################
 escolhendo ="fasefinal.1"
 while escolhendo =="fasefinal.1":
    escolha_11= int(input("O que você quer evoluir primeiro: 1 para quartel/2 para estabulo/3 para soldados/4 para buscar diplomacia "))
    if escolha_11 == 1:
    	print("voce evoluiu o Quartel em 1")
    	niveis_iniciais.nv_quartel +=1
    	escolhendo = "passou de fase"
    elif escolha_11 == 2:
    	print("voce evoluiu o Estabulo em 1")
    	niveis_iniciais.nv_estabulo +=1
    	escolhendo = "passou de fase"
    elif escolha_11 == 3:
    	print("voce contratou mais 10 soldados")
    	niveis_iniciais.num_soldados +=10
    	escolhendo = "passou de fase"
    elif escolha_11 == 4:
    	print("voce fez diplomacia com um novo país")
    	niveis_iniciais.diplomacia +=1
    	escolhendo = "passou de fase"
    elif escolha_11> 5 or escolha_11< 1:
        print("Digite um valor valido")
        escolhendo ="fasefinal.1"
        
################################
#Editar essa parte             #
################################
 print("Agora voce pode continuar expandindo seu imperio... mas antes vamos ver o que esta acontecendo por la")
 print(evento_aleatorio())
 
################################
#Escolha 2 da fase final       #
################################
 escolhendo ="fasefinal.2"
 while escolhendo =="fasefinal.2":
    escolha_12= int(input("O que você quer evoluir primeiro: 1 para quartel/2 para estabulo/3 para soldados/4 para buscar diplomacia "))
    if escolha_12 == 1:
    	print("voce evoluiu o Quartel em 1")
    	niveis_iniciais.nv_quartel +=1
    	escolhendo = "passou de fase"
    elif escolha_12 == 2:
    	print("voce evoluiu o Estabulo em 1")
    	niveis_iniciais.nv_estabulo +=1
    	escolhendo = "passou de fase"
    elif escolha_12 == 3:
    	print("voce contratou mais 10 soldados")
    	niveis_iniciais.num_soldados +=10
    	escolhendo = "passou de fase"
    elif escolha_12 == 4:
    	print("voce fez diplomacia com um novo país")
    	niveis_iniciais.diplomacia +=1
    	escolhendo = "passou de fase"
    elif escolha_12> 5 or escolha_12< 1:
        print("Digite um valor valido")
        escolhendo ="fasefinal.2"
        
################################
#Editar essa parte             #
################################
 print("Agora voce pode continuar expandindo seu imperio... mas antes vamos ver o que esta acontecendo por la")
 print(evento_aleatorio())
 print(niveis_iniciais.nv_quartel)
 print(niveis_iniciais.nv_estabulo)
 print(niveis_iniciais.num_soldados)
 print(niveis_iniciais.diplomacia)


