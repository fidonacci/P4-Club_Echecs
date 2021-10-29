

class Player:

    count = 0

    def __init__(self, first_name="", last_name="", birth_date="", sex="", rank="") -> None:

        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.sex = sex
        self.rank = rank
        self.name = self.first_name + " " + self.last_name

    def serialize(self):

        player = {}
        player['first_name'] = self.first_name
        player['last_name'] = self.last_name
        player['birth_date'] = self.birth_date
        player['sex'] = self.sex
        player['rank'] = self.rank
        player['name'] = self.first_name + " "+ self.last_name


        return player

    def unserialize(player: dict):
        player_object = Player()
        player_object.first_name = player['first_name']
        player_object.last_name = player['last_name']
        player_object.birth_date = player['birth_date']
        player_object.sex = player['sex']
        player_object.rank = player['rank']
        player_object.name = player['first_name'] + " "+ player['last_name']

        return player_object


    def player_to_dict(player):

        player_object = Player(
            first_name=player[0], last_name=player[1], birth_date=player[2], sex=player[3], rank=player[4])
        player_dict = player_object.serialize()

        return player_dict
