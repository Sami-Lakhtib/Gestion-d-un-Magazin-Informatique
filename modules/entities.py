from sqlite3 import Cursor

class Client:
    def __init__(self, _id_client, _nom, _prenom, _telephone, _email, _adresse):
        self.id_client = _id_client
        self.nom = _nom
        self.prenom = _prenom
        self.telephone = _telephone
        self.email = _email
        self.adresse = _adresse
    
    def display(self):
        print(f"""
        id_client: {self.id_client}
        nom: {self.nom}
        prenom: {self.prenom}
        telephone: {self.telephone}
        email: {self.email}
        adresse: {self.adresse}
        """)
        
    def saveToDatabase(self, cursor: Cursor):
        cursor.execute(
            """INSERT INTO client(nom, prenom, telephone, email, adresse)
            VALUES (?, ?, ?, ?, ?)""",
            (self.nom, self.prenom, self.telephone, self.email, self.adresse)
        )


class Produit:
    def __init__(self, _id_produit, _nom, _categorie, _prix_achat, _prix_vente, _quantite_stock, _seuil_alerte, _description):
        self.id_produit = _id_produit
        self.nom = _nom
        self.categorie = _categorie
        self.prix_achat = _prix_achat
        self.prix_vente = _prix_vente
        self.quantite_stock = _quantite_stock
        self.seuil_alerte = _seuil_alerte
        self.description = _description
        
    def display(self):
        print(f"""
        id_produit: {self.id_produit}
        nom: {self.nom}
        categorie: {self.categorie}
        prix_achat: {self.prix_achat}
        prix_vente: {self.prix_vente}
        quantite_stock: {self.quantite_stock}
        seuil_alerte: {self.seuil_alerte}
        description: {self.description}
        """)
        
    def saveToDatabase(self, cursor: Cursor):
        cursor.execute(
            """INSERT INTO produit(nom, categorie, prix_achat, prix_vente, quantite_stock, seuil_alerte, description)
            VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (self.nom, self.categorie, self.prix_achat, self.prix_vente, self.quantite_stock, self.seuil_alerte, self.description)
        )
    
    def editStock(self, cursor: Cursor):
        cursor.execute(
            """UPDATE produit
            SET quantite_stock = ?
            WHERE id_produit = ? """,
        (self.quantite_stock, self.id_produit)
        )
       

class Vente:
    def __init__(self, _id_vente, _id_client, _id_produit, _quantite, _date_vente, _prix_unitaire, _montant_total):
        self.id_vente = _id_vente
        self.id_client = _id_client
        self.id_produit = _id_produit
        self.quantite = _quantite
        self.date_vente = _date_vente
        self.prix_unitaire = _prix_unitaire
        self.montant_total = _montant_total
        
    def display(self):
        print(f"""
        id_vente: {self.id_vente}
        id_client: {self.id_client}
        id_produit: {self.id_produit}
        quantite: {self.quantite}
        date_vente: {self.date_vente}
        prix_unitaire: {self.prix_unitaire}
        montant_total: {self.montant_total}
        """)
    
    def saveToDatabase(self, cursor: Cursor):
        cursor.execute(
            """INSERT INTO vente(id_client, id_produit, quantite, date_vente, prix_unitaire, montant_total)
            VALUES (?, ?, ?, ?, ?, ?)""",
            (self.id_client, self.id_produit, self.quantite, self.date_vente, self.prix_unitaire, self.montant_total)
        )


