import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import csv

####
# Graafika algatamine
####
root = tk.Tk()              # Loome graafika juurakna
root.title("Graafikud")

####
# Sisendfaili lugemine
####
root.filename =  filedialog.askopenfilename(initialdir = ".",title = "Vali sisendfail",filetypes = (("csv files","*.csv"),("all files","*.*")))

csv_fail = open(root.filename, encoding="UTF8")     # Avame faili, mille kasutaja sisendiks valis
csv_reader = csv.reader(csv_fail, delimiter = ";")  # Anname selle CSV lugejale
ridade_loendur = 0
andmed = []
for rida in csv_reader:             # CSV lugeja jaotab iga rea järjendiks (meil semikoolonite järgi)
    if ridade_loendur == 0:         # Esimesel real on veergude nimed
        print("veergude nimed:"+str(rida))
        veergude_nimed = rida
    else:                           # Ülejäänud ridadel on andmed
        print("rea sisu:"+str(rida))
        andmed.append(rida)
    ridade_loendur += 1
csv_fail.close()

####
# Valikute küsimise aken
####
def edasi_nupp():   # Kutsume välja edasi-nupu vajutamisel (muudame muutujat, et lubada edasiminekut)
    pidur.set(1)
    
frame = tk.Frame(root)          # Loome aknasse raami (ala, mille sisse paigutame teised graafikajupid)
frame.pack(side=tk.TOP)         # Paigutame raami akna ülemise serva külge (ilma käsuta "pack" ei ilmu raami sisu ekraanile)

tekst = "Vali graafikul näidatavad väärtused"        
silt = tk.Label(frame, text=tekst)   # Lisame raamile sildi meie määratud tekstiga
silt.config(font=("Serif", 16))
silt.pack(fill=tk.BOTH, padx=5, pady=5)

graafikute_valikud = []     # Kasutaja valib, milliste veergude graafikuid näidata. Peame kasutama Tk IntVar tüüpi, muidu valikunupud ei toimi.  
for veeru_nimi in veergude_nimed:
    var = tk.IntVar()
    graafikute_valikud.append(var)
    if veeru_nimi == "Nimi":         # Nimedest ei saa graafikut teha, seega ei tee me sellele valikunuppu
        var.set(0)
    else:
        c = tk.Checkbutton(frame, text=veeru_nimi, variable=var)    # Kui valimata, siis 0. Kui valitud, siis 1.
        c.pack(side=tk.TOP,anchor="w")

button = tk.Button(frame, 
                    text="Edasi", 
                    fg="black",
                    command=edasi_nupp)     # Loome nupu, millega minnakse edasi graafikute joonistamise juurde
button.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10) # paigutame nupu alla serva
pidur = tk.IntVar()
frame.wait_variable(pidur)        # Ootame muutuja pidur muutumist (nupu vajutamist).
                                  # Kui me siin ei pidurdaks, üritaks Tkinter korraga programmi kõiki graafikaelemente näidata

kasutatavad_indeksid = []         # Eraldame nende veergude indeksid, mida kasutaja näha tahtis
i = 0
for valik in graafikute_valikud:
    if graafikute_valikud[i].get() == 1:     # Kui valiku väärtus indeksil i on 1, siis on tegu soovitava indeksiga
        kasutatavad_indeksid.append(i)
    i += 1

####
# Graafikute kuvamise aken
####
for widget in frame.winfo_children(): # Kustutame raami eelneva sisu (valikuvariandid ja edasi-nupu), et asendada see uuega
    widget.destroy()

värvid ={"Jõud":"red", "Kiirus":"green", "Elud":"pink"}
for indeks in kasutatavad_indeksid:     # Iga indeks vastab ühele andmeveerule/graafikule
    figure1 = Figure(figsize=(5,4), dpi=100) 
    subplot1 = figure1.add_subplot(1,1,1)
    nimi = veergude_nimed[indeks] # Graafiku pealkirja võtame veergude nimede järjendist  
    subplot1.set_title(nimi)   
    xAxis = []      # Nimed
    yAxis = []      # Arvulised väärtused
    for andmerida in andmed:    # Igast andmereast võtame nime(esimese veeru) ning indeksile vastava veeru väärtuse
        xAxis.append(andmerida[0])
        yAxis.append(int(andmerida[indeks]))
    if nimi in värvid: # Kui veerul on eraldi määratud värv, kasutame seda
        värv = värvid.get(nimi)
    else:
        värv = "black"
    subplot1.bar(xAxis, yAxis, color = värv)      # Moodustame graafiku nimedest ja väärtustest
    canvas = FigureCanvasTkAgg(figure1, frame) 
    canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

####
# Graafika käivitamine
####    
root.mainloop()