if __name__ == "__main__":
    exit(0)

from datetime import date
import tkinter
from sqlite3 import Cursor
from modules.entities import Produit, Client, Vente

WIDGET_WIDTH = 50
PRODUCT = 0
CLIENT = 1
QUANTITY = 2

def save_sale(window: tkinter.Tk, inputs: list[tkinter.StringVar], cursor: Cursor):
    nomProduit = inputs[PRODUCT].get().strip()
    mailClient = inputs[CLIENT].get().strip()
    quantite = (int(inputs[QUANTITY].get().strip()) if inputs[QUANTITY].get().isdigit() else None)
    
    errorString = ""
    
    cursor.execute("SELECT * FROM produit WHERE nom = ?", tuple({nomProduit}))
    row_p = cursor.fetchone()
    
    cursor.execute("SELECT * FROM client WHERE email LIKE ?", tuple({mailClient}))
    row_c = cursor.fetchone()

    produit, client = None, None

    if not row_p:
        errorString += "-Aucun client trouve.\n"
    else:
        produit = Produit(row_p["id_produit"], row_p["nom"], row_p["categorie"], row_p["prix_achat"],
                    row_p["prix_vente"], row_p["quantite_stock"], row_p["seuil_alerte"], row_p["description"]
                )
        
    if not row_c:
        errorString += "-Aucun produit trouve.\n"
    else:
        client = Client(row_c["id_client"], row_c["nom"], row_c["prenom"],
                    row_c["telephone"], row_c["email"], row_c["adresse"]
                )
    
    if not quantite:
        errorString += "-Quantite invalide.\n"
    else:
        if produit and client:
            if quantite > produit.quantite_stock:
                errorString += "-Quantite en stock insuffisante.\n"
    
    
    if errorString:
        errorLabel = tkinter.Label(window, text=errorString, justify='left')
        errorLabel.pack(anchor='center', pady=(10, 0))
        window.after(2000, errorLabel.destroy)
    else:
        Vente(None, client.id_client, produit.id_produit, quantite, date.today().strftime("%d-%m-%y"), produit.prix_vente, quantite * produit.prix_vente).saveToDatabase(cursor)
        produit.quantite_stock -= quantite
        produit.editStock(cursor)
        
        successLabel = tkinter.Label(window, text="Vente enregistree avec succes!", justify='center')
        successLabel.pack(anchor='center', pady=(10, 0))
        window.after(2000, window.destroy)
        
        
    



def main(cursor: Cursor):
    
    window = tkinter.Tk("Magazin Informatique")
    window.geometry("700x700")
    window.minsize(700, 700)
    window.maxsize(700, 700)
    
    inputs = [tkinter.StringVar() for i in range(3)]    

    tkinter.Label(window, text="Naviguez le catalogue").pack(anchor='center')
    
    tkinter.Label(window, text="Nom de produit:", width=WIDGET_WIDTH, anchor='w').pack(anchor='center', pady=(10, 10))
    tkinter.Entry(window, textvariable=inputs[PRODUCT], width=WIDGET_WIDTH).pack(anchor='center', pady=(0, 10))
    
    tkinter.Label(window, text="Adresse e-mail du client:", width=WIDGET_WIDTH, anchor='w').pack(anchor='center', pady=(10, 10))
    tkinter.Entry(window, textvariable=inputs[CLIENT], width=WIDGET_WIDTH).pack(anchor='center', pady=(0, 10))
    
    tkinter.Label(window, text="Quantite:", width=WIDGET_WIDTH, anchor='w').pack(anchor='center', pady=(10, 10))
    tkinter.Entry(window, textvariable=inputs[QUANTITY], width=WIDGET_WIDTH).pack(anchor='center', pady=(0,10))
    
    SubmitButton = tkinter.Button(window, text="Confirmer", width=25, height=2, command=lambda: save_sale(window, inputs, cursor))
    SubmitButton.pack(pady=(20,0), anchor='center')
    
    window.mainloop()