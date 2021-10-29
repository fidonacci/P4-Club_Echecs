from controllers import play_championship
from views import view
from models.player import Player
from helpers import db_management


class Menu():

    def __init__(self) -> None:
        self.view = view.View()

    def display_home_menu(self):

        user_input = self.view.home_menu()

        if user_input == "Start New Championship":

            champ = play_championship.PlayChampionship()

            while len(champ.championship.players) < 8:

                play_input = self.view.menu_for_championship_player_config()

                if play_input == "Select existing Player":
                    self.view.show_players_list(
                        db_management.players_table.all())

                    while True:
                        try:
                            player_id = self.view.prompt_for_player_id()
                            int(player_id)
                            break
                        except ValueError:
                            print("Enter a valid id number")

                    player_object = db_management.players_table.get(
                        doc_id=int(player_id))

                    champ.add_player(player_object)

                elif play_input == "Add new Player":
                    player_id = db_management.add_player()
                    player_object = Player()
                    player_object.unserialize(
                        db_management.players_table.get(doc_id=int(player_id)))
                    champ.add_player(player_object)

            champ.generate_first_round()
            champ.enter_round_results(1)
            champ.generate_next_round(2)
            champ.enter_round_results(2)

            champ.generate_next_round(3)
            champ.enter_round_results(3)

            champ.generate_next_round(4)
            champ.enter_round_results(4)

            db_management.save_championship(champ.championship.serialize())

        elif user_input == "Reports":
            self.display_reports_menu()

        elif user_input == "Exit":

            return None

        return None

    def display_reports_menu(self):

        user_input = self.view.reports_menu()

        if user_input == "Back to Home Menu":
            self.display_home_menu()
        elif user_input == "Display Players List":
            self.display_players_list()
        elif user_input == "Display Championships":
            self.display_championships_list()

        return None

    def display_players_list(self):

        self.view.show_players_list(db_management.players_table.all())

        user_input = self.view.players_list_menu()

        if user_input == "Back to Reports Menu":
            self.display_reports_menu()
        elif user_input == "Add Player":
            db_management.add_player()
            self.display_players_list()
        elif user_input == "Modify Player":
            player_id = self.view.prompt_for_player_id()
            db_management.modify_player(player_id)
            self.display_players_list()
        elif user_input == "Delete Player":
            player_id = self.view.prompt_for_player_id()
            db_management.delete_player(player_id)
            self.display_players_list()

        return None

    def display_championships_list(self):

        self.view.show_championships_list(
            db_management.championships_table.all())

        user_input = self.view.championships_list_menu()

        if user_input == "Back to Reports Menu":
            self.display_reports_menu()
        elif user_input == "Show Championship Players":
            while True:
                try:
                    champ_id = self.view.prompt_for_champ_id()
                    int(champ_id)
                    break
                except ValueError:
                    print("Enter a valid id number")

            self.view.show_champ_players_list(
                db_management.championships_table.get(doc_id=int(champ_id))['players'])
            self.display_championships_list()

        return None
