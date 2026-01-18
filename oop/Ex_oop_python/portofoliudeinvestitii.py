from typing import Dict, List, Tuple
import pandas as pd# pandas e pt a lucra cu tabele in excel, baze de date etc
import matplotlib.pyplot as plot
import statistics as stats

class PortofoliuInvestitii:
    nume_titular: str
    tranzactii: Dict[int, List[Tuple[str,float]]]
    __cod_portofoliu: str

    def __init__(self, nume_titular: str, cod_portofoliu: str):
        self.nume_titular = nume_titular
        self.__cod_portofoliu = cod_portofoliu
        self.tranzactii = {luna: [] for luna in range (1,13)}

    def __str__(self):
        return f"{self.nume_titular} are portofoliul cu codul {self.__cod_portofoliu}."

    def verifica_cod(self, cod_introdus: str) -> bool:
        if cod_introdus == self.__cod_portofoliu:
            return True
        else:
            return False

    def schimba_cod(self, cod_vechi: str, cod_nou: str) -> None:
        if cod_vechi == self.__cod_portofoliu:
            print(f"codul portofoliului a fost actualizat")
        else:
            print(f"codul nu a fost actualizat")

    def inregistreaza_tranzactie(self, cod: str, luna: int, tip: str, suma: float) -> None:
        if cod != self.__cod_portofoliu:
            print(f"Tranzactia nu a fost inregsitrata")
        #else:
            #print(f"tranzactia continua")
        if tip not in ("BUY", "SELL"):
            print(f"tipul tranzactiei trebuie sa fie 'BUY' sau 'SELL'.")
            return
        self.tranzactii[luna].append((tip, suma))
        print(f"Tranzacția ({tip}, {suma}) a fost înregistrată pentru luna {luna}.")
    def afisare(self):
        print(self.__str__())

    def df_lunar(self) -> pd.DataFrame:
        rows = []
        for luna in range(1, 13):
            BUY = sum(s for tip, s in self.tranzactii[luna] if tip == "BUY")
            SELL = sum(s for tip, s in self.tranzactii[luna] if tip == "SELL")
            net = SELL-BUY
            rows.append({  # adauga un rand in dictionar
                "luna": luna,
                "BUY": BUY,
                "SELL": SELL,
                "net": net

            })
        return pd.DataFrame(rows)

    def statistici_profit(self) -> dict:
        input = self.df_lunar()
        profit_total = input["net"].sum()
        profit_mediu_lunar = input["net"].mean()
        luna_max_profit = input.loc[input["net"].idxmax(), "luna"] if (input["net"] > 0).any() else None
        output = pd.DataFrame(
            {
                "indicator": [
                "profit_total",
                "profit_mediu_lunar",
                "luna_max_profit"
                ],
                "valori": [
                profit_total,
                profit_mediu_lunar,
                luna_max_profit
                ]
            }
        )
        return output

    def ploteaza_tranzactii(self) -> None:
        df = self.df_lunar()
        luni = df["luna"].tolist()
        BUY = df["BUY"].tolist()
        SELL = df["SELL"].tolist()

        latime = 0.4
        x = df.index

        plot.figure(figsize=(10, 5))

        plot.bar(x - latime / 2, BUY, latime, label="BUY")
        plot.bar(x + latime / 2, SELL, latime, label="SELL")

        plot.xticks(x, [str(l) for l in luni])

        plot.xlabel("luni")
        plot.ylabel("suma (ron)")

        plot.legend()

        plot.title(f"Tranzactii portofoliu - {self.nume_titular}")

        plot.tight_layout()

        plot.show()



















