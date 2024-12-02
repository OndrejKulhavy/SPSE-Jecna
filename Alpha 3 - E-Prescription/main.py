from src.data.db_manager import DatabaseManager
from src.logic.app import App


def main():
    db = DatabaseManager()
    App(db)


if __name__ == '__main__':
    main()
