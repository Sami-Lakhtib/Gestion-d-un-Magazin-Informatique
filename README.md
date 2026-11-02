# Gestion d'un Magasin Informatique

Petite application de **gestion de stock** pour un magasin informatique.

Stack : **Python 3**, **SQLite**, **Tkinter** (bibliothèque standard uniquement).

---

## Fonctionnalités

- Ajouter un client
- Ajouter un produit (prix, stock, seuil d'alerte)
- Réapprovisionner le stock
- Enregistrer une vente (le stock diminue automatiquement)
- Parcourir le catalogue (produits sous le seuil en rouge)
- Consulter la liste des ventes
- Alertes stock sur le tableau de bord (`quantite_stock <= seuil_alerte`)

Les produits à sélectionner (vente / réapprovisionnement) passent par une **liste déroulante**.

---

## Prérequis

- Python 3 installé (Tkinter inclus avec l'installation classique sous Windows)

Vérification :

```bash
python --version
```

---

## Lancement

Depuis le dossier du projet :

```bash
cd Gestion-d-un-Magazin-Informatique
python main.py
```

### Données de test

Pour (re)créer la base avec des clients, produits et ventes d'exemple :

```bash
python init_db.py
```

Ce script **écrase** les données existantes de `magazin.db`.

---

## Architecture

Le code est organisé en 3 couches :

| Couche | Dossier | Rôle |
|---|---|---|
| Interface | `ui/` | Fenêtres Tkinter |
| Métier | `services/` | Validation et règles (stock, alertes, ventes) |
| Données | `repositories/` | Requêtes SQL |
| Modèles | `models/` | Entités `Client`, `Produit`, `Vente` |

```
main.py                 # Point d'entrée
database.py             # Connexion SQLite + schéma
init_db.py              # Jeu de données de test
models/                 # Entités
repositories/           # Accès aux 3 tables
services/               # Logique métier
ui/                     # Interface graphique
```

Flux typique :

`UI` → `Service` → `Repository` → `magazin.db`

---

## Base de données

Fichier : `magazin.db`  
**3 tables** uniquement :

### `client`
`id_client`, `nom`, `prenom`, `telephone`, `email`, `adresse`

### `produit`
`id_produit`, `nom`, `categorie`, `prix_achat`, `prix_vente`, `quantite_stock`, `seuil_alerte`, `description`

### `vente`
`id_vente`, `id_client`, `id_produit`, `quantite`, `date_vente`, `prix_unitaire`, `montant_total`

Relations :
- une vente référence un client et un produit
- une vente diminue `quantite_stock`
- un réapprovisionnement augmente `quantite_stock`

---

## Utilisation rapide

1. Lancer `python init_db.py` puis `python main.py`
2. Consulter le catalogue et les alertes (ex. clé USB sous le seuil)
3. Enregistrer une vente via les listes déroulantes
4. Réapprovisionner un produit en alerte pour faire disparaître l'alerte

---

## Auteurs

Projet scolaire — gestion de stock magasin informatique.
