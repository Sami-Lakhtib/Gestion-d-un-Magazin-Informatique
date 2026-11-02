import tkinter as tk


def afficher_tableau(parent, colonnes, lignes, couleur_ligne=None):
    frame = tk.Frame(parent)
    frame.pack(anchor="center", pady=(10, 10))

    for i, titre in enumerate(colonnes):
        tk.Label(
            frame,
            text=titre,
            anchor="w",
            justify="left",
            borderwidth=2,
            relief="solid",
            bg="black",
            fg="white",
            width=12,
            pady=5,
            padx=5,
        ).grid(row=0, column=i, sticky="nsew")

    for i, ligne in enumerate(lignes):
        bg = couleur_ligne(ligne) if couleur_ligne else "lightblue"
        for j, valeur in enumerate(ligne):
            tk.Label(
                frame,
                text=str(valeur),
                anchor="w",
                justify="left",
                borderwidth=1,
                relief="solid",
                width=12,
                pady=5,
                padx=5,
                bg=bg,
            ).grid(row=i + 1, column=j, sticky="nsew")

    return frame


def afficher_message(window, texte, duree_ms=2000, fermer_fenetre=False):
    label = tk.Label(window, text=texte, justify="left")
    label.pack(anchor="center", pady=(10, 0))
    if fermer_fenetre:
        window.after(duree_ms, window.destroy)
    else:
        window.after(duree_ms, label.destroy)
