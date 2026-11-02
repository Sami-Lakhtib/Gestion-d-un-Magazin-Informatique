from services.client_service import ClientService
from services.produit_service import ProduitService
from services.vente_service import VenteService


class Services:
    def __init__(self, db):
        self.db = db
        self.clients = ClientService(db)
        self.produits = ProduitService(db)
        self.ventes = VenteService(db)
