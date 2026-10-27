"""Pärib Eleringi kogulehelt (dashboard.elering.ee) tänased päev-ette elektrihinnad,
prindib need ja salvestab faili hinnad.csv.

API dokumentatsioon: https://dashboard.elering.ee/assets/swagger-ui/index.html
Vastus tuleb 15-minutiliste intervallidena: {'timestamp': unix-aeg, 'price': EUR/MWh}.
Ajad arvutatakse Eesti ajavööndis (Europe/Tallinn), sõltumata arvuti enda seadetest.

Käivita:  python elering_hinnad_reesar.py
"""
import csv
from datetime import datetime, time
from zoneinfo import ZoneInfo

import requests

API = "https://dashboard.elering.ee/api/nps/price"
FAILI_NIMI = "hinnad.csv"
EESTI = ZoneInfo("Europe/Tallinn")

def tanased_hinnad() -> dict[datetime, float]:
    """Tagastab tänased hinnad sõnastikuna {Eesti kellaaeg: hind EUR/MWh}.
    API ootab algus- ja lõpuaega koos ajavööndiga (ISO 8601), lõpp on kaasa arvatud,
    seega küsime Eesti aja järgi 00:00:00 kuni 23:59:59.
    """
    tana = datetime.now(EESTI).date()
    algus = datetime.combine(tana, time.min, tzinfo=EESTI)
    lopp = datetime.combine(tana, time.max, tzinfo=EESTI)
    vastus = requests.get(API, params={"start": algus.isoformat(), "end": lopp.isoformat()})
    vastus.raise_for_status()

    hinnad = {}
    for kirje in vastus.json()["data"]["ee"]:
        aeg = datetime.fromtimestamp(kirje["timestamp"], EESTI)
        hinnad[aeg] = kirje["price"]
    return hinnad

def salvesta_csv(hinnad: dict[datetime, float], failinimi: str) -> None:
    """Kirjutab hinnad CSV-faili: esimesel real veerupäised, edasi aeg;hind."""
    with open(failinimi, "w", newline="") as f:
        kirjutaja = csv.writer(f, delimiter=";")
        kirjutaja.writerow(["aeg", "hind_eur_mwh"])
        for aeg, hind in hinnad.items():
            kirjutaja.writerow([f"{aeg:%Y-%m-%d %H:%M}", hind])

def main() -> None:
    hinnad = tanased_hinnad()
    salvesta_csv(hinnad, FAILI_NIMI)
    print(f"Salvestatud faili {FAILI_NIMI}\n")
    print(f"{datetime.now(EESTI):%Y-%m-%d} elektrihinnad ({len(hinnad)} intervalli):")
    for aeg, hind in hinnad.items():
        print(f"  {aeg:%H:%M}  {hind:7.2f} EUR/MWh")

    odavaim = min(hinnad, key=hinnad.get)
    kalleim = max(hinnad, key=hinnad.get)
    print(f"\nOdavaim: {odavaim:%H:%M} {hinnad[odavaim]:.2f} EUR/MWh")
    print(f"Kalleim: {kalleim:%H:%M} {hinnad[kalleim]:.2f} EUR/MWh")

#Odavaima ja kalleima hinna leidmine ja failidesse odav.txt, kallis.txt salvestamine
    with open('odav.txt', 'w') as odav:
        odav.write(f"Odavaim: {odavaim:%H:%M} {hinnad[odavaim]} EUR/MWh")

    with open('kallis.txt', 'w') as kallis:
        kallis.write(f"Kalleim: {kalleim:%H:%M} {hinnad[kalleim]} EUR/MWh")

#Odavaima 4h järjestiku leidmine ja faili 4h_tarbija.txt salvestamine
    hinnad_list = list(hinnad.items())
    max_summa = 999
    min_summa = 0

    for i in range(len(hinnad_list) - 15):
        summa = 0
        for j in range(16):
            summa += hinnad_list[i + j][1]

        if summa < max_summa:
            max_summa = summa
            min_summa = i

    algus_aeg = hinnad_list[min_summa][0]
    lopp_aeg = hinnad_list[min_summa + 15][0]
    keskmine_hind = max_summa / 16

    with open('4h_tarbija.txt', 'w', encoding='utf-8') as f_4h:
        f_4h.write(
            f"Odavaim 4h periood on alates kell {algus_aeg:%H:%M} kuni {lopp_aeg:%H:%M}. Keskmine hind: {keskmine_hind:.2f} EUR/MWh")

    print(f"4h odavaim periood ({algus_aeg:%H:%M} - {lopp_aeg:%H:%M}) on salvestatud faili 4h_tarbija.txt")

if __name__ == "__main__":
    main()