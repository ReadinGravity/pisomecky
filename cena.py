cena=float(input("Zadaj mi cenu: "))
kus=float(input("zadaj kusy: "))

print ("cena je: ", cena*kus, end="€ ")
print ("dph je: ", cena*kus/20, end="€ ")
print ("cena bez dph je: ", (cena*kus)-(cena*kus/20), end="€ ")

price=cena*kus
