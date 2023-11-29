def spracuj_riadok(riadok):
    riadok = riadok[:-1]
    vysledok = ""
    counter = 0
    char = '0'

    for i in range(len(riadok)):
        if riadok[i] == char:
            counter += 1
        else:
            vysledok += str(counter) + ' '
            counter = 1 if riadok[i] == '1' else 0
            char = riadok[i]

    vysledok += str(counter) + ' '
    return vysledok

with open("kompresia_obrazka_1.txt", 'r', encoding="UTF-8") as citanie, open("kompresia_obrazka_vystup.txt", 'w', encoding="UTF-8") as pisanie:
    rozmery = citanie.readline()
    obrazok = citanie.readlines()

    pisanie.write(rozmery)
    for line in obrazok:
        pisanie.write(spracuj_riadok(line) + '\n')
