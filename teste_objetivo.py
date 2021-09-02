import random
import config
import niveis_iniciais as nv
import easygui as box

nivel_objetivo_quartel = random.randint(2,6)
evoluirquartel = "evoluir quarteis em %s" %nivel_objetivo_quartel
nivel_objetivo_estabulo = random.randint(2,6)
evoluirestabulo = "evoluir estabulo em %s" %nivel_objetivo_estabulo
nivel_objetivo_expandir = random.randint(3,7)
expandirx = "expandir as suas ligações em %s" %nivel_objetivo_expandir
nivel_objetivo_treinar = random.randint(10,50)
treinarx = "Treinar %s soldados" %nivel_objetivo_treinar
termos_de_guerra = (evoluirquartel, evoluirestabulo, expandirx, treinarx)
objetivo = random.choice(termos_de_guerra)
aceitar_destino = box.ynbox("Seu objetivo é: %s. Você deve realizar o seu objetivo dentro de %s turnos para conquistar vantagens estratégicas. Aceita seu Destino?" %(objetivo, nv.turnos_aleatorios), "Aceitar o seu Destino", ("Sim", "Não"))


if aceitar_destino == True:
 iniciar_jogo = True
 iniciar_objetivo = False
else:
 box.msgbox("A escolha e toda sua. Até a próxima!", "Saindo")
 iniciar_jogo = False
 iniciar_objetivo = False
################################
# Teste do Objetivo            #
################################
def testar_objetivo():
 
 if objetivo == "Evoluir quarteis":
    if nv.nv_quartel == nivel_objetivo_quartel:
        box.msgbox("Você alcançou o objetivo, por isso irá ganhar uma recompensa!")
        #criar recompensa
    else:
        box.msgbox("Você não alcançou o objetivo, infelizmente não receberá uma recompensa")
 elif objetivo == "Evoluir estabulo":
    if nv.nv_estabulo == nivel_objetivo_estabulo:
        box.msgbox("Você alcançou o objetivo, por isso irá ganhar uma recompensa!")
        #criar recompensa
    else:
        box.msgbox("Você não alcançou o objetivo, infelizmente não receberá uma recompensa")
 elif objetivo == "Treinar Mais soldados":
    if nv.num_soldados == nivel_objetivo_treinar:
        box.msgbox("Você alcançou o objetivo, por isso irá ganhar uma recompensa!")
        #criar recompensa
    else:
        box.msgbox("Você não alcançou o objetivo, infelizmente não receberá uma recompensa")
 elif objetivo == "Diplomacia":
    if nv.diplomacia == nivel_objetivo_expandir:
        box.msgbox("Você alcançou o objetivo, por isso irá ganhar uma recompensa!")
        #criar recompensa
    else:
        box.msgbox("Você não alcançou o objetivo, infelizmente não receberá uma recompensa")
