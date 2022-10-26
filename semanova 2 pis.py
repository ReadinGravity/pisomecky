#vztvorte funciu vypis kt ma 1 vstupny parameter retazec string, vypise pre kazdy zna retayce 4 udaje
#(porad cislo, ordinalnu hodntou, samotny ynak, znak kt nasleduje za nim)

def vypis(word:str):
    porad=0
    ordhod=ord(word[0])
    znak=word[0]
    znak2=chr(ordhod+1)
    print(porad, ordhod, znak, znak2)

vypis ("Ahoj")
vypis("dudo")
