

def ristsumma(arv:int)-> int:
    rs = 0
    for el in (str(arv)):
        print(type(el), el)
        rs = rs + int(el)
    return rs
print(ristsumma(926))

i = 2
while(True):
    i += 1
    if i**2 == ristsumma(i)**3:
        print(i)
        break

def yhis_kassa(n1, n2):
    str2 = str(n2)
    yhised_elemendid = []

    for el1 in str(n1):
        if el1 in str2:
            yhised_elemendid.append(el1)

    return set(yhised_elemendid)

print(yhis_kassa(n1:78293, n2:78322))
print(yhis_kassa(n1:23821, n2:8312))
print(yhis_kassa(n1:23123, n2:7635))
