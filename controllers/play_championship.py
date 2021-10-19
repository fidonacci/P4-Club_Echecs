from models.match import Match
from models.championship import Championship
from models.player import Player
from views import view

NUMBER_OF_PLAYERS = 8
PLAYERS = [("Fahd", "JAMAI", "30/07/1987", "Male", 800),
           ("Asmaa", "SENHADJI", "31/08/1987", "Female", 890),
           ("Sadi", "JAMAI", "21/05/2021", "Male", 900),
           ("Ali", "JAMAI", "", "Male", 900)]


class PlayChampionship:
    def __init__(self) -> None:
        self.view = view.View()
        championship_name = self.view.prompt_for_championship_name()
        championship_location = self.view.prompt_for_championship_location()
        championship_date = self.view.prompt_for_championship_date()

        self.championship = Championship(
            championship_name, championship_location, championship_date)

    def add_players(self, players=None, number_of_players=NUMBER_OF_PLAYERS):

        if players is not None:
            for player in players:
                player = Player(player[0], player[1],
                                player[2], player[3], player[4])
                self.championship.players.append(player)

        else:
            print("ELSE")
            while number_of_players != 0:
                first_name = self.view.prompt_for_player_first_name()
                last_name = self.view.prompt_for_player_last_name()
                birth_date = self.view.prompt_for_player_birth_date()
                sex = self.view.prompt_for_player_sex()
                rank = self.view.prompt_for_player_rank()

                player = Player(first_name, last_name, birth_date, sex, rank)
                self.championship.players.append(player)
                number_of_players -= 1

    def generate_first_round(self):

        players_grid = sorted(self.championship.players, key=lambda player: player.rank)
       

        for player1 in players_grid[:int(len(players_grid)/2)]:
            

            print(player1.first_name)
            for player2 in players_grid[int(len(players_grid)/2)+1:]:
                
                match = Match([player1.id, 0],[player2.id, 0])
               
                import pdb; pdb.set_trace()

                self.championship.rounds[0].matchs.append(match)
