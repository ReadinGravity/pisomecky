#dany je zoz kt je plny stringov random, vytvorte novy zoz kt bude obsahovat pocty samohlasok v jedno stringoch

zoz=["jozo","fero","jano","dudo","spagetkyspomazankou","spigimigy","heheheeh","dazdovka","cajik","maja" ]
samohl="euioay"
nzoz=[]
pocet=0
for i in zoz:
	for x in i:
		if x in samohl:
			pocet+=1
	nzoz.append(pocet)
	pocet=0
print(*nzoz)

