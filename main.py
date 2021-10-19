from controllers.play_championship import PlayChampionship, PLAYERS


def main():
    champ = PlayChampionship()
    champ.add_players(PLAYERS)
    print(champ.championship.players)
    champ.generate_first_round()
    print(champ.championship.rounds[0].matchs)


if __name__ == "__main__":
    main()
