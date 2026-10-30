if __name__ == "__main__":
    exit(1)

import tkinter
from modules.entities import Produit

WIDGET_WIDTH = 50

NOM = 0
CATEGORIE = 1
PRIX_ACHAT = 2
PRIX_VENTE = 3
QUANTITE_STOCK = 4
SEUIL_ALERTE = 5
DESCRIPTION = 6

def save_product(window: tkinter.Tk, vars: list[tkinter.StringVar], cursor):
        nom = vars[NOM].get().strip()
        cat = vars[CATEGORIE].get().strip()
        pa = (float(vars[PRIX_ACHAT].get()) if vars[PRIX_ACHAT].get().isdigit() else None)
        pv = (float(vars[PRIX_VENTE].get()) if vars[PRIX_VENTE].get().isdigit() else None)
        qs = (int(vars[QUANTITE_STOCK].get()) if vars[QUANTITE_STOCK].get().isdigit() else None)
        seuil = (int(vars[SEUIL_ALERTE].get()) if vars[SEUIL_ALERTE].get().isdigit() else None)
        desc = vars[DESCRIPTION].get().strip()
        
        errorString = ""
        
        if (not nom) or len(nom) > 64:
            errorString += "-Nom invalide.\n"
        if (not cat) or len(cat) > 32:
            errorString += "-Categorie invalide.\n"
        if pa is None or pa < 0:
            errorString += "-Prix d'achat invalide.\n"
        if pv is None or pv < 0:
            errorString += "-Prix de vente.\n"
        if qs is None:
            errorString += "-Quantite de Stock invalide.\n"
        if seuil is None:
            errorString += "-Seuil d'alerte invalide.\n"            
        
        if errorString:
            errorLabel = tkinter.Label(window, text=errorString, justify='left')
            errorLabel.pack(anchor='center', pady=(10, 0))
            window.after(2000, errorLabel.destroy)
        else:
            Produit(None, nom, cat, pa, pv, qs, seuil, desc).saveToDatabase(cursor)
            successLabel = tkinter.Label(window, text="Produit enregistre avec succes!", justify='center')
            successLabel.pack(anchor='center', pady=(10, 0))
            window.after(2000, window.destroy)
        
def main(parent_window, cursor):  


    window = tkinter.Toplevel(parent_window)
    window.title("Ajout de produit")
    window.geometry("700x700")
    window.minsize(700, 700)
    window.maxsize(700, 700)
    
    textVars = [tkinter.StringVar(window) for i in range(7)]

    tkinter.Label(window, text="Ajout de produit").pack(pady=(10, 40))


    tkinter.Label(window, text="Nom:", width=WIDGET_WIDTH, anchor='w').pack(anchor='center')
    Nom = tkinter.Entry(window, width=WIDGET_WIDTH, textvariable=textVars[NOM])
    Nom.pack(pady=(0, 20))

    tkinter.Label(window, text="Categorie:", width=WIDGET_WIDTH, anchor='w').pack(anchor='center')
    tkinter.Entry(window, width=WIDGET_WIDTH, textvariable=textVars[CATEGORIE]).pack(pady=(0, 20))

    tkinter.Label(window, text="Prix achat:", width=WIDGET_WIDTH, anchor='w').pack(anchor='center')
    tkinter.Entry(window, width=WIDGET_WIDTH, textvariable=textVars[PRIX_ACHAT]).pack(pady=(0, 20))

    tkinter.Label(window, text="Prix vente:", width=WIDGET_WIDTH, anchor='w').pack(anchor='center')
    tkinter.Entry(window, width=WIDGET_WIDTH, textvariable=textVars[PRIX_VENTE]).pack(pady=(0, 20))

    tkinter.Label(window, text="Quantite en stock:", width=WIDGET_WIDTH, anchor='w').pack(anchor='center')
    tkinter.Entry(window, width=WIDGET_WIDTH, textvariable=textVars[QUANTITE_STOCK]).pack(pady=(0, 20))

    tkinter.Label(window, text="Seuil d'alerte:", width=WIDGET_WIDTH, anchor='w').pack(anchor='center')
    tkinter.Entry(window, width=WIDGET_WIDTH, textvariable=textVars[SEUIL_ALERTE]).pack(pady=(0, 20))

    tkinter.Label(window, text="Description:", width=WIDGET_WIDTH, anchor='w').pack(anchor='center')
    tkinter.Entry(window, width=WIDGET_WIDTH, textvariable=textVars[DESCRIPTION]).pack(pady=(0, 20))


    SubmitButton = tkinter.Button(window, text="Enregistrer", width=25, height=2, command=lambda: save_product(window, textVars, cursor))
    SubmitButton.pack(pady=(20,0), anchor='center')


    window.mainloop()
