import sqlite3


conn = sqlite3.connect("magazin.db")
conn.row_factory = sqlite3.Row

cursor = conn.cursor()

cursor.executescript("""
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS client(
    id_client INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    prenom TEXT NOT NULL,
    telephone TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    adresse TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS produit(
    id_produit INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT UNIQUE NOT NULL,
    categorie TEXT NOT NULL,
    prix_achat REAL NOT NULL,
    prix_vente REAL NOT NULL,
    quantite_stock INTEGER NOT NULL,
    seuil_alerte INTEGER NOT NULL,
    description TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS vente(
    id_vente INTEGER PRIMARY KEY AUTOINCREMENT,
    id_client INTEGER REFERENCES client(id_client),
    id_produit INTEGER REFERENCES produit(id_produit),
    quantite INTEGER NOT NULL,
    date_vente TEXT NOT NULL,
    prix_unitaire REAL NOT NULL,
    montant_total REAL NOT NULL
);
""") 