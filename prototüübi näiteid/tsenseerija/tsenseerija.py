from easygui import *

###############################
# Tsenseeritavate sõnade aken #
###############################
msg = "Sisesta tühikutega eraldatult sõnad, mis välja tsenseerida:"
sisend = enterbox(msg)                       # Tekstikasti sisestatud teksti salvestame muutujasse
tsenseeritavad_sõnad = sisend.split(" ")     # Jagame sisestatud teksti tühikute pealt eraldi sõnedeks
print("Tsenseeritakse: " + str(tsenseeritavad_sõnad)) 

####################
# "OK" nupuga aken #
####################
msg = "Sõnad sisse loetud. Järgmisena vali sisendfail, mida tsenseerida."
msgbox(msg)

#############################
# Sisendfaili valimise aken #
#############################
failinimi = fileopenbox("Vali sisendfail")          # Kasutaja valib sisendfaili

########################
# Sisendfaili lugemine #
########################
read = []
fail = open(failinimi,"r")                          # Avame sisendfaili
for rida in fail:
    read.append(rida)
fail.close()

######################
# Andmete töötlemine #
######################
tsenseeritud_read = []                              # Loome tühja järjendi tsenseeritud ridade hoidmiseks
for rida in read:                                   # Võtame korraga ühe rea
    for tsenseeritav_sõna in tsenseeritavad_sõnad:  # Käime igast reast üle korra iga tsenseeritava sõna kohta
        rida = rida.replace(tsenseeritav_sõna, "<TSENSEERITUD>")  # Igas kohas, kus see sõna reas leidub, asendame selle tekstiga "<TSENSEERITUD>"
    tsenseeritud_read.append(rida)                  # Jätame tsenseeritud rea järjendi abil meelde

####################
# "OK" nupuga aken #
####################
msg = "Tsenseerimine tehtud. Järgmisena vali väljundfail, kuhu tulemus salvestada."
msgbox(msg)

##############################
# Väljundfaili valimise aken #
##############################
failinimi = filesavebox("Save As...", default="tsenseeritud_tekst.txt")   # Kasutaja valib väljundfaili, vaikimisi nimega "tsenseeritud_tekst.txt"

############################
# Väljundfaili kirjutamine #
############################
fail = open(failinimi,"w")          # Avame väljundfaili
for rida in tsenseeritud_read:      # Iga tsenseeritud rea kirjutame faili
    fail.write(rida)
fail.close()