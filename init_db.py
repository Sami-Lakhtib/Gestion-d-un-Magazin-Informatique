"""Initialise magazin.db avec des donnees de test.

A lancer depuis ce dossier :
    python init_db.py

Ecrase les donnees existantes (tables client, produit, vente).
"""

from database import Database

db = Database()

db.conn.executescript("""
PRAGMA foreign_keys = ON;
DELETE FROM vente;
DELETE FROM produit;
DELETE FROM client;
DELETE FROM sqlite_sequence;
""")

clients = [
    ("Ben Ali", "Ahmed", "216123456789", "ahmed.benali@email.com", "12 rue Habib Bourguiba, Tunis"),
    ("Trabelsi", "Sara", "216987654321", "sara.trabelsi@email.com", "45 avenue de France, Sfax"),
    ("Gharbi", "Youssef", "216555111222", "youssef.gharbi@email.com", "8 rue Ibn Khaldoun, Sousse"),
    ("Mansouri", "Ines", "216333444555", "ines.mansouri@email.com", "21 cite El Ghazala, Ariana"),
    ("Jaziri", "Karim", "216222333444", "karim.jaziri@email.com", "3 rue de la Liberte, Bizerte"),
    ("Hammami", "Lina", "216111222333", "lina.hammami@email.com", "17 boulevard 14 Janvier, Nabeul"),
]

produits = [
    ("PC Portable Lenovo IdeaPad", "Ordinateurs", 1200, 1599, 15, 5, "Intel i5, 8 Go RAM, 512 Go SSD"),
    ("PC Portable HP Pavilion", "Ordinateurs", 1400, 1899, 8, 3, "Intel i7, 16 Go RAM, 512 Go SSD"),
    ("Souris Logitech M185", "Peripheriques", 12, 25, 40, 10, "Souris sans fil USB"),
    ("Clavier mecanique Redragon", "Peripheriques", 45, 79, 20, 5, "Clavier RGB switches rouges"),
    ("Ecran Samsung 24 pouces", "Peripheriques", 180, 249, 12, 4, "Full HD 75 Hz"),
    ("SSD Kingston 1 To", "Composants", 55, 89, 25, 8, "SSD SATA 2.5 pouces"),
    ("RAM DDR4 16 Go", "Composants", 35, 59, 30, 10, "2x8 Go 3200 MHz"),
    ("Cable HDMI 2m", "Accessoires", 4, 12, 50, 15, "Cable HDMI haute vitesse"),
    ("Cle USB 64 Go", "Accessoires", 6, 15, 3, 5, "USB 3.0 - stock faible pour tests d'alerte"),
    ("Routeur TP-Link Archer", "Reseau", 40, 69, 10, 3, "Wi-Fi 6 double bande"),
]

ventes = [
    (1, 3, 2, "15-10-26", 25, 50),
    (2, 1, 1, "18-10-26", 1599, 1599),
    (3, 8, 3, "20-10-26", 12, 36),
    (4, 9, 2, "22-10-26", 15, 30),
    (1, 6, 1, "25-10-26", 89, 89),
    (5, 4, 1, "28-10-26", 79, 79),
]

db.conn.executemany(
    """INSERT INTO client(nom, prenom, telephone, email, adresse)
       VALUES (?, ?, ?, ?, ?)""",
    clients,
)
db.conn.executemany(
    """INSERT INTO produit(nom, categorie, prix_achat, prix_vente, quantite_stock, seuil_alerte, description)
       VALUES (?, ?, ?, ?, ?, ?, ?)""",
    produits,
)
db.conn.executemany(
    """INSERT INTO vente(id_client, id_produit, quantite, date_vente, prix_unitaire, montant_total)
       VALUES (?, ?, ?, ?, ?, ?)""",
    ventes,
)

db.commit()

n_clients = db.conn.execute("SELECT COUNT(*) FROM client").fetchone()[0]
n_produits = db.conn.execute("SELECT COUNT(*) FROM produit").fetchone()[0]
n_ventes = db.conn.execute("SELECT COUNT(*) FROM vente").fetchone()[0]
db.close()

print("Base de donnees initialisee : magazin.db")
print(f"  {n_clients} clients")
print(f"  {n_produits} produits")
print(f"  {n_ventes} ventes")
print("Relancer ce script ecrase les donnees et remet les valeurs de test.")
