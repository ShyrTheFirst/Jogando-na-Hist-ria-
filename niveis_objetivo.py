import random
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


