from models.round import Round
from models.player import Player
NUMBER_OF_ROUNDS = 4


class Championship:
    def __init__(self, name="", location="", date="", timecontrol="", description="", number_of_rounds=NUMBER_OF_ROUNDS) -> None:
        self.name = name
        self.location = location
        self.date = date
        self.number_of_rounds = number_of_rounds
        self.rounds = [
            Round(f"Round{round_number+1}") for round_number
            in range(number_of_rounds)]
        self.players = []
        self.timecontrol = timecontrol
        self.description = description

    def serialize(self):
        championship = {}
        championship['name'] = self.name
        championship['location'] = self.location
        championship['number_of_rounds'] = self.number_of_rounds
        championship['rounds'] = [self.rounds[round_number].serialize()
                                  for round_number in range(len(self.rounds))]
        championship['players'] = [self.players[player_number].serialize()
                                   for player_number in range(len(self.players))]
        championship['time_control'] = self.timecontrol
        championship['description'] = self.description
        return championship

    @staticmethod
    def unserialize(champ_dict):
        
        champ = Championship()
        champ.name = champ_dict['name']
        champ.location = champ_dict['location']
        champ.number_of_rounds = champ_dict['number_of_rounds']

        champ.rounds = [Round.unserialize(round)
                        for round in champ_dict['rounds']]
        champ.players = [Player.unserialize(player)
                         for player in champ_dict['players']]
        champ.timecontrol = champ_dict['time_control']
        champ.description = champ_dict['description']
        return champ

    def show_results(self):
        players_final_score = []
        for player in self.players:
            player_score = 0
            for round in self.rounds:
                for chess_match in round.matchs:
                    if player.name == chess_match.player1[0]:
                        player_score = player_score + int(chess_match.player1[1])
                    elif player.name == chess_match.player2[0]:
                        player_score = player_score + int(chess_match.player2[1])
            players_final_score.append([player.name, player_score])
        
        return players_final_score
                    

