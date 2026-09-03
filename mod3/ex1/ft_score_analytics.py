import sys


def usage_message() -> None:
    print(
        "No scores provided. Usage: "
        "python3 ft_score_analytics.py <score1> <score2> ..."
    )


def main() -> None:
    args = sys.argv[1:]
    argslen = len(args)
    print("=== Player Score Analytics ===")
    if (argslen == 0):
        usage_message()
        return
    scores = []
    for arg in args:
        try:
            score = int(arg)
            scores.append(score)
        except ValueError:
            print(f"Invalid parameter: '{arg}'")

    if len(scores) > 0:
        print(f"Scores processed: {scores}")

        print(f"Total players: {argslen}")

        total_score = sum(scores)
        print(f"Total score: {total_score}")

        average_score = float(total_score / argslen)
        print(f"Average score: {average_score:.1f}")

        high_score = max(scores)
        print(f"High score: {high_score}")

        low_score = min(scores)
        print(f"Low score: {low_score}")

        score_range = high_score - low_score
        print(f"Score range: {score_range}")
    else:
        usage_message()


if __name__ == "__main__":
    main()
