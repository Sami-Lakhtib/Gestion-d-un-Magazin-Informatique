if __name__ == "__main__":
    exit(1)

import tkinter
from modules.entities import Client

WIDGET_WIDTH = 50
NOM = 0
PRENOM = 1
TEL = 2
MAIL = 3
AD = 4

def save_client(window: tkinter.Tk, vars: list[tkinter.StringVar], cursor):
        nom = vars[NOM].get().strip()
        prenom = vars[PRENOM].get().strip()
        tel = vars[TEL].get().replace(" ", "")
        mail = vars[MAIL].get().replace(" ", "")
        ad = vars[AD].get().strip()
        
        errorString = ""
        
        if (not nom) or len(nom) > 32:
            errorString += "-Nom invalide.\n"
        if (not prenom) or len(prenom) > 32:
            errorString += "-Prenom invalide\n"
        if (not tel) or len(tel) != 12:
            errorString += "-Numero de telephone invalide. (XXX YYY YYY YYY).\n"
        if (not mail) or not mail.find("@"):
            errorString += "-Adresse e-mail invalide\n"
        if not ad:
            errorString += "-Adresse invalide\n"
        
        if errorString:
            errorLabel = tkinter.Label(window, text=errorString, justify='left')
            errorLabel.pack(anchor='center', pady=(10, 0))
            window.after(2000, errorLabel.destroy)
        else:
            Client(None, nom, prenom, tel, mail, ad).saveToDatabase(cursor)
            successLabel = tkinter.Label(window, text="Client cree avec succes!", justify='center')
            successLabel.pack(anchor='center', pady=(10, 0))
            window.after(2000, window.destroy)
        
def main(cursor):  


    window = tkinter.Tk("Magazin Informatique")
    window.geometry("700x600")
    window.minsize(700, 600)
    window.maxsize(700, 600)
    
    textVars = [tkinter.StringVar(window) for i in range(5)]

    tkinter.Label(window, text="Ajout de client").pack(pady=(10, 40))


    tkinter.Label(window, text="Nom:", width=WIDGET_WIDTH, anchor='w').pack(anchor='center')
    Nom = tkinter.Entry(window, width=WIDGET_WIDTH, textvariable=textVars[NOM])
    Nom.pack(pady=(0, 20))

    tkinter.Label(window, text="Prenom:", width=WIDGET_WIDTH, anchor='w').pack(anchor='center')
    tkinter.Entry(window, width=WIDGET_WIDTH, textvariable=textVars[PRENOM]).pack(pady=(0, 20))

    tkinter.Label(window, text="Telephone:", width=WIDGET_WIDTH, anchor='w').pack(anchor='center')
    tkinter.Entry(window, width=WIDGET_WIDTH, textvariable=textVars[TEL]).pack(pady=(0, 20))

    tkinter.Label(window, text="Email:", width=WIDGET_WIDTH, anchor='w').pack(anchor='center')
    tkinter.Entry(window, width=WIDGET_WIDTH, textvariable=textVars[MAIL]).pack(pady=(0, 20))

    tkinter.Label(window, text="Adresse:", width=WIDGET_WIDTH, anchor='w').pack(anchor='center')
    tkinter.Entry(window, width=WIDGET_WIDTH, textvariable=textVars[AD]).pack(pady=(0, 20))


    SubmitButton = tkinter.Button(window, text="Soumettre", width=25, height=2, command=lambda: save_client(window, textVars, cursor))
    SubmitButton.pack(pady=(20,0), anchor='center')


    window.mainloop()