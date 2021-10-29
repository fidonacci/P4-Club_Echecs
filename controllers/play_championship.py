from models.chess_match import ChessMatch
from models.championship import Championship
from models.player import Player
from views import view

NUMBER_OF_PLAYERS = 4
PLAYERS = [("Fahd", "JAMAI", "30/07/1987", "Male", 1500),
           ("Asmaa", "SENHADJI", "31/08/1987", "Female", 1300),
           ("Sadi", "JAMAI", "21/05/2021", "Male", 1100),
           ("Ali", "JAMAI", "", "Male", 900),
           ("Nanno", "JAMAI", "30/07/1987", "Male", 800),
           ("Lola", "SENHADJI", "31/08/1987", "Female", 700),
           ("Fidou", "JAMAI", "21/05/2021", "Male", 500),
           ("Plitou", "JAMAI", "", "Male", 300)]


class PlayChampionship:
    def __init__(self) -> None:
        self.view = view.View()
        championship_name = self.view.prompt_for_championship_name()
        championship_location = self.view.prompt_for_championship_location()
        championship_date = self.view.prompt_for_championship_date()
        championship_time_control = self.view.menu_championship_time_controle()
        championship_description = self.view.\
            prompt_for_championship_description()

        self.championship = Championship(
            championship_name,
            championship_location,
            championship_date,
            championship_time_control,
            championship_description)

    def add_player(self, player: Player):
        player_object = Player.unserialize(player)

        if player_object in self.championship.players:
            return print("Player already added to this Championship ! ")
        else:
            self.championship.players.append(player_object)
            return None

    def generate_first_round(self):

        players_grid = sorted(self.championship.players,
                              key=lambda player: int(player.rank),
                              reverse=True)

        first_half_grid = players_grid[:int(len(players_grid)/2)]

        second_half_grid = players_grid[int(len(players_grid)/2):]

        for position in range(len(first_half_grid)):
            chess_match = ChessMatch([first_half_grid[position].name, ""],
                          [second_half_grid[position].name, ""])

            self.championship.rounds[0].matchs.append(chess_match)

    def find_player_by_name(self, name):
        players = self.championship.players
        return next(
            player for player in players
            if player.name == name)

    def enter_round_results(self, round_number):

        self.view.prompt_for_round_results(round_number)

        for chess_match in self.championship.rounds[round_number-1].matchs:
            player1_name = self.find_player_by_name(chess_match.player1[0]).name
            player2_name = self.find_player_by_name(chess_match.player2[0]).name

            match_description = f"{player1_name} to {player2_name}"

            chess_match.player1[1] = self.view.prompt_for_match_result_player1(
                match_description)

            chess_match.player2[1] = self.view.prompt_for_match_result_player2(
                match_description)

    def rank_grid(self, round_number):
        current_round = self.championship.rounds[round_number-1]
        round_players = []

        for chess_match in current_round.matchs:
            round_players.append(chess_match.player1 +
                                 [self.find_player_by_name(chess_match.player1[0])
                                     .rank])
            round_players.append(chess_match.player2 +
                                 [self.find_player_by_name(chess_match.player2[0])
                                     .rank])

        sorted_round_players = sorted(
            round_players, key=lambda player:
            (player[1], player[2]), reverse=True)

        return sorted_round_players

    def extract_players(self, matchs):
        matchs_players = []
        for chess_match in matchs:
            matchs_players.append([chess_match[0][0], chess_match[1][0]])
        return matchs_players

    def generate_next_round(self, round_number):

        ranked_grid = self.rank_grid(round_number-1)

        while len(ranked_grid) > 0:

            player_position = 1
            first_player = ranked_grid[0]
            second_player = ranked_grid[player_position]

            match_players_to_verify1 = [first_player[0], second_player[0]]
            match_players_to_verify2 = [second_player[0], first_player[0]]

            for round in self.championship.rounds:
                if match_players_to_verify1 in \
                        self.extract_players(round.matchs)\
                        or match_players_to_verify2 in \
                        self.extract_players(round.matchs):
                    player_position += 1

            print(round_number)
            print(ranked_grid)
            print(first_player)
            print(second_player)
            ranked_grid.remove(first_player)
            ranked_grid.remove(second_player)

            self.championship.rounds[round_number-1].matchs \
                .append(ChessMatch([first_player[0], 0], [second_player[0], 0]))
