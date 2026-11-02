import sqlite3

from models.entities import Produit
from repositories.produit_repository import ProduitRepository


class ProduitService:
    def __init__(self, db):
        self.db = db
        self.repo = ProduitRepository(db)

    def lister(self):
        return self.repo.find_all()

    def lister_en_alerte(self):
        return self.repo.find_en_alerte()

    def reapprovisionner(self, nom_produit, quantite):
        if not quantite or quantite <= 0:
            return ["-Quantite invalide."]

        produit = self.repo.find_by_nom(nom_produit)
        if not produit:
            return ["-Aucun produit trouve."]

        self.repo.update_stock(produit.id_produit, produit.quantite_stock + quantite)
        self.db.commit()
        return []

    def ajouter(self, nom, categorie, prix_achat, prix_vente, quantite_stock, seuil_alerte, description):
        erreurs = self._valider(
            nom, categorie, prix_achat, prix_vente, quantite_stock, seuil_alerte, description
        )
        if erreurs:
            return erreurs

        produit = Produit(
            None, nom, categorie, prix_achat, prix_vente, quantite_stock, seuil_alerte, description
        )
        try:
            self.repo.insert(produit)
            self.db.commit()
        except sqlite3.IntegrityError:
            return ["Ce nom de produit existe deja."]
        return []

    def _valider(self, nom, categorie, prix_achat, prix_vente, quantite_stock, seuil_alerte, description):
        erreurs = []
        if (not nom) or len(nom) > 64:
            erreurs.append("-Nom invalide.")
        if (not categorie) or len(categorie) > 32:
            erreurs.append("-Categorie invalide.")
        if prix_achat is None or prix_achat < 0:
            erreurs.append("-Prix d'achat invalide.")
        if prix_vente is None or prix_vente < 0:
            erreurs.append("-Prix de vente.")
        if quantite_stock is None:
            erreurs.append("-Quantite de Stock invalide.")
        if seuil_alerte is None:
            erreurs.append("-Seuil d'alerte invalide.")
        return erreurs
