from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        m = float(mass.get()) 
        h = float(heigh.get()) 
        meters.set(m/(h**2))
        met = m/(h**2)
        if met < 16:
            results.set("Underweight (Severe thinness)")
        elif met == 16 or met > 16 and met < 17:
            results.set("Underweight (Moderate thinness)")
        elif met == 17 or met > 17 and met < 18.5:
            results.set("Underweight (Mild thinness)")
        elif met == 18.5 or met > 18.5 and met < 25:
            results.set("Normal range")
        elif met == 25 or met > 25 and met < 30:
            results.set("Overweight (Pre-obese)")
        elif met == 30 or met > 30 and met < 35:
            results.set("Obese (Class I)")
        elif met == 35 or met > 35 and met < 40:
            results.set("Obese (Class II)")
        elif met == 40 or met > 40:
            results.set("Obese (Class III)")
        
    except ValueError:
        pass

root = Tk()
root.title("body mass index")
root.geometry("300x150")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mass = StringVar()
mass_entry = ttk.Entry(mainframe, width=7, textvariable=mass)
mass_entry.grid(column=2, row=1, sticky=(W, E))

heigh = StringVar()
heigh_entry = ttk.Entry(mainframe, width=7, textvariable=heigh)
heigh_entry.grid(column=2, row=2, sticky=(W, E))

meters = StringVar()

ttk.Label(mainframe, textvariable=meters).grid(column=2, row=3, sticky=(W, E))

results = StringVar()

ttk.Label(mainframe, textvariable=results).grid(column=2, row=4, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=4, sticky=W)

ttk.Label(mainframe, text="mass:").grid(column=1, row=1, sticky=E)
ttk.Label(mainframe, text="kg").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="heigh:").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="m").grid(column=3, row=2, sticky=W)
ttk.Label(mainframe, text="BMS = ").grid(column=1, row=3, sticky=E)
ttk.Label(mainframe, text="kg/m^2").grid(column=3, row=3, sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

mass_entry.focus()
root.bind("<Return>", calculate)
root.mainloop()