import random


def get_achievements() -> list[str]:
    return [
        'Crafting Genius',
        'World Savior',
        'Master Explorer',
        'Collector Supreme',
        'Untouchable',
        'Boss Slayer',
        'Strategist',
        'Unstoppable',
        'Speed Runner',
        'Survivor',
        'Treasure Hunter',
        'First Steps',
        'Sharp Mind',
        'Hidden Path Finder'
    ]


def gen_player_achievements() -> set[str]:
    achievements = get_achievements()

    return set(random.sample(
        achievements, k=random.randrange(1, len(achievements) + 1)
        ))


def main() -> None:
    print("=== Achievement Tracker System ===")
    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()
    achievements = get_achievements()

    print(f"\nPlayer Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")

    distinct_achievements = alice.union(bob, charlie, dylan)
    print(
        "\nAll distinct achievements: "
        f"{distinct_achievements}"
        )

    common_achievements = alice.intersection(bob, charlie, dylan)
    print(f"\nCommon achievements: {common_achievements}")

    print(f"\nOnly Alice has: {alice.difference(bob, charlie, dylan)}")
    print(f"Only Bob has: {bob.difference(alice, charlie, dylan)}")
    print(f"Only Charlie has: {charlie.difference(alice, bob, dylan)}")
    print(f"Only Dylan has: {dylan.difference(alice, bob, charlie)}")

    set_achievements = set(achievements)
    print(f"\nAlice is missing: {set_achievements.difference(alice)}")
    print(f"Bob is missing: {set_achievements.difference(bob)}")
    print(f"Charlie is missing: {set_achievements.difference(charlie)}")
    print(f"Dylan is missing: {set_achievements.difference(dylan)}")


if __name__ == "__main__":
    main()
