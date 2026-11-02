from models.entities import Vente


class VenteRepository:
    def __init__(self, db):
        self.db = db

    def insert(self, vente: Vente):
        self.db.conn.execute(
            """INSERT INTO vente(id_client, id_produit, quantite, date_vente, prix_unitaire, montant_total)
               VALUES (?, ?, ?, ?, ?, ?)""",
            (
                vente.id_client,
                vente.id_produit,
                vente.quantite,
                vente.date_vente,
                vente.prix_unitaire,
                vente.montant_total,
            ),
        )

    def find_all_detaillees(self):
        return self.db.conn.execute(
            """SELECT v.id_vente,
                      v.date_vente,
                      c.prenom || ' ' || c.nom AS client,
                      c.email AS email_client,
                      p.nom AS produit,
                      v.quantite,
                      v.prix_unitaire,
                      v.montant_total
               FROM vente v
               JOIN client c ON c.id_client = v.id_client
               JOIN produit p ON p.id_produit = v.id_produit
               ORDER BY v.id_vente"""
        ).fetchall()
