import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import random

random.seed() # Tagame, et juhuslikud järjestused poleks kogu aeg samad

küs_fail = open("küsimused.txt", encoding="UTF8")
küsimused = []
for rida in küs_fail:
    küsimus = rida.strip().split("\t")   # kohal 0 on pildifaili nimi, kohal 1 on õige vastus, edasi valed vastused
    küsimused.append(küsimus)
küs_fail.close()

random.shuffle(küsimused)       # Paneme küsimused juhuslikku järjekorda

root = tk.Tk()                  # Loome tühja juurakna, kuhu saame graafikaelemente lisada
root.title("Mälumäng")
frame = tk.Frame(root)          # Loome aknasse raami, mille sees hakkame näitama küsimusi
frame.pack(side=tk.TOP)         # Paigutame raami tahvlile ülemise serva külge (ilma käsuta "pack" ei ilmu raami ega selle sisu ekraanile)

global punktid    # Arvestame punkte globaalses muutujas (nendega peab ettevaatlik olema)
punktid = 0

def õige_käsk():    # Käivitame siis, kui valitakse õige vastus (suurendame punktisummat)
    global punktid
    punktid += 1
    messagebox.showinfo("Õige!", "Õige vastus!\nSkoor: " + str(punktid))
    pidur.set(0)      # Ebaharilikult pole oluline, mis väärtuse me siin anname. Oluline on see, et Tk näeb oleku muutumist.
    
def vale_käsk():    # Käivitame siis, kui valitakse vale vastus (vähendame punktisummat)
    global punktid
    global õige_vastus
    messagebox.showinfo("Vale!", "Vale vastus!\nÕige vastus oli: "+ õige_vastus +"\nSkoor: " + str(punktid))
    pidur.set(0)      # Ebaharilikult pole oluline, mis väärtuse me siin anname. Oluline on see, et Tk näeb oleku muutumist.
    
for küsimus in küsimused:    # Näitame korraga ühe küsimuse
    vastused = küsimus[1:]      # Alates teisest elemendist (indeksist 1) on vastusevariandid
    global õige_vastus
    õige_vastus = vastused[0]   # Õige vastus on failis esimene

    img = ImageTk.PhotoImage(Image.open(küsimus[0]))    # Lisa küsimusele vastav pilt
    w1 = tk.Label(frame, image=img).pack(side="top")    # Paiguta pilt ülemisse serva

    random.shuffle(vastused) # Paneme vastusevariandid juhuslikku järjekorda
    for vastus in vastused:  # Igale vastusevariandile loome eraldi nupu
        if vastus == õige_vastus:    # Kui õige vastuse nupp, seome sellele õige valiku funktsiooni
            käsk = õige_käsk
        else:                        # Kui vale vastuse nupp, seome sellele vale valiku funktsiooni
            käsk = vale_käsk
        button = tk.Button(frame, 
                       text=vastus, 
                       fg="black",
                       command=käsk)
        button.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=10, pady=10)   # paiguta nupp vasakult alates, terve serva ulatuses laiali
    pidur = tk.IntVar()
    frame.wait_variable(pidur)        # Graafika ootab siin muutuja pidur oleku muutust. Kui me siin ei ootaks, üritaks Tkinter kõiki küsimusi korraga (edutult) näidata
    for widget in frame.winfo_children(): # Kustutame küsimuse jupid (pildi ja nupud) raamist, et saaks näidata järgmist küsimust
        widget.destroy()

# Siia jõudes on kõik küsimused läbitud
lõputekst = "Mäng on lõppenud.\nTulemus: " + str(punktid) + " punkt(i)."        
lõpusilt = tk.Label(frame, text=lõputekst)   # Lisame tahvlile sildi meie määratud tekstiga
lõpusilt.config(font=("Serif", 44))
lõpusilt.pack(fill=tk.BOTH)
button = tk.Button(frame, 
                    text="Sulge", 
                    fg="black",
                    command=root.destroy)   # Nupu vajutamisel hävitatakse juuraken, see sulgeb programmi
button.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)
            
root.mainloop()     # Käivitame Tk graafika