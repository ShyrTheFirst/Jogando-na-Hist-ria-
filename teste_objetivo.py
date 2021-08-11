import random
import niveis_iniciais

termos_de_guerra = ("Evoluir quarteis", "Evoluir estabulo", "Diplomacia", "Treinar mais soldados")
objetivo = random.choice(termos_de_guerra)
print("Você deve - ", objetivo)
aceitar_destino = input("Você aceita seu destino? (S/N):")
if aceitar_destino == "S":
 print("Vamos começar!")
 iniciar_jogo = True
 iniciar_objetivo = False
else:
 print("Volte quando estiver pronto")
 iniciar_jogo = False
 iniciar_objetivo = False
################################
# Teste do Objetivo            #
################################
def testar_objetivo():
 if objetivo == "Evoluir quarteis":
    if niveis_iniciais.nv_quartel == 2:
        print("muito bom!")
    else:
        print("Você ainda precisa evoluir mais!")
 elif objetivo == "Evoluir estabulo":
    if niveis_iniciais.nv_estabulo == 2:
        print("muito bom!")
    else:
        print("Você ainda precisa evoluir mais!")
 elif objetivo == "Treinar Mais soldados":
    if niveis_iniciais.num_soldados == 20:
        print("muito bom!")
    else:
        print("Você ainda precisa evoluir mais!")
 elif objetivo == "Diplomacia":
    if niveis_iniciais.diplomacia == 2:
        print("muito bom!")
    else:
        print("Você não conquistou o titulo de diplomata ainda! Conheça mais povos")

  
