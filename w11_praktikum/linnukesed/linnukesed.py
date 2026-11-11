'''
Juku otsustas osa võtta aialinnuvaatlusest ja läks tunniks ajaks õue.
Ta kirjutas nähtud lindude liikide ja arvude kaupa faili linnud.txt.
Igas reas on liik ja arv teineteisest eraldatud komaga.
Eeldame, et liigid mitmel real ei kordu.

tihane,7
varblane,5
rohevint,1
leevike,6
vares,2

Kirjuta funktsioon linnud_sõnastikku, mille argumendiks on failinimi ja mis tagastab sõnastiku, kus kirjete võtmeteks on linnunimed ja väärtusteks lindude arvud.

Näiteks:
>> linnud_sõnastikku("linnud.txt")
{'tihane': 7, 'varblane': 5, 'rohevint': 1, 'leevike': 6, 'vares': 2}


Kirjuta programm, mis:
* küsib kasutajalt faili nime;
* loeb funktsiooni linnud_sõnastikku abil sellest failist andmed ja koostab sõnastiku;
* küsib kasutajalt arvu;
* väljastab eraldi ridadel kõik linnuliigid, keda Juku nägi rohkem kui näidatud arv kordi, ning nende arvud sulgudes;
* väljastab Juku nähtud lindude koguarvu.

LISA ÜLESANNE KODUS LAHENDAMISEKS: küsi Juku käest uuesti, mis lindusid ta veel nägi.
Kõik sisestused peavad olema ühel real. Näiteks:
> Uus sisestus: vares,4
> Uus sisestus: roherähn,6
> Uus sisestus: vares,4
väljub ctrl + C

Näiteks võib programmi väljund olla:
Sisesta failinimi: linnud.txt
Sisesta arv: 5
tihane (7)
leevike (6)
Juku nägi väljas 21 lindu.
'''


"""def loe_linnud(faili_nimi):
    with open(faili_nimi + ".txt", encoding="utf-8") as f:
        for rida in f:
            if rida:
                yield [osa.strip().lower() for osa in rida.split(",")]


def loo_linnu_raamat(faili_generaator):
    sonastik = dict()

    for lind, arv in faili_generaator:
        sonastik[lind] = int(arv)

    return sonastik

def lindude_koguarv(linnu_raamat):
    return sum(linnu_raamat.values())


faili_nimi = input("Anna kohe oma faili nimi siia: ")
fail = loe_linnud(faili_nimi)
linnu_raamat = loo_linnu_raamat(fail)
print(linnu_raamat)
print(lindude_koguarv(linnu_raamat))"""

def linnud_sonastikku(faili_nimi):
    linnud = {}                                          #teen tühja sõnastiku
    with open(faili_nimi, "r", encoding="utf-8") as f:      #avan faili
        for rida in f:              #rea kaupa käin andmed läbi, puhastan need stripiga ja kui rida esineb,
                                    #lisan spliti koha pealt dicti nime ja arvu
            rida = rida.strip()
            if rida:
                osa = rida.split(",")
                nimi = osa[0].strip()
                arv = int(osa[1].strip())
            linnud[nimi] = arv      #siin toimub lisamine key value paarina
    return linnud

fail = "linnud.txt" #input("Sisesta failinimi: ")
lind_arv = int(input("Sisesta arv: "))
lindude_sonastik = linnud_sonastikku(fail)

try:    # tänu sellele try käsule, teab arvuti, et hiljem peale info sisestamist saab selle bloki ära lõpetada, nt ctrl + c
    while True: #lõputu tsükkel, mis kestab kuni kasutaja manuaalse lõpuni
        uus_sisestus = input("Uus sisestus: ")
        if uus_sisestus.strip():
            osa = uus_sisestus.split(",")
            nimi = osa[0].strip()
            arv = int(osa[1].strip())

            if nimi in lindude_sonastik:  #kui lind on juba sõnastikus, liidan arvud kokku
                lindude_sonastik[nimi] += arv
            else:
                lindude_sonastik[nimi] = arv  #kui on täiesti uus lind, lisan sõnastikku
except KeyboardInterrupt:   #lõpetab tsükli, kui kasutaja vajutab klava
    pass # jätkab järgmise koodiga edasi
koguarv = 0
for lind, arv in lindude_sonastik.items():
    koguarv += arv              #liidan kokku kõigi lindude koguarvu

    if arv > lind_arv:               #kui vaatluste arv on suurem kui kasutaja sisestatud arv, prindin välja
        print(f"{lind} ({arv})")

faili_nimi = linnud_sonastikku("linnud.txt")

print(f"Juku nägi väljas {koguarv} lindu")
