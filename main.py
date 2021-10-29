from controllers.load_championship import LoadChampionship
from controllers.menu import Menu
from models.championship import Championship
from helpers import random_generation, db_management
from tinydb import TinyDB



def main():
    # champ = PlayChampionship()

    # champ = LoadChampionship(db_management.championships_table.all()[0])
    # db_management.insert_random_players_in_db(8)
    # menu = Menu()
    # menu.display_home_menu()
    champ = Championship.unserialize(db_management.championships_table.all()[0])
    
    import pdb; pdb.set_trace()



    # champ.generate_first_round()
    # champ.enter_round_results(1)
    # champ.generate_next_round(2)
    # champ.enter_round_results(2)

    # champ.generate_next_round(3)
    # champ.enter_round_results(3)

    # champ.generate_next_round(4)
    # champ.enter_round_results(4)


if __name__ == "__main__":
    main()
