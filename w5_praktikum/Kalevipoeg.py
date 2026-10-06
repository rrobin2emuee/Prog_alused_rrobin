args = [9,8,7,1,2,3,4,5,6,7,8]
kalevipoeg = "soomlased kirjutasid maha meie eepose"

print(len(kalevipoeg))
print(max(kalevipoeg))


koodid = [ord(m) for m in kalevipoeg]
print(min(koodid), max(koodid))