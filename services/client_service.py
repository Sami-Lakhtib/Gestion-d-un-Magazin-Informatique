import sqlite3

from models.entities import Client
from repositories.client_repository import ClientRepository


class ClientService:
    def __init__(self, db):
        self.db = db
        self.repo = ClientRepository(db)

    def ajouter(self, nom, prenom, telephone, email, adresse):
        erreurs = self._valider(nom, prenom, telephone, email, adresse)
        if erreurs:
            return erreurs

        client = Client(None, nom, prenom, telephone, email, adresse)
        try:
            self.repo.insert(client)
            self.db.commit()
        except sqlite3.IntegrityError:
            return ["Cet email existe deja."]
        return []

    def _valider(self, nom, prenom, telephone, email, adresse):
        erreurs = []
        if (not nom) or len(nom) > 32:
            erreurs.append("-Nom invalide.")
        if (not prenom) or len(prenom) > 32:
            erreurs.append("-Prenom invalide")
        if (not telephone) or len(telephone) != 12:
            erreurs.append("-Numero de telephone invalide. (XXX YYY YYY YYY).")
        if (not email) or "@" not in email:
            erreurs.append("-Adresse e-mail invalide")
        if not adresse:
            erreurs.append("-Adresse invalide")
        return erreurs
