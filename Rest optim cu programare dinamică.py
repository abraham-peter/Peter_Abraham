bancnote=[{"valoare": 50, "stoc": 20},
     {"valoare": 20, "stoc": 1 },
     {"valoare": 10, "stoc": 40 },
     {"valoare": 5, "stoc": 50 },
     {"valoare": 1, "stoc": 100}]
produse= [
    { "nume": "Lapte", "pret": 7 },
    { "nume": "Paine", "pret": 3 },
    { "nume": "Ciocolata", "pret": 5 },
    { "nume": "Apa", "pret": 2 },
    { "nume": "Cafea", "pret": 9 }
  ]
import random
     
def calculare_rest_dinamic(rest):
    dp = [(rest+1)] * (rest + 1)
    dp[0] = 0
    bancnote_folosite = [[] for _ in range(rest + 1)]
    bancnote_sortate = sorted(bancnote, key=lambda x: x["valoare"], reverse=True)
    
    for amount in range(1, rest + 1):
        for bancnota in bancnote_sortate:
            valoare = bancnota["valoare"]
            if amount >= valoare and bancnota["stoc"] > 0 and dp[amount - valoare] != (rest + 1):
             
                if dp[amount] > 1 + dp[amount - valoare]:
                    dp[amount] = 1 + dp[amount - valoare]
                    bancnote_folosite[amount] = bancnote_folosite[amount - valoare].copy()
                    bancnote_folosite[amount].append(valoare)
    
    if dp[rest] == (rest + 1):
        return None, []
    
    
    bancnote_rezultat = {}
    for valoare in bancnote_folosite[rest]:
        if valoare in bancnote_rezultat:
            bancnote_rezultat[valoare] += 1
        else:
            bancnote_rezultat[valoare] = 1
        
        for b in bancnote:
            if b["valoare"] == valoare:
                b["stoc"] -= 1
                break
    
    return dp[rest], bancnote_rezultat

import random
if __name__ == "__main__":
    while(True):
        print("Inturduceti numele produsului:")
        nume_produs=input()
        print("Intrduceti suma platita:")
        suma_platita=int(input())
        rest = 0
        stoc_ramas = 0
        produs_gasit = False
        
        for i in range(len(produse)):
            if produse[i]["nume"]==nume_produs:
                produs_gasit = True
                rest=suma_platita-produse[i]["pret"]
                break
        
        if not produs_gasit:
            print("Produsul nu a fost găsit!")
            continue
                
        print("Restul este:", rest)
        
        if rest < 0:
            print("Suma plătită este insuficientă!")
            continue
        elif rest == 0:
            print("Nu este rest de dat")
            continue
        
        min_bancnote, bancnote_folosite = calculare_rest_dinamic(rest)
        
        if min_bancnote is None:
            print("Nu avem suficiente bancnote pentru a da rest!")
        else:
            print(f"Numărul minim de bancnote necesare: {min_bancnote}")
            print("Bancnote folosite:")
            for valoare, numar in sorted(bancnote_folosite.items(), reverse=True):
                print(f"  - {numar} bancnote de {valoare}")
        
        print(f"Produs: {nume_produs}, Suma plătită: {suma_platita}, Rest: {rest}")
