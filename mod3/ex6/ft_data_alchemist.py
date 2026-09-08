import random


def main() -> None:
    print("=== Game Data Alchemist ===")

    players = [
        'Alice',
        'bob',
        'Charlie',
        'dylan',
        'Emma',
        'Gregory',
        'john',
        'kevin',
        'Liam'
    ]
    print(f"Initial list of players: {players}")

    capitalized_list = [player.capitalize() for player in players]
    print(f"New list with all names capitalized: {capitalized_list}")

    capitalized_only = [p for p in players if p == p.capitalize()]
    print(f"New list of capitalized names only: {capitalized_only}\n")

    score_dict = {
        player: random.randrange(0, 1000)
        for player in capitalized_only
    }
    print(f"Score dict: {score_dict}")

    score_dict = [s for s in score_dict.values()]
    score_average = sum(score_dict) / len(score_dict)
    print(f"Score average is {score_average}")

    high_scores = {
        player: [score_dict]
        for player in score_dict
        if score_dict[player] > score_average
    }
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
