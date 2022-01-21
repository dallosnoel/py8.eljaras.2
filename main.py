'''
2. Feladat
Írj eljárást, amely paraméterül kapott számról eldönti, és a képernyőre kiírja, hogy negatív, pozitív vagy nulla-e!
'''
def milyen(szam):
  if szam == 0:
    print(f"A szám 0")
  if szam > 0:
    print(f"A szám pozitív")
  if szam < 0:
    print(f"A szám negatív")

