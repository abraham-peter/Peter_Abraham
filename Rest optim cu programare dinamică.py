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
  dp=[rest+1]*(rest+1)
  dp[0]=0
  for amount in range(1,rest+1):
      for bancnota in bancnote:
          if amount-bancnota["valoare"]>=0:
              dp[amount]=min(dp[amount],1+dp[amount-bancnota["valoare"]])
              bancnota["stoc"]-=1
  if dp[amount]!=rest+1:
      return dp[amount]
import random
if __name__ == "__main__":
    while(True):
        print("Inturduceti numele produsului:")
        nume_produs=input()
        print("Intrduceti suma platita:")
        suma_platita=int(input())
        for i in range(5):
            if produse[i]["nume"]==nume_produs:
                stoc_ramas=bancnote[i]["stoc"]-1
                bancnote[i]["stoc"]=stoc_ramas
                if stoc_ramas<0:
                    print("Nu avem suficiente produse")
                    break
                rest=suma_platita-produse[i]["pret"]
                break
                

        print("Restul este:",rest)
        min_bancnote=calculare_rest_dinamic(rest)
        if rest<0:
            print("Nu avem suficiente bani")
        elif rest==0:
            print("Nu este rest de dat")
        print(nume_produs,suma_platita,rest,min_bancnote,stoc_ramas)
        
    


