import tkinter as tk

from ui.widgets import afficher_message

WIDGET_WIDTH = 50
PRODUCT, CLIENT, QUANTITY = range(3)


def ouvrir_ajout_vente(parent_window, services):
    window = tk.Toplevel(parent_window)
    window.title("Enregistrement de vente")
    window.geometry("700x700")
    window.minsize(700, 700)
    window.maxsize(700, 700)

    inputs = [tk.StringVar() for _ in range(3)]

    tk.Label(window, text="Naviguez le catalogue").pack(anchor="center")

    tk.Label(window, text="Nom de produit:", width=WIDGET_WIDTH, anchor="w").pack(anchor="center", pady=(10, 10))
    tk.Entry(window, textvariable=inputs[PRODUCT], width=WIDGET_WIDTH).pack(anchor="center", pady=(0, 10))

    tk.Label(window, text="Adresse e-mail du client:", width=WIDGET_WIDTH, anchor="w").pack(anchor="center", pady=(10, 10))
    tk.Entry(window, textvariable=inputs[CLIENT], width=WIDGET_WIDTH).pack(anchor="center", pady=(0, 10))

    tk.Label(window, text="Quantite:", width=WIDGET_WIDTH, anchor="w").pack(anchor="center", pady=(10, 10))
    tk.Entry(window, textvariable=inputs[QUANTITY], width=WIDGET_WIDTH).pack(anchor="center", pady=(0, 10))

    def confirmer():
        quantite_texte = inputs[QUANTITY].get().strip()
        quantite = int(quantite_texte) if quantite_texte.isdigit() else None
        erreurs = services.ventes.enregistrer(
            inputs[PRODUCT].get().strip(),
            inputs[CLIENT].get().strip(),
            quantite,
        )
        if erreurs:
            afficher_message(window, "\n".join(erreurs))
        else:
            afficher_message(window, "Vente enregistree avec succes!", fermer_fenetre=True)

    tk.Button(window, text="Confirmer", width=25, height=2, command=confirmer).pack(pady=(20, 0), anchor="center")
    window.wait_window()
