import tkinter as tk
import database as db
from actions import addClient, addProduct, addSale, browseCatalog


def open_add_client_window(parent_window, cursor):
    addClient.main(parent_window, cursor)

def open_add_product_window(parent_window, cursor):
    addProduct.main(parent_window, cursor)

def open_add_sale_window(parent_window, cursor):
    addSale.main(parent_window, cursor)

def open_browse_catalog_window(parent_window, cursor):
    browseCatalog.main(parent_window, cursor)


def main():
    root = tk.Tk()
    root.title("Magasin Informatique - Tableau de Bord")
    root.geometry("400x400")
    root.minsize(400, 400)
    root.maxsize(400, 400)

    tk.Label(root, text="Tableau de Bord", font=("Arial", 16)).pack(pady=20)

    # Bouton pour ajouter un client
    tk.Button(root, text="Ajouter un Client", command=lambda: open_add_client_window(root, db.cursor), width=30, height=2).pack(pady=5)

    # Bouton pour ajouter un produit
    tk.Button(root, text="Ajouter un Produit", command=lambda: open_add_product_window(root, db.cursor), width=30, height=2).pack(pady=5)

    # Bouton pour enregistrer une vente
    tk.Button(root, text="Enregistrer une Vente", command=lambda: open_add_sale_window(root, db.cursor), width=30, height=2).pack(pady=5)

    # Bouton pour parcourir le catalogue
    tk.Button(root, text="Parcourir le Catalogue", command=lambda: open_browse_catalog_window(root, db.cursor), width=30, height=2).pack(pady=5)

    # Bouton pour quitter
    tk.Button(root, text="Quitter", command=root.quit, width=30, height=2).pack(pady=20)

    root.mainloop()

    db.conn.commit()
    db.conn.close() # Close the database connection when the main window is closed


if __name__ == "__main__":
    main()