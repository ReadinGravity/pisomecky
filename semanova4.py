#napiste funkciu kt vstup parametrom huderet a funkcia bude return ret, vystup ret budepovod zasifr spos
#samohl posun +2, spoluhl +3
#len lowercase

def encode(slovo: str) -> str:
    nr=""
    spoluhl="wrtpsdfghjklzxcvbnm"
    samohl="euioay"
    for i in slovo:
        if i in spoluhl:
            a=(ord(i)-97+3)%26+97
            x=chr(a)
            nr+=x
        elif i in samohl:
            c=(ord(i)-97+2)%26+97
            y=chr(c)
            nr+=y
    return nr

print(encode("abcd"))
print(encode("spagetkyspomazankou"))
print(encode("spiguthovejepileptickedazdovky"))
