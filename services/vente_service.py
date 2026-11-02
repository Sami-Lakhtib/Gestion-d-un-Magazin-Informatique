from datetime import date

from models.entities import Vente
from repositories.client_repository import ClientRepository
from repositories.produit_repository import ProduitRepository
from repositories.vente_repository import VenteRepository


class VenteService:
    def __init__(self, db):
        self.db = db
        self.clients = ClientRepository(db)
        self.produits = ProduitRepository(db)
        self.ventes = VenteRepository(db)

    def lister(self):
        return self.ventes.find_all_detaillees()

    def enregistrer(self, nom_produit, email_client, quantite):
        produit = self.produits.find_by_nom(nom_produit)
        client = self.clients.find_by_email(email_client)

        erreurs = []
        if not produit:
            erreurs.append("-Aucun produit trouve.")
        if not client:
            erreurs.append("-Aucun client trouve.")
        if not quantite:
            erreurs.append("-Quantite invalide.")
        elif produit and quantite > produit.quantite_stock:
            erreurs.append("-Quantite en stock insuffisante.")

        if erreurs:
            return erreurs

        vente = Vente(
            None,
            client.id_client,
            produit.id_produit,
            quantite,
            date.today().strftime("%d-%m-%y"),
            produit.prix_vente,
            quantite * produit.prix_vente,
        )
        self.ventes.insert(vente)
        self.produits.update_stock(produit.id_produit, produit.quantite_stock - quantite)
        self.db.commit()
        return []
