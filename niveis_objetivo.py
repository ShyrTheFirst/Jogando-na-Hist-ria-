import random
nivel_objetivo_quartel = 0
evoluirquartel = "evoluir quarteis em %s" %nivel_objetivo_quartel
nivel_objetivo_estabulo = 0
evoluirestabulo = "evoluir estabulo em %s" %nivel_objetivo_estabulo
nivel_objetivo_expandir = 0
expandirx = "expandir as suas ligações em %s" %nivel_objetivo_expandir
nivel_objetivo_treinar = 0
treinarx = "Treinar %s soldados" %nivel_objetivo_treinar
termos_de_guerra = (evoluirquartel, evoluirestabulo, expandirx, treinarx)
objetivo = random.choice(termos_de_guerra)



