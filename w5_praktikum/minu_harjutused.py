#Tee kalkulaator
#küsi kasutaja käest kaks arvu
#küsi tehe
#print tehe koos sisestatud arvude vastus
"""
x = int(input("Siseta arv, millega arvutada soovid"))
y =int(input("Sisesta teine arv, millega arvutada soovid"))
tehe = input("Sisesta tehte tüüp")
"""
""" if tehe == "+":
    print(x+y)
elif tehe == "-":
    print(x-y)
elif tehe == "*":
    print(x*y)
elif tehe == "/":

    print(x, tehe, y)
"""

################################################################
a = int(input("Siseta arv, millega arvutada soovid"))
b =int(input("Sisesta teine arv, millega arvutada soovid"))
tehe = input("Sisesta tehte tüüp")

def summa(a, b):
    return a + b
def lahutamine(a, b):
    return a - b
def korrutamine(a, b):
    return a * b
def jagamine(a, b):
    return a / b

operaatorid = {
    "+": summa,
    "-": lahutamine,
    "*": korrutamine,
    "/": jagamine,
}
print(operaatorid[tehe](a, b))






''' m = 123
print(m//2)
print(m/100, m//100)
'''