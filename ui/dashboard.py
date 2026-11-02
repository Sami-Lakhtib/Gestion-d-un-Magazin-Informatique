import tkinter as tk

from ui.add_client_window import ouvrir_ajout_client
from ui.add_product_window import ouvrir_ajout_produit
from ui.add_sale_window import ouvrir_ajout_vente
from ui.catalog_window import ouvrir_catalogue
from ui.restock_window import ouvrir_reapprovisionnement
from ui.sales_window import ouvrir_liste_ventes


class Dashboard:
    def __init__(self, services):
        self.services = services
        self.root = tk.Tk()
        self.root.title("Magasin Informatique - Tableau de Bord")
        self.root.geometry("400x680")
        self.root.minsize(400, 680)

        tk.Label(self.root, text="Tableau de Bord", font=("Arial", 16)).pack(pady=20)

        tk.Button(self.root, text="Ajouter un Client", command=self._ouvrir_client, width=30, height=2).pack(pady=5)
        tk.Button(self.root, text="Ajouter un Produit", command=self._ouvrir_produit, width=30, height=2).pack(pady=5)
        tk.Button(self.root, text="Reapprovisionner le Stock", command=self._ouvrir_reappro, width=30, height=2).pack(pady=5)
        tk.Button(self.root, text="Enregistrer une Vente", command=self._ouvrir_vente, width=30, height=2).pack(pady=5)
        tk.Button(self.root, text="Parcourir le Catalogue", command=self._ouvrir_catalogue, width=30, height=2).pack(pady=5)
        tk.Button(self.root, text="Liste des Ventes", command=self._ouvrir_ventes, width=30, height=2).pack(pady=5)
        tk.Button(self.root, text="Quitter", command=self.root.quit, width=30, height=2).pack(pady=20)

        self.alerts_frame = tk.Frame(self.root)
        self.alerts_frame.pack(fill="x", padx=20, pady=(0, 10))
        self.rafraichir_alertes()

    def run(self):
        self.root.mainloop()

    def rafraichir_alertes(self):
        for widget in self.alerts_frame.winfo_children():
            widget.destroy()

        alertes = self.services.produits.lister_en_alerte()
        if not alertes:
            tk.Label(self.alerts_frame, text="Aucun produit sous le seuil d'alerte.", fg="green").pack(anchor="w")
            return

        tk.Label(
            self.alerts_frame,
            text="Produits sous le seuil d'alerte :",
            fg="red",
            font=("Arial", 10, "bold"),
        ).pack(anchor="w")

        for produit in alertes:
            tk.Label(
                self.alerts_frame,
                text=f"- {produit.nom} : {produit.quantite_stock} (seuil {produit.seuil_alerte})",
                fg="red",
                wraplength=360,
                justify="left",
            ).pack(anchor="w")

    def _ouvrir_client(self):
        ouvrir_ajout_client(self.root, self.services)
        self.rafraichir_alertes()

    def _ouvrir_produit(self):
        ouvrir_ajout_produit(self.root, self.services)
        self.rafraichir_alertes()

    def _ouvrir_vente(self):
        ouvrir_ajout_vente(self.root, self.services)
        self.rafraichir_alertes()

    def _ouvrir_reappro(self):
        ouvrir_reapprovisionnement(self.root, self.services)
        self.rafraichir_alertes()

    def _ouvrir_catalogue(self):
        ouvrir_catalogue(self.root, self.services)
        self.rafraichir_alertes()

    def _ouvrir_ventes(self):
        ouvrir_liste_ventes(self.root, self.services)
        self.rafraichir_alertes()
