
from w5_praktikum.kalkulaator import operaatorid

a = int(input("Siseta arv, millega arvutada soovid"))
b =int(input("Sisesta teine arv, millega arvutada soovid"))
tehe = input("Sisesta tehte tüüp")

print(operaatorid[tehe](a, b))