#Tee kalkulaator
#küsi kasutaja käest kaks arvu
#küsi tehe
#print tehe koos sisestatud arvude vastus

x = int(input("Siseta arv, millega arvutada soovid"))
y =int(input("Sisesta teine arv, millega arvutada soovid"))
tehe = input("Sisesta tehte tüüp")

if tehe == "+":
    print(x+y)
elif tehe == "-":
    print(x-y)
elif tehe == "*":
    print(x*y)
elif tehe == "/":

    print(x, tehe, y)


for operaator in ["+","-","*","/"]:
    if tehe == operaator:


''' m = 123
print(m//2)
print(m/100, m//100)
'''