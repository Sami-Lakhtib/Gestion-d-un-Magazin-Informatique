if __name__ == "__main__":
    exit(1)
    
import tkinter
from sqlite3 import Cursor

product_fields = ["id", "nom", "categorie", "prix d'achat", "prix de vente", "quantite en stock", "seuil d'alerte", "description"]

def main(parent_window, cursor: Cursor):
    window = tkinter.Toplevel(parent_window)
    window.title("Catalogue")
    window.geometry("700x700")
    window.resizable(True, True)
    
    tkinter.Label(window, text="Voir le catalogue", anchor='center').pack(pady=(10, 10))
    
    frame = tkinter.Frame(window)
    frame.pack(anchor='center', pady=(10, 10))
    
    
    for i, f in enumerate(product_fields):
        tkinter.Label(frame, text=str(f),
                      anchor='w', justify='left', borderwidth=2, relief='solid', bg="black", fg="white",
                      width=10, pady=5, padx=5).grid(row=0, column=i, columnspan=1, sticky='nsew')


    cursor.execute("SELECT * FROM produit;")

    for i, row in enumerate(cursor):
        for j, data in enumerate(row):
            tkinter.Label(frame, text=str(data), anchor='w', justify='left', borderwidth=1, relief='solid', width=10, pady=5, padx=5, bg='lightblue').grid(row=i + 1, column=j, columnspan=1, sticky='nsew')
    
    
    window.mainloop()