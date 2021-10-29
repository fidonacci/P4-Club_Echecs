from simple_term_menu import TerminalMenu


class View:
    def __init__(self) -> None:
        pass

    def prompt_for_championship_name(self):
        return input(4*"\n" + "Championship name: ")

    def prompt_for_championship_location(self):
        return input("Championship location: ")

    def prompt_for_championship_date(self):
        return input("Championship date: ")

    def prompt_for_championship_description(self):
        return input("Championship description: ")

    def prompt_for_player_first_name(self):
        return input("Player first name: ")

    def prompt_for_player_last_name(self):
        return input("Player last name: ")

    def prompt_for_player_birth_date(self):
        return input("Player birth date: ")

    def prompt_for_player_sex(self):
        return input("Player sex: ")

    def prompt_for_player_rank(self):
        while True:
            try:
                rank = int(input("Player rank: "))
                return rank
            except ValueError as e:
                print("Not a proper integer! Try it again")

        
        
        
    def prompt_for_round_results(self, round_number):
        return print(4*"\n" + f"ROUND {round_number}" + "\n"
                     + "########################################")

    def prompt_for_match_result_player1(self, match_description):
        return input(f"Match opposing {match_description}" +
                     "  ----  Player1 score: ")

    def prompt_for_match_result_player2(self, match_description):
        return input(f"Match opposing {match_description} " +
                     " ----  Player2 score: ")

    def home_menu(self):
        options = ["Start New Championship", "Load Championship", "Reports", "Exit"]
        terminal_menu = TerminalMenu(options, title="Home Menu")
        menu_entry_index = terminal_menu.show()
        return options[menu_entry_index]

    def reports_menu(self):
        options = ["Display Championships",
                   "Display Players List", "Back to Home Menu"]
        terminal_menu = TerminalMenu(options, title="Reports Menu")

        menu_entry_index = terminal_menu.show()

        return options[menu_entry_index]
    

    
    def show_players_list(self, players_list):
        print("\n-----------------------")
        print("Database Players List".upper())
        print("-----------------------")

        for player in players_list:
            print(f"Player ID : {player.doc_id} /// {str(player)} \n")

    def show_champ_players_list(self, players_list):
        print("\n-----------------------")
        print("Championship Players List".upper())
        print("-----------------------")

        for player in players_list:
            print(f"Player {str(player)} \n")
   
    def players_list_menu(self):
        
        options = ["Add Player",
                   "Modify Player", "Delete Player", "Back to Reports Menu"]
        
        terminal_menu = TerminalMenu(options, title="Players List Menu")

        menu_entry_index = terminal_menu.show()

        return options[menu_entry_index]  

    def championships_list_menu(self):
        options = ["Show Championship Players", "Back to Reports Menu"]
        
        terminal_menu = TerminalMenu(options, title="Championships List Menu")

        menu_entry_index = terminal_menu.show()

        return options[menu_entry_index]  

    def prompt_for_player_id(self):
        return input("Player id: ")

    
    def prompt_for_champ_id(self):
        return input("Championship id: ")

    def menu_for_championship_player_config(self):
       
        options = ["Select existing Player",
                   "Add new Player",]
        
        terminal_menu = TerminalMenu(options, title="Players List Menu")

        menu_entry_index = terminal_menu.show()

        return options[menu_entry_index]
    
    def menu_championship_time_controle(self):
       
        options = ["Bullet",
                   "Blitz","Rapid"]
        
        terminal_menu = TerminalMenu(options, title="Championship Time Control")

        menu_entry_index = terminal_menu.show()

        return options[menu_entry_index]
    
    def show_championships_list(self, championships_list):
        print("\n-----------------------")
        print("Database Championships List".upper())
        print("-----------------------")

        for championship in championships_list:
            print(f"Player ID : {championship.doc_id} /// {str(championship['name'])} \n")