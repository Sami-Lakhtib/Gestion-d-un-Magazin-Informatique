import tkinter as tk

from ui.widgets import afficher_message, creer_liste_deroulante

WIDGET_WIDTH = 50


def ouvrir_ajout_vente(parent_window, services):
    window = tk.Toplevel(parent_window)
    window.title("Enregistrement de vente")
    window.geometry("700x500")
    window.minsize(700, 500)
    window.maxsize(700, 500)

    noms_produits = [produit.nom for produit in services.produits.lister()]
    produit_var = tk.StringVar()
    client_var = tk.StringVar()
    quantite_var = tk.StringVar()

    tk.Label(window, text="Enregistrement de vente").pack(pady=(10, 40))

    tk.Label(window, text="Produit:", width=WIDGET_WIDTH, anchor="w").pack(anchor="center")
    if noms_produits:
        creer_liste_deroulante(window, noms_produits, produit_var, width=WIDGET_WIDTH).pack(pady=(0, 20))
    else:
        tk.Label(window, text="Aucun produit enregistre.", fg="red").pack(pady=(0, 20))

    tk.Label(window, text="Adresse e-mail du client:", width=WIDGET_WIDTH, anchor="w").pack(anchor="center")
    tk.Entry(window, textvariable=client_var, width=WIDGET_WIDTH).pack(pady=(0, 20))

    tk.Label(window, text="Quantite:", width=WIDGET_WIDTH, anchor="w").pack(anchor="center")
    tk.Entry(window, textvariable=quantite_var, width=WIDGET_WIDTH).pack(pady=(0, 20))

    def confirmer():
        if not noms_produits:
            afficher_message(window, "-Aucun produit enregistre.")
            return

        quantite_texte = quantite_var.get().strip()
        quantite = int(quantite_texte) if quantite_texte.isdigit() else None
        erreurs = services.ventes.enregistrer(
            produit_var.get().strip(),
            client_var.get().strip(),
            quantite,
        )
        if erreurs:
            afficher_message(window, "\n".join(erreurs))
        else:
            afficher_message(window, "Vente enregistree avec succes!", fermer_fenetre=True)

    tk.Button(window, text="Confirmer", width=25, height=2, command=confirmer).pack(pady=(20, 0), anchor="center")
    window.wait_window()
