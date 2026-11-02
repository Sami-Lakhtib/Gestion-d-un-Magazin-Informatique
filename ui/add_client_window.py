import tkinter as tk

from ui.widgets import afficher_message

WIDGET_WIDTH = 50
NOM, PRENOM, TEL, MAIL, AD = range(5)


def ouvrir_ajout_client(parent_window, services):
    window = tk.Toplevel(parent_window)
    window.title("Ajout de client")
    window.geometry("700x600")
    window.minsize(700, 600)
    window.maxsize(700, 600)

    text_vars = [tk.StringVar(window) for _ in range(5)]

    tk.Label(window, text="Ajout de client").pack(pady=(10, 40))

    tk.Label(window, text="Nom:", width=WIDGET_WIDTH, anchor="w").pack(anchor="center")
    tk.Entry(window, width=WIDGET_WIDTH, textvariable=text_vars[NOM]).pack(pady=(0, 20))

    tk.Label(window, text="Prenom:", width=WIDGET_WIDTH, anchor="w").pack(anchor="center")
    tk.Entry(window, width=WIDGET_WIDTH, textvariable=text_vars[PRENOM]).pack(pady=(0, 20))

    tk.Label(window, text="Telephone:", width=WIDGET_WIDTH, anchor="w").pack(anchor="center")
    tk.Entry(window, width=WIDGET_WIDTH, textvariable=text_vars[TEL]).pack(pady=(0, 20))

    tk.Label(window, text="Email:", width=WIDGET_WIDTH, anchor="w").pack(anchor="center")
    tk.Entry(window, width=WIDGET_WIDTH, textvariable=text_vars[MAIL]).pack(pady=(0, 20))

    tk.Label(window, text="Adresse:", width=WIDGET_WIDTH, anchor="w").pack(anchor="center")
    tk.Entry(window, width=WIDGET_WIDTH, textvariable=text_vars[AD]).pack(pady=(0, 20))

    def soumettre():
        erreurs = services.clients.ajouter(
            text_vars[NOM].get().strip(),
            text_vars[PRENOM].get().strip(),
            text_vars[TEL].get().replace(" ", ""),
            text_vars[MAIL].get().replace(" ", ""),
            text_vars[AD].get().strip(),
        )
        if erreurs:
            afficher_message(window, "\n".join(erreurs))
        else:
            afficher_message(window, "Client cree avec succes!", fermer_fenetre=True)

    tk.Button(window, text="Soumettre", width=25, height=2, command=soumettre).pack(pady=(20, 0), anchor="center")
    window.wait_window()
