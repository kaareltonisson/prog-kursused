# Näiteprojektid

Siin kaustas paiknevad tarkvara arendamise õpiku näiteprojektid. Need materjalid on mõeldud praktiliste näidetena programmidest, millega sarnaste loomisega peaks õpilane oma projekti raames hakkama saama. Materjalide sisu on lubatud oma projektis kasutada:      

# Näidete nimistu

Igal näiteprogrammil võib olla täiendavaid Pythoni mooduleid, mis tuleb programmi käivitamiseks esmalt paigaldada. 

## Tsenseerija

Programm on tekstide tsenseerija. Kasutaja valitud sõned asendatakse sisendfailis (ka sõnede osadena) sõnega <TSENSEERITUD>.

### Paigaldamine

Programm nõuab graafikamooduli EasyGUI (mooduli nimi **easygui**) paigaldamist.

### Programmi töö

Programm küsib kasutajalt sõned, mis välja tsenseerida (tekstikasti sisestatuna). 
Kasutajalt küsitakse sisendfail (failibrauseri aknaga).
Programm loeb sisendfaili tekstina sisse.
Programm asendab igas reas kõik soibvad sõnejupid sõnega <TSENSEERITUD>.
Kasutajalt küsitakse väljundfail (failibrauseri aknaga, vaikimisi tsenseeritud_tekst.txt). 
Tsenseeritud tekst kirjutatakse määratud faili.

## Mälumäng

Programm on piltidega mälumäng. Igas küsimuses (näites on kaasas kaks küsimust) kuvatakse kasutajale pilt ning mingi arv valikuvariantide nuppe. Kui kasutaja nupule klõpsab, näidatakse tema tulemust: õige vastusega saab 1 punkti, vale vastusega 0 punkti ning näidatakse õiget vastust. Seejärel ilmub järgmine küsimus. Küsimuste järjekord ja valikuvariantide järjekord on iga kord juhuslikud. Kui küsimused otsa saavad, kuvatakse punktisumma.

### Paigaldamine

Programm nõuab mooduli PIL (mooduli nimi **pillow**) paigaldamist. Selle abil saame Tkinteris kasutada erinevate failiformaatidega pilte.
Programm kasutab graafikaliidest Tkinter, mis peaks olema Pythoniga vaikimisi kaasas.

### Programmi töö

Programm loeb failist *"küsimused.txt"* küsimuste info. Igal real on tabulaatorisümboliga (*tab*, *"\t"*) eraldatud väärtused. Esimene neist on pildifaili nimi/asukoht. Teine väärtus on õige vastusevariant. Kõik järgnevad väärtused on valed vastusevariandid (nii mitu kui soovime).
Programm paneb küsimused juhuslikku järjestusse.
Programm alustab Tkinteri graafika tööd. 
Ühe küsimuse jaoks kuvatakse vastav pilt ning paigutatakse selle alla valikuvariantide nupud (juhuslikus järjestuses). Nuppudega on seotud funktsioonid, mis käivituvad nupule vajutades. Õige valiku nupu funktsioon annab ühe punkti juurde ja kuvab akna "Õige!". Vale valiku nupu funktsioon punkte juurde ei anna ning kuvab akna "Vale!", kus on antud õige vastus.
Seejärel graafika ootab, kuni nupuvajutusega käivitatud funktsioon muudaks teatud muutujat. Vastasel juhul üritaks Tkinter korraga kõiki küsimusi näidata, mida me ei soovi.
Kui kasutaja vajutab valiku nupule, käivitub õige/vale valiku funktsioon (avaneb vastav pop-up aken). Akna sulgemisel kuvatakse järgmine küsimus.
Küsimuste lõppedes kuvatakse punktisumma.

## Graafikute kuvaja

Programm on CSV faili sisu põhjal loodud graafikute kuvaja. Programm loeb sisendfailist andmed. Kasutaja valib, milliseid veergusid näidata. Valitud veergude põhjal luuakse graafikud, mis kuvatakse ekraanile.

Meie näites on esimesel real veergude nimed (Nimi;Jõud;Kiirus;Elud) ning seejärel kolm andmerida.
Igal real on tegelase nimi ning tema kolme omaduse väärtused: jõud, kiirus ja elud.

### Paigaldamine

Vajalik on paigaldada moodul **matplotlib**, mille abil on võimalik moodustada graafikuid.
Programm kasutab graafikaliidest Tkinter, mis peaks olema Pythoniga vaikimisi kaasas.
Programm kasutab moodulit csv, mis peaks Pythoniga kaasas olema, et töödelda CSV faile.

### Programmi töö

Kasutajalt küsitakse sisendfaili asukoht failibrauseri abil.
Programm loeb sisendfaili ning jagab iga rea semikoolonite põhjal järjendiks. Ridade järjendid hoiustatakse andmete järjendina.
Programm moodustab veerunimede põhjal valikukastid, mis vastavad veergude nimedele (välja arvatud Nimi). Programm lisab nende alla kinnitava nupu tekstiga "Edasi".
Kasutaja valib soovitud veerud ning vajutab nuppu.
Programm moodustab iga valitud veeru kohta graafiku, lugedes iga andmerea kohta rea nime ning vastavalt kohalt veeru väärtuse. Erinevatele omadustele on määratud erinevad graafikute värvid.
