# napiste funckiu kt bude mat 1 vstup parameter retaazec funckia ret prejde a vrati priemer vsetkych cislic kt tam najde

def average(ret:str):
    nums = "0123456789"
    sum=0
    pocet=0
    for i in ret:
        if i in nums:
            pocet+=1
            sum+=int(i)
#       else:
#         return("false") - dava potom false aj ked tam je hociake pismeno
    average=sum/pocet
    return(average)

print(average("10245867"))
print(average("dfg175468"))
print(average("ajbfhe"))











