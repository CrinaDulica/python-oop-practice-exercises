def creare_persoana(nume, varsta):
    return {
        "nume" : nume,
        "varsta" : varsta
    }
def afisare_persoana(dict):
    #print(f"{dict['nume']} are varsta" f"{dict['varsta']}")
    print(dict['nume'] , 'are varsta' , dict['varsta'])

def varsta_medie_toate_persoanele(dict):
    suma_varsta = 0
    for persoana in dict:
        suma_varsta += persoana["varsta"]
    nr_persoane = len(dict)
    medie = suma_varsta/nr_persoane
    return medie



