from portofoliudeinvestitii import PortofoliuInvestitii
portofoliu = PortofoliuInvestitii("mihai", "CRI123")
portofoliu.inregistreaza_tranzactie("CRI123", 1, "BUY", 2000)
portofoliu.inregistreaza_tranzactie("CRI123", 1, "SELL", 500)
portofoliu.inregistreaza_tranzactie("CRI123", 2, "BUY", 1800)
portofoliu.inregistreaza_tranzactie("CRI123", 2, "SELL", 200)
portofoliu.inregistreaza_tranzactie("CRI123", 3, "BUY", 100)
portofoliu.inregistreaza_tranzactie("CRI123", 3, "SELL", 200)
portofoliu.inregistreaza_tranzactie("CRI123", 4, "BUY", 400)
portofoliu.inregistreaza_tranzactie("CRI123", 4, "SELL", 1500)
portofoliu.inregistreaza_tranzactie("CRI123", 5, "BUY", 1300)
portofoliu.inregistreaza_tranzactie("CRI123", 5, "SELL", 300)
portofoliu.inregistreaza_tranzactie("CRI123", 6, "BUY", 1000)
portofoliu.inregistreaza_tranzactie("CRI123", 6, "SELL", 2000)
portofoliu.inregistreaza_tranzactie("CRI123", 7, "BUY", 900)
portofoliu.inregistreaza_tranzactie("CRI123", 7, "SELL", 300)
portofoliu.inregistreaza_tranzactie("CRI123", 8, "BUY", 400)
portofoliu.inregistreaza_tranzactie("CRI123", 8, "SELL", 500)
portofoliu.inregistreaza_tranzactie("CRI123", 9, "BUY", 500)
portofoliu.inregistreaza_tranzactie("CRI123", 9, "SELL", 600)
portofoliu.inregistreaza_tranzactie("CRI123", 10, "BUY", 400)
portofoliu.inregistreaza_tranzactie("CRI123", 10, "SELL", 500)
portofoliu.inregistreaza_tranzactie("CRI123", 11, "BUY", 300)
portofoliu.inregistreaza_tranzactie("CRI123", 11, "SELL", 100)
portofoliu.inregistreaza_tranzactie("CRI123", 12, "BUY", 200)
portofoliu.inregistreaza_tranzactie("CRI123", 12, "SELL", 500)


portofoliu.afisare()
df = portofoliu.df_lunar()
print(df)

df_stat = portofoliu.statistici_profit()
print(df_stat)



portofoliu.ploteaza_tranzactii()


statistici = portofoliu.statistici_profit()
print(statistici)