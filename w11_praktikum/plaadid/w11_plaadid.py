'''
Saaremaal, Rahuste külas, ühes väikemajas peetakse garaažimüüki.
Seal elav vanataat on otsustanud oma vinüülplaatide kogu maha müüa
Ta on aastakümneid kogunud erinevate žanrite ja aastakümnete muusikat, kuid nüüd on aeg edasi liikuda
Tal on mitu kastitäit vinüülplaate, mida ta on hoolikalt hoidnud ning on kirja pannud kõik plaadid, mida ta kunagi kogunud on.

Ridade kaupa on paberile kirja pandud iga plaadi pealkiri, žanr ja väljaandmise aasta.

Kirjuta programm, mis loeb vanataadi vinüülplaatide kogu andmed failist ja võimaldab kasutajal otsida plaate žanri või/ja aasta järgi.

Võtab sisendina faili nime.

Küsib kasutajalt žanri (jätta tühjaks, kui ei soovi žanri järgi otsida).

Küsib kasutajalt aasta (jätta tühjaks, kui ei soovi aasta järgi otsida).

Väljastab kõik plaadid, mis vastavad kasutaja sisestatud kriteeriumitele
Kui kasutaja ei sisesta ühtegi kriteeriumi, tagastab programm kõik plaadid.

###
Näide programmi tööst
>> Sisesta faili nimi: vinüülid.txt
>> Sisesta žanr:
>> Sisesta ajavahemik: 1970

The Beatles - Let It Be

###
Näide programmi tööst
>> Sisesta faili nimi: vinüülid.txt
>> Sisesta žanr: pop
>> Sisesta ajavahemik:

Michael Jackson - Thriller

###
Näide programmi tööst
>> Sisesta faili nimi: vinüülid.txt
>> Sisesta žanr:
>> Sisesta ajavahemik:

The Beatles - Let It Be
Michael Jackson - Thriller
Queen - A Night at the Opera
'''
otsitav_zanr = input("Sisesta žanr: ").lower()  #küsin kasutajalt zanri, muudan vastuse väiketähteteks
otsitav_aasta = input("Sisesta ajavahemik: ")   #küsin kasutajalt aastat

with open("kogumik.txt", "r", encoding="utf-8") as fail:    #avan faili lugemise reziimis
    for rida in fail:   #käin tsükliga read läbi
        osad = rida.strip().split(",")  # Jagame rea komade järgi tükkideks

        plaat = osad[0].strip()             #omistan muutujatele vastavalt listi indeksi järgi kas nimi, zanr ja aasta
        zanr = osad[1].strip().lower()
        aasta = osad[2].strip()

        if (not otsitav_zanr or otsitav_zanr == zanr) and (not otsitav_aasta or otsitav_aasta == aasta):     # Kontrollin, kas kriteeriumid klapivad või kas zanr/aasta väli jäeti tühjaks
            print(plaat)