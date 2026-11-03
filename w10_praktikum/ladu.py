def loe_read(failinimi):
    with open(failinimi, encoding="utf-8") as f:        #utf-8 on eesti tähestik
        next(f, None)       # Jätab esimese rea vahele, sest see on csv failis pealkiri
        for rida in f:
            yield rida.strip()              # .strip puhastab teksti formaadi ära

def kontrolli_eks_toode(nimekiri, toode):       #nimekiri on sõnastik, toode on list, üks rida toote andmeid
    hind = float(toode[2])

    if nimekiri.get("max_t") is None or nimekiri["max_t"]["hind_km_ta"] < hind:       #kõige kallima toote leidmine
        nimekiri["max_t"] = {                                                   # võrdlen, kas kalleima toote hind on antud või väiksem senisest maksimumist
            "inventari_nr": toode[0],
            "nimetus": toode[1],
            "hind_km_ta": hind,
            "km_maar": toode[4],}

    if nimekiri.get("min_t") is None or nimekiri["min_t"]["hind_km_ta"] > hind:       #kõige odavama toote leidmine
        nimekiri["min_t"] = {                                                   # võrdlen, kas odavaima toote hind on antud või suurem senisest miinimumist
            "inventari_nr": toode[0],
            "nimetus": toode[1],
            "hind_km_ta": hind,
            "km_maar": toode[4],}

def main():     #selles põhifun. annan muutujatele algväärtused ning hiljem salvestan siia leitud väärtused
    toodete_arv = 0 # integer
    maarade_arvud = {}  #sõnastik
    otsas_tooted = [] #list
    eks_toode = {"max_t": None, "min_t": None}  #sõnastik(key, value) paarid

    vaartus_km_ta = 0.0 #float
    vaartus_vana_km_ga = 0.0 #float
    vaartus_uue_maaraga = 0.0 #float

    for rida in loe_read("tooted.csv"): # hakkan käima loe_read generaatori abil rea kaupa läbi andmeid
        toode = rida.split(";")         # teen eraldatud ; listi, et saaksin ligi andmetele indeksite kaudu
        toodete_arv += 1                # toodete arvu leian lisades mällu iga rea kohta +1

        maar = int(toode[4])             # eraldan toodete arvu käibemaksumäärade kaupa, tekstist teen int
        maarade_arvud[maar] = maarade_arvud.get(maar, 0) + 1    #otsin sõnastikust maarade_arvud praegust käibemaksumäära ja lisan vastavalt kas 9 või 22% loendurisse

        laoseis = int(toode[3]) # teen laoseisu int-iks ja lisan append
        if laoseis <= 0:
            otsas_tooted.append((toode[0], toode[1]))   #lisan laost otsas oleva toote info nimekirja, inv nr ja nimi

        kontrolli_eks_toode(eks_toode, toode)     # kõige kallim ja odavam toode, funktsiooni väljakutse(sõnastik,list)

        hind_km_ta = float(toode[2])                 # arvutan  toodete kogu väärtuse ilma km_ta
        vaartus_km_ta += hind_km_ta * laoseis

        hind_vana = hind_km_ta * (1 + maar / 100)    # arvutan vana km-ga toodete kogu väärtuse
        vaartus_vana_km_ga += hind_vana * laoseis

        uus_maar = 24 if maar == 22 else maar        # arvutan hinna uue km määraga
        hind_uus = hind_km_ta * (1 + uus_maar / 100)
        vaartus_uue_maaraga += hind_uus * laoseis

    vahe = (vaartus_uue_maaraga - vaartus_vana_km_ga)   #arvutan uue ja vana km määra vahe kogu laoseisu puhul

    print(f"1. Toodete arv failis: {toodete_arv}")  #prindin välja aruande

    print("2. Toodete arv käibemaksumäärade kaupa:")
    for m, arv in sorted(maarade_arvud.items()): #Võtan sõnastikust kõik kirjed ehk paarid korraga (ühes pooles on käibemaksumäär ja teises pooles toodete arv)
        print(f"   - {m}%: {arv} toodet")

    print(f"3. Laost otsas on {len(otsas_tooted)} toodet:")
    for inv, nim in otsas_tooted:
        print(f"   - {inv}: {nim}")

    max_t = eks_toode["max_t"]      #arvutan min ja max toote hinnad km määraga
    min_t = eks_toode["min_t"]
    max_km_ga = round(max_t["hind_km_ta"] * (1 + int(max_t["km_maar"]) / 100), 2)
    min_km_ga = round(min_t["hind_km_ta"] * (1 + int(min_t["km_maar"]) / 100), 2)

    print(f"4. Kõige kallim: {max_t['nimetus']} ({max_t['inventari_nr']})," f" {max_t['hind_km_ta']} € km-ta, {max_km_ga} € km-ga")
    print(f"   Kõige odavam: {min_t['nimetus']} ({min_t['inventari_nr']})," f" {min_t['hind_km_ta']} € km-ta, {min_km_ga} € km-ga")

    print(f"5. Lao koguväärtus käibemaksuta: {vaartus_km_ta:,.2f} €")
    print("6. Lao koguväärtus käibemaksuga (vana määr):" f" {vaartus_vana_km_ga:,.2f} €")
    print("   Lao koguväärtus käibemaksuga (uus määr):" f" {vaartus_uue_maaraga:,.2f} €")
    print(f"   Vahe: ({vahe:,.2f} €")

with open("tooted_2025_07.csv", "w", encoding="utf-8") as uus_tabel: #avan uue faili ning kirjutan sinna uue tabeli
    uus_tabel.write("inventari_nr;nimetus;hind;laoseis;km_maar;hind_km_ga\n") # Kirjutan esimese rea koos uue veeru nimega

    # Siia tuleb sinu olemasolev tsükkel, mis loeb vanu tooteid
    for rida in loe_read("tooted.csv"):
        toode = rida.split(";")

        # Võtame vanadandmed
        inventari_nr = toode[0]
        nimetus = toode[1]
        hind_ta = float(toode[2])
        laoseis = toode[3]
        maar = int(toode[4])

        # Muudame 22% -> 24%
        uus_maar = 24 if maar == 22 else maar

        # Arvutame uue hinna käibemaksuga (ümardame 2 komakohani)
        hind_km_ga = round(hind_ta * (1 + uus_maar / 100), 2)

        # Paneme uue rea semikoolonitega kokku
        uus_rida = (
            f"{inventari_nr};{nimetus};{hind_ta};{laoseis};{uus_maar};{hind_km_ga}\n"
        )

        # Kirjutame selle rea uude faili
        uus_tabel.write(uus_rida)
if __name__ == "__main__":
    main()