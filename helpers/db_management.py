from tinydb import TinyDB, Query
from models.player import Player
from views import view
from helpers import random_generation

db = TinyDB('db.json', sort_keys=True, indent=4, separators=(',', ': '))
players_table = db.table("Players table")
championships_table = db.table("Championships table")


PlayerQuery = Query()


def insert_random_players_in_db(number_of_players):
    for player in random_generation.generate_players(number_of_players):
        players_table.insert(Player.player_to_dict(player))


def add_player():

    add_player_view = view.View()
    first_name = add_player_view.prompt_for_player_first_name()
    last_name = add_player_view.prompt_for_player_last_name()
    birth_date = add_player_view.prompt_for_player_birth_date()
    sex = add_player_view.prompt_for_player_sex()
    rank = add_player_view.prompt_for_player_rank()

    player = Player(first_name, last_name, birth_date, sex, rank)

    return players_table.insert(player.serialize())


def modify_player(player_id):

    modify_player_view = view.View()

    player = players_table.get(doc_id=int(player_id))

    if player is not None:

        player_object = Player()
        player_object.unserialize(player)

        player_object.first_name = modify_player_view.prompt_for_player_first_name()
        player_object.last_name = modify_player_view.prompt_for_player_last_name()
        player_object.birth_date = modify_player_view.prompt_for_player_birth_date()
        player_object.sex = modify_player_view.prompt_for_player_sex()
        player_object.rank = modify_player_view.prompt_for_player_rank()

        players_table.update(player_object.serialize(),
                             doc_ids=[int(player_id)])

    else:
        print("Player does not exist")


def delete_player(player_id):
    players_table.remove(doc_ids=[int(player_id)])


def return_player_id(first_name):
    return players_table.get(PlayerQuery.first_name == first_name).doc_id


def save_championship(champ_dict):
    championships_table.insert(champ_dict)

