#funkciu kt sa bude volat jozo, 1 vstup parameter aka zoznam funkci vrati true ak je v zoz viiac parnych ako npar cisel
#inak vrati false

def jozo(zoznam):
    par=0
    nepar=0
    for i in zoznam:
        if i%2==0:
            par+=1
        else:
            nepar+=1
    if par>nepar:
        status=True
    else:
        status=False
    return status


print(jozo([3, 2, 10, 10, 12, 120]))
print(jozo([33, 2, 11, 10, 1221, 120]))
