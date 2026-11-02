import tkinter as tk

from ui.widgets import afficher_tableau

COLONNES = [
    "id",
    "nom",
    "categorie",
    "prix d'achat",
    "prix de vente",
    "quantite en stock",
    "seuil d'alerte",
    "description",
]


def ouvrir_catalogue(parent_window, services):
    window = tk.Toplevel(parent_window)
    window.title("Catalogue")
    window.geometry("900x500")
    window.resizable(True, True)

    tk.Label(window, text="Voir le catalogue", anchor="center").pack(pady=(10, 10))
    tk.Label(
        window,
        text="Lignes rouges : stock inferieur ou egal au seuil d'alerte",
        fg="red",
        anchor="center",
    ).pack(pady=(0, 10))

    lignes = [produit.valeurs_catalogue() for produit in services.produits.lister()]

    def couleur_ligne(ligne):
        quantite_stock, seuil_alerte = ligne[5], ligne[6]
        return "#f8b4b4" if quantite_stock <= seuil_alerte else "lightblue"

    afficher_tableau(window, COLONNES, lignes, couleur_ligne)
    window.wait_window()
