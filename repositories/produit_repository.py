from models.entities import Produit


class ProduitRepository:
    def __init__(self, db):
        self.db = db

    def insert(self, produit: Produit):
        self.db.conn.execute(
            """INSERT INTO produit(nom, categorie, prix_achat, prix_vente, quantite_stock, seuil_alerte, description)
               VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (
                produit.nom,
                produit.categorie,
                produit.prix_achat,
                produit.prix_vente,
                produit.quantite_stock,
                produit.seuil_alerte,
                produit.description,
            ),
        )

    def find_all(self):
        rows = self.db.conn.execute("SELECT * FROM produit ORDER BY id_produit").fetchall()
        return [Produit.from_row(row) for row in rows]

    def find_by_nom(self, nom: str):
        row = self.db.conn.execute(
            "SELECT * FROM produit WHERE nom = ?",
            (nom,),
        ).fetchone()
        return Produit.from_row(row) if row else None

    def find_en_alerte(self):
        rows = self.db.conn.execute(
            """SELECT * FROM produit
               WHERE quantite_stock <= seuil_alerte
               ORDER BY nom"""
        ).fetchall()
        return [Produit.from_row(row) for row in rows]

    def update_stock(self, id_produit: int, quantite_stock: int):
        self.db.conn.execute(
            """UPDATE produit
               SET quantite_stock = ?
               WHERE id_produit = ?""",
            (quantite_stock, id_produit),
        )
