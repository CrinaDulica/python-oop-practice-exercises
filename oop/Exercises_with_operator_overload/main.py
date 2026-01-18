from produs import Produs
p1 = Produs("Casti", "400")
p1.adauga_review("Crina","10")
p1.adauga_review("Denisa","8")
p1.adauga_review("Matias","5")
p1.adauga_review("Mihai","4")
p1.adauga_review("Edi","10")
p1.adauga_review("Dan","9")
p1.adauga_review("Dana","6")

p2 = Produs("Frigider","5000")
p2.adauga_review("Maria","10")
p2.adauga_review("Alexandra","10")
p2.adauga_review("Manuela","10")
p2.adauga_review("Flavius","8")
p2.adauga_review("Cristian","10")
p2.adauga_review("Geta","7")
p2.adauga_review("Cornel","9")

p3=Produs("Telefon","4000")
p3.adauga_review("Ana","10")
p3.adauga_review("Marius","6")
p3.adauga_review("Claudia","2")
p3.adauga_review("Eric","4")
p3.adauga_review("Anastasia","6")
p3.adauga_review("Sofia","10")
p3.adauga_review("Narcis","10")
print(p1)
print(p2)
print(p3)

print(p1 == p2)
print(p2 != p3)
print(p1 < p2)
print(p3 >= p1)

print("nr review.uri: ")
print(len(p1))
print(len(p2))
print(len(p3))

print("verificam autorul: ")
print("Crina" in p1)
print("Crina" in p2)


print(p1())
print(p2())

print(p1())
pachet = p1 + p2
print(pachet)
pachet.afisare_review()

p1 += ("Alex", 7)
p1.afisare_review()

print("Review p3[0]:", p3[0].autor, p3[0].nota)
p3[0] = 7
print("Dupa modificare:", p3[0].autor, p3[0].nota)

p1_marire_pret = p2 * 1.1
print(p1.afisare_review())
p1_marire_pret.afisare_review()

p2_fara_Maria = p2 - "Maria"
print(p2_fara_Maria.afisare_review())

print(p1 & p2)

produs_nou = p1 | p3
print(produs_nou)
produs_nou.afisare_review()

print("----------")

lprod = [p1, p2, p3]
total = sum(lprod)
medie = total / len(lprod)
print(round(medie, 2))

print("----------")

for autor, nota in p1:
    print(autor, nota)








