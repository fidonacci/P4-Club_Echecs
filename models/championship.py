from models.round import Round
NUMBER_OF_ROUNDS = 4


class Championship:
    def __init__(self, name, location, date,
                 number_of_rounds=NUMBER_OF_ROUNDS) -> None:
        self.name = name
        self.location = location
        self.number_of_rounds = number_of_rounds
        self.rounds = []
        for round_number in range(number_of_rounds):
            self.rounds.append(Round(f"Round{round_number+1}"))
        self.players = []
        self.time_control = ""
        self.description = ""
