import random
import config
import niveis_iniciais as nv
import niveis_objetivo as obj
import easygui as box

################################
# Iniciar o Objetivo           #
################################
def iniciar_objetivo():
 obj.nivel_objetivo_quartel = random.randint(2,6)
 obj.evoluirquartel = "evoluir quarteis em %s" %obj.nivel_objetivo_quartel
 obj.nivel_objetivo_estabulo = random.randint(2,6)
 obj.evoluirestabulo = "evoluir estabulo em %s" %obj.nivel_objetivo_estabulo
 obj.nivel_objetivo_expandir = random.randint(3,7)
 obj.expandirx = "expandir as suas ligações em %s" %obj.nivel_objetivo_expandir
 obj.nivel_objetivo_treinar = random.randint(10,50)
 obj.treinarx = "Treinar %s soldados" %obj.nivel_objetivo_treinar
 obj.termos_de_guerra = (obj.evoluirquartel, obj.evoluirestabulo, obj.expandirx, obj.treinarx)
 print(obj.termos_de_guerra)
 obj.objetivo = random.choice(obj.termos_de_guerra)
 print(obj.objetivo)
 aceitar_destino = box.ynbox("Seu objetivo é: %s. Você deve realizar o seu objetivo dentro de %s turnos para conquistar vantagens estratégicas. Aceita seu Destino?" %(obj.objetivo, nv.turnos_aleatorios), "Aceitar o seu Destino", ("Sim", "Não"))
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
 
 if obj.objetivo == obj.evoluirquartel:
    if nv.nv_quartel == obj.nivel_objetivo_quartel:
        box.msgbox("Você alcançou o objetivo, por isso irá ganhar uma recompensa!")
        #criar recompensa
    else:
        box.msgbox("Você não alcançou o objetivo, infelizmente não receberá uma recompensa, o seu nivel: %s , o nivel necessário %s" %(nv.nv_quartel, obj.nivel_objetivo_quartel))
 if obj.objetivo == obj.evoluirestabulo:
    if nv.nv_estabulo == obj.nivel_objetivo_estabulo:
        box.msgbox("Você alcançou o objetivo, por isso irá ganhar uma recompensa!")
        #criar recompensa
    else:
        box.msgbox("Você não alcançou o objetivo, infelizmente não receberá uma recompensa o seu nivel: %s , o nivel necessário %s" %(nv.nv_estabulo, obj.nivel_objetivo_estabulo))
 if obj.objetivo == obj.treinarx:
    if nv.num_soldados == obj.nivel_objetivo_treinar:
        box.msgbox("Você alcançou o objetivo, por isso irá ganhar uma recompensa!")
        #criar recompensa
    else:
        box.msgbox("Você não alcançou o objetivo, infelizmente não receberá uma recompensa o seu nivel: %s , o nivel necessário %s" %(nv.num_soldados, obj.nivel_objetivo_treinar))
 if obj.objetivo == obj.expandirx:
    if nv.diplomacia == obj.nivel_objetivo_expandir:
        box.msgbox("Você alcançou o objetivo, por isso irá ganhar uma recompensa!")
        #criar recompensa
    else:
        box.msgbox("Você não alcançou o objetivo, infelizmente não receberá uma recompensa o seu nivel: %s , o nivel necessário %s" %(nv.diplomacia, obj.nivel_objetivo_expandir))
