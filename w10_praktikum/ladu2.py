
def loe_read(failinimi):
    with open(failinimi, encoding="utf-8") as f:
        next(f, None) #esimese rea jätan välja, kuna see on pealkirja rida .csv failis
       # lugeja = csv.DictReader(f, delimiter=";")
        for rida in f:
           yield rida.rstrip("\n")

otsas_toode = {}
vanad_mm = {}
toodete_arv = 0
toode_rida = []

def lisa_toode(nimekiri, toode):
    nimekiri[toode[0]] = {
        "nimetus": toode[1],
        "hind_km_ta": toode[2],
        "laoseis": toode[3],
        "km_maar": toode[4],  }

for rida in loe_read("tooted.csv"):
    toode_rida = (rida.split(";"))
    toodete_arv += 1

    vanad_mm[toode_rida[4]] = vanad_mm.get(toode_rida[4], 0) + 1
    toote_kogus_int = int(toode_rida[3])
    if toote_kogus_int <= 0:
        lisa_toode(otsas_toode, toode_rida)

def kontrolli_eks_toode(nimekiri, toode):
    if nimekiri.get("max_t")["hind"] < toode[2]:
        lisa_toode()

def kontrolli_eks_toode(toode):
  """Leiab kõige kallima ja odavama toote lühemalt."""
  hind = float(toode[2])

  # Hoiame infot praeguse toote kohta käepärases formaadis
  t_andmed = {
      "inv_nr": toode[0],
      "nimetus": toode[1],
      "hind_km_ta": toode[2],
      "km_maar": toode[4],
  }

  # Kontrollime maksimumi
  if eks_toode["max_t"] is None or hind > float(
      eks_toode["max_t"]["hind_km_ta"]
  ):
    eks_toode["max_t"] = t_andmed

  # Kontrollime miinimumi
  if eks_toode["min_t"] is None or hind < float(
      eks_toode["min_t"]["hind_km_ta"]
  ):
    eks_toode["min_t"] = t_andmed
