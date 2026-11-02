import tkinter as tk

from ui.widgets import afficher_message

WIDGET_WIDTH = 50
NOM, CATEGORIE, PRIX_ACHAT, PRIX_VENTE, QUANTITE_STOCK, SEUIL_ALERTE, DESCRIPTION = range(7)


def _entier_si_chiffres(valeur):
    return int(valeur) if valeur.isdigit() else None


def ouvrir_ajout_produit(parent_window, services):
    window = tk.Toplevel(parent_window)
    window.title("Ajout de produit")
    window.geometry("700x700")
    window.minsize(700, 700)
    window.maxsize(700, 700)

    text_vars = [tk.StringVar(window) for _ in range(7)]

    tk.Label(window, text="Ajout de produit").pack(pady=(10, 40))

    tk.Label(window, text="Nom:", width=WIDGET_WIDTH, anchor="w").pack(anchor="center")
    tk.Entry(window, width=WIDGET_WIDTH, textvariable=text_vars[NOM]).pack(pady=(0, 20))

    tk.Label(window, text="Categorie:", width=WIDGET_WIDTH, anchor="w").pack(anchor="center")
    tk.Entry(window, width=WIDGET_WIDTH, textvariable=text_vars[CATEGORIE]).pack(pady=(0, 20))

    tk.Label(window, text="Prix achat:", width=WIDGET_WIDTH, anchor="w").pack(anchor="center")
    tk.Entry(window, width=WIDGET_WIDTH, textvariable=text_vars[PRIX_ACHAT]).pack(pady=(0, 20))

    tk.Label(window, text="Prix vente:", width=WIDGET_WIDTH, anchor="w").pack(anchor="center")
    tk.Entry(window, width=WIDGET_WIDTH, textvariable=text_vars[PRIX_VENTE]).pack(pady=(0, 20))

    tk.Label(window, text="Quantite en stock:", width=WIDGET_WIDTH, anchor="w").pack(anchor="center")
    tk.Entry(window, width=WIDGET_WIDTH, textvariable=text_vars[QUANTITE_STOCK]).pack(pady=(0, 20))

    tk.Label(window, text="Seuil d'alerte:", width=WIDGET_WIDTH, anchor="w").pack(anchor="center")
    tk.Entry(window, width=WIDGET_WIDTH, textvariable=text_vars[SEUIL_ALERTE]).pack(pady=(0, 20))

    tk.Label(window, text="Description:", width=WIDGET_WIDTH, anchor="w").pack(anchor="center")
    tk.Entry(window, width=WIDGET_WIDTH, textvariable=text_vars[DESCRIPTION]).pack(pady=(0, 20))

    def enregistrer():
        erreurs = services.produits.ajouter(
            text_vars[NOM].get().strip(),
            text_vars[CATEGORIE].get().strip(),
            _entier_si_chiffres(text_vars[PRIX_ACHAT].get()),
            _entier_si_chiffres(text_vars[PRIX_VENTE].get()),
            _entier_si_chiffres(text_vars[QUANTITE_STOCK].get()),
            _entier_si_chiffres(text_vars[SEUIL_ALERTE].get()),
            text_vars[DESCRIPTION].get().strip(),
        )
        if erreurs:
            afficher_message(window, "\n".join(erreurs))
        else:
            afficher_message(window, "Produit enregistre avec succes!", fermer_fenetre=True)

    tk.Button(window, text="Enregistrer", width=25, height=2, command=enregistrer).pack(pady=(20, 0), anchor="center")
    window.wait_window()
