import tkinter as tk

from ui.widgets import afficher_tableau

COLONNES = [
    "id",
    "date",
    "client",
    "email",
    "produit",
    "quantite",
    "prix unitaire",
    "total",
]


def ouvrir_liste_ventes(parent_window, services):
    window = tk.Toplevel(parent_window)
    window.title("Ventes")
    window.geometry("900x500")
    window.resizable(True, True)

    tk.Label(window, text="Liste des ventes", anchor="center").pack(pady=(10, 10))

    lignes = []
    for vente in services.ventes.lister():
        lignes.append(
            [
                vente["id_vente"],
                vente["date_vente"],
                vente["client"],
                vente["email_client"],
                vente["produit"],
                vente["quantite"],
                vente["prix_unitaire"],
                vente["montant_total"],
            ]
        )

    if not lignes:
        tk.Label(window, text="Aucune vente enregistree.").pack(pady=20)
    else:
        afficher_tableau(window, COLONNES, lignes)

    window.wait_window()
