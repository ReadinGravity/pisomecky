def spracuj_riadok(riadok):
    riadok=riadok[:-1]
    vysledok=""
    count=0
    coun=0
    for char in riadok:
        if char=="0":
            count+=1

        if char=="1":
            coun+=1
    return vysledok+str(count)+" "

with open("kompresia_obrazka_1.txt", 'r', encoding="UTF-8") as citanie, open("kompresia_obrazka_vystup.txt", 'w', encoding="UTF-8") as pisanie:
    rozmery=citanie.readline()
    obrazok=citanie.readlines()

    pisanie.write(rozmery)
    for line in obrazok:
        pisanie.write(spracuj_riadok(line)+'\n')

