from database import Database
from services import Services
from ui.dashboard import Dashboard


def main():
    db = Database()
    dashboard = Dashboard(Services(db))
    dashboard.run()
    db.close()


if __name__ == "__main__":
    main()
