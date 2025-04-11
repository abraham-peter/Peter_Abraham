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
copie_bancnote=bancnote
registru_clienti={}
import random
def calculare_rest_dinamic(rest):
  dp=[rest+1]*(rest+1)
  dp[0]=0
  for amount in range(1,rest+1):
      for bancnota in bancnote:
          if amount-bancnota["valoare"]>=0:
              dp[amount]=min(dp[amount],1+dp[amount-bancnota["valoare"]])
              bancnota["stoc"]-=1
  for bancnota,copie_bancnota in zip(bancnote,copie_bancnote):
      diferenta=copie_bancnota["stoc"]-bancnota["stoc"]-1
      if diferenta>0:
          print(f"Numarul de bancnote folosite din  {bancnota['valoare']} este {diferenta}")
  if dp[amount]!=rest+1:
      return dp[amount]
  
import random
if __name__ == "__main__":
    while(True):
        print("Inturduceti numele clientului:")
        nume_client=input()
        print("Intrduceti suma platita:")
        suma_platita=int(input())
        rest=calculare_rest_dinamic(suma_platita)
        if rest<0:
            print("Nu avem suficiente bani")
        elif rest==0:
            print("Nu este rest de dat")
        print(nume_client,suma_platita,rest)
    # rest=suma_platita-produse[0]["pret"]#30-7=23
    # rest=
    # print(rest)
    # if(rest<0):
    #     print("Nu avem suficiente bani")
    # elif(rest==0):
    #     print("Nu este rest de dat")
    # else:
    #     print(calculare_rest_dinamic(rest))
    
    


