import tkinter as tk

from ui.widgets import afficher_message, creer_liste_deroulante

WIDGET_WIDTH = 50


def ouvrir_reapprovisionnement(parent_window, services):
    window = tk.Toplevel(parent_window)
    window.title("Reapprovisionnement")
    window.geometry("700x400")
    window.minsize(700, 400)
    window.maxsize(700, 400)

    noms_produits = [produit.nom for produit in services.produits.lister()]
    nom_var = tk.StringVar()
    quantite_var = tk.StringVar()

    tk.Label(window, text="Ajouter du stock").pack(pady=(10, 40))

    tk.Label(window, text="Produit:", width=WIDGET_WIDTH, anchor="w").pack(anchor="center")
    if noms_produits:
        creer_liste_deroulante(window, noms_produits, nom_var, width=WIDGET_WIDTH).pack(pady=(0, 20))
    else:
        tk.Label(window, text="Aucun produit enregistre.", fg="red").pack(pady=(0, 20))

    tk.Label(window, text="Quantite a ajouter:", width=WIDGET_WIDTH, anchor="w").pack(anchor="center")
    tk.Entry(window, width=WIDGET_WIDTH, textvariable=quantite_var).pack(pady=(0, 20))

    def confirmer():
        if not noms_produits:
            afficher_message(window, "-Aucun produit enregistre.")
            return

        texte = quantite_var.get().strip()
        quantite = int(texte) if texte.isdigit() else None
        erreurs = services.produits.reapprovisionner(nom_var.get().strip(), quantite)
        if erreurs:
            afficher_message(window, "\n".join(erreurs))
        else:
            afficher_message(window, "Stock mis a jour avec succes!", fermer_fenetre=True)

    tk.Button(window, text="Confirmer", width=25, height=2, command=confirmer).pack(pady=(20, 0), anchor="center")
    window.wait_window()
