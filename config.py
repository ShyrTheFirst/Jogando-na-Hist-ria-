import random

#CORRIGIR NÃO MUDANÇA DOS NIVEIS
#TALVEZ CRIAR UM OUTRO .py PARA ALTERAR OS NIVEIS


################################
# Niveis iniciais              #
################################
nv_quartel = 0
nv_estabulo = 0
num_soldados = 0
diplomacia = 0
################################
#Definições das fases          #
################################
def evento_aleatorio():
    lista_evento = ("ataque inesperado", "fome entre os servos", "doenças infecciosas")
    evento_escolhido = random.choice(lista_evento)
    return evento_escolhido
    
def fase_01():
    print("inicio da fase, texto de abertura")
    escolha_01= input("O que você quer evoluir primeiro: 1 para quartel/2 para estabulo/3 para soldados/4 para buscar diplomacia ")
    if escolha_01 == 1:
    	print("voce evoluiu o Quartel em 1")
    	nv_quartel = nv_quartel + 1
    elif escolha_01 == 2:
    	print("voce evoluiu o Estabulo em 1")
    	config.nv_estabulo = config.nv_estabulo + 1
    elif escolha_01 == 3:
    	print("voce contratou mais 10 soldados")
    	config.num_soldados = config.num_soldados + 1
    elif escolha_01 == 4:
    	print("voce fez diplomacia com um novo país")
    	config.diplomacia = config.diplomacia + 1
    elif int(escolha_01) > 5 or int(escolha_01) < 1:
    	escolha_01 = input ("digite um valor valido (1 , 2 , 3 ou 4 ")
    print("Agora voce pode continuar expandindo seu imperio... mas antes vamos ver o que esta acontecendo por la")
    print(evento_aleatorio())
    
    #pode escolher mais uma vez uma das opções.


