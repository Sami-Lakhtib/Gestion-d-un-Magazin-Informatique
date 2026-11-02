class Client:
    def __init__(self, id_client, nom, prenom, telephone, email, adresse):
        self.id_client = id_client
        self.nom = nom
        self.prenom = prenom
        self.telephone = telephone
        self.email = email
        self.adresse = adresse

    @classmethod
    def from_row(cls, row):
        return cls(
            row["id_client"],
            row["nom"],
            row["prenom"],
            row["telephone"],
            row["email"],
            row["adresse"],
        )


class Produit:
    def __init__(self, id_produit, nom, categorie, prix_achat, prix_vente, quantite_stock, seuil_alerte, description):
        self.id_produit = id_produit
        self.nom = nom
        self.categorie = categorie
        self.prix_achat = prix_achat
        self.prix_vente = prix_vente
        self.quantite_stock = quantite_stock
        self.seuil_alerte = seuil_alerte
        self.description = description

    @classmethod
    def from_row(cls, row):
        return cls(
            row["id_produit"],
            row["nom"],
            row["categorie"],
            row["prix_achat"],
            row["prix_vente"],
            row["quantite_stock"],
            row["seuil_alerte"],
            row["description"],
        )

    @property
    def en_alerte(self):
        return self.quantite_stock <= self.seuil_alerte

    def valeurs_catalogue(self):
        return [
            self.id_produit,
            self.nom,
            self.categorie,
            self.prix_achat,
            self.prix_vente,
            self.quantite_stock,
            self.seuil_alerte,
            self.description,
        ]


class Vente:
    def __init__(self, id_vente, id_client, id_produit, quantite, date_vente, prix_unitaire, montant_total):
        self.id_vente = id_vente
        self.id_client = id_client
        self.id_produit = id_produit
        self.quantite = quantite
        self.date_vente = date_vente
        self.prix_unitaire = prix_unitaire
        self.montant_total = montant_total

    @classmethod
    def from_row(cls, row):
        return cls(
            row["id_vente"],
            row["id_client"],
            row["id_produit"],
            row["quantite"],
            row["date_vente"],
            row["prix_unitaire"],
            row["montant_total"],
        )
