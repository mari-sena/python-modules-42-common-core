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

    score_dict = dict()
    for player in capitalized_list:
        score_dict.update({player: random.randrange(0, 1000)})
    print(f"Score dict: {score_dict}")

    score_list = [s for s in score_dict.values()]
    score_average = sum(score_list) / len(score_list)
    print(f"Score average is {score_average}")

    high_scores = [s for s in score_dict.values() if s > score_average]
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
