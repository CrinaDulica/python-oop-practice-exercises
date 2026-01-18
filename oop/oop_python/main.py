from pers import *

pers1 = creare_persoana("Andreea",19)
afisare_persoana(pers1)

#------------------------------------------------------------------
dictionar_persoane = []
persoana2 = creare_persoana("Iuliana", 15)
persoana3 = creare_persoana("Denisa", 22)
persoana4 = creare_persoana("Marius", 24)
persoana5 = creare_persoana("Mihai", 22)
persoana6 = creare_persoana("Edi",20 )
persoana7 = creare_persoana("Cristian", 25)
dictionar_persoane.append(persoana2)
dictionar_persoane.append(persoana3)
dictionar_persoane.append(persoana4)
dictionar_persoane.append(persoana5)
dictionar_persoane.append(persoana6)
dictionar_persoane.append(persoana7)

print(dictionar_persoane)

print("Media varstei: ", varsta_medie_toate_persoanele(dictionar_persoane), " ani")