
class Player:

    count = 0

    def __init__(self, first_name, last_name, birth_date, sex, rank) -> None:
        self.id = Player.count
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.sex = sex
        self.rank = rank
        Player.count += 1
