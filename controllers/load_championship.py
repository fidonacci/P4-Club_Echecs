from models.championship import Championship
from views.view import View


class LoadChampionship:
    def __init__(self, db_championship) -> None:
        self.view = View()

        self.championship = Championship.unserialize(db_championship)
