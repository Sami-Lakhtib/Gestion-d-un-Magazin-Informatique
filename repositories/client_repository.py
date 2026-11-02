from models.entities import Client


class ClientRepository:
    def __init__(self, db):
        self.db = db

    def insert(self, client: Client):
        self.db.conn.execute(
            """INSERT INTO client(nom, prenom, telephone, email, adresse)
               VALUES (?, ?, ?, ?, ?)""",
            (client.nom, client.prenom, client.telephone, client.email, client.adresse),
        )

    def find_by_email(self, email: str):
        row = self.db.conn.execute(
            "SELECT * FROM client WHERE email = ?",
            (email,),
        ).fetchone()
        return Client.from_row(row) if row else None
