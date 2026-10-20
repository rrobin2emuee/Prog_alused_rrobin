#for i in range(0,6):
   # print(i*"*")

'''for i in range(6):
    tühikud = " " * (5 - i)
    tärnid = "*" * i
    print(tühikud + tärnid)'''

#for i in range(1, 6):
   # print(("*" * i).rjust(5))

'''for i in range(1, 6):
    vasak = (i * "*").ljust(5)
    parem = (i * "*").rjust(5)
    print(parem + vasak)'''
'''
def kool3(kõrgus):
    for i in range(kõrgus):
        tühik = " " * (kõrgus - i)
        tähed = "*" * (i * 2 -1)
        print (tühik, tähed)
#kool3(5)

def kool4(korgus,sumbol):
    for i in range(korgus):
        print((korgus - i)* " " + (i * 2 + 1) * sumbol + (korgus - i)* " ")
#kool4(5,"*")



def kool5(korgus, sumbol):
    for i in range(korgus - 1, -1, -1):
        print((korgus - i - 1) * " " + (i * 2 + 1) * sumbol)

#kool5(4, "*")

print(kool4(4,"*") + (kool5(4, "*")))'''

def kool4(korgus, i, sumbol):
    return (korgus - i - 1) * " " + (i * 2 + 1) * sumbol + (korgus - i - 1) * " "
def kool5(korgus, i, sumbol):
    return (korgus - i - 1) * " " + (i * 2 + 1) * sumbol
korgus = 4
for i in range(korgus):
    print(kool4(korgus, i, "*") + "|" + kool5(korgus, korgus - 1 - i, "*"))