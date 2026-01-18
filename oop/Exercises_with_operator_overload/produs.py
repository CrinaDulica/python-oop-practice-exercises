class Produs:
    class Review:
        def __init__(self, autor: str, nota: float):
            self.autor = autor
            self.nota = float(nota)
    def __init__(self, nume: str, pret: float):
        self.nume = nume
        self.pret = float(pret)
        self.reviewuri = []

    def __str__(self):
        return f"{self.autor}: {self.nota}"
    def adauga_review(self, autor: str, nota: float):
        self.reviewuri.append(Produs.Review(autor, nota))
    def rating(self):
        if not self.reviewuri:
            return 0
        total = sum(float(r.nota) for r in self.reviewuri)
        return round(total / len(self.reviewuri), 2)

    def __str__(self):
        return f"{self.nume} , Pret: {self.pret} , Rating: {self.rating()}"

    def __eq__(self, other):
        return self.nume == other.nume
        return self.pret == other.pret
    def __ne__(self, other):
        return not self.__eq__(other)
    def __lt__(self, other):
        return self.rating() < other.rating()
    def __le__(self, other):
        return self.rating() <= other.rating()
    def __gt__(self, other):
        return self.rating() > other.rating()
    def __ge__(self, other):
        return self.rating() >= other.rating()
    def __add__(self, other):
        if not isinstance(other,Produs):
            return NotImplemented
        nume_nou = f"{self.nume} & {other.nume}"
        pachet = Produs(nume_nou, self.pret + other.pret)
        pachet.reviewuri = self.reviewuri + other.reviewuri
        return pachet

    def afisare_review(self):
        print(f"Review-urile pentru {self.nume}:")
        for r in self.reviewuri:
            print(f" {r.autor}: {r.nota}")

    def __iadd__(self, other):
        autor, nota = other
        self.adauga_review(autor, nota)
        return self
    def __mul__(self, other):
        produs_nou = Produs(self.nume, self.pret)
        produs_nou.reviewuri = self.reviewuri.copy()
        return produs_nou
    def __sub__(self, other):
        produs_copie = Produs(self.nume, self.pret)
        for n in self.reviewuri:
            if n.autor != other:
                produs_copie.reviewuri.append(Produs.Review(n.autor, n.nota))
        return produs_copie
    def __getitem__(self, item):
        return self.reviewuri[item]
    def __setitem__(self, key, value):
        self.reviewuri[key].nota = value
    def __contains__(self, item):
        return any(n.autor == item for n in self.reviewuri)
    def __len__(self):
        return len(self.reviewuri)
    def __call__(self):
        return self.rating()
    def __bool__(self):
        return bool(self.reviewuri)
    def __and__(self, other):
       autori_self = {n.autor for n in self.reviewuri}
       autori_other = {n.autor for n in other.reviewuri}
       return autori_self
       return autori_other
    def __or__(self, other):
        produs_nou = Produs(f"{self.nume} | {other.nume}", max(self.pret, other.pret))
        dict_note = {}

        for n in self.reviewuri + other.reviewuri:
            nota = float(n.nota)
            dict_note[n.autor] = max(dict_note.get(n.autor, 0), n.nota)

        for autor, nota in dict_note.items():
            produs_nou.adauga_review(autor, nota)

        return produs_nou
    def __radd__(self, other):
        return other + self.rating()


    def __iter__(self):
        for n in self.reviewuri:
            yield (n.autor, n.nota)




















