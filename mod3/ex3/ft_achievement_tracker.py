import random

achievements: set[str] = [
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
    'Sharp Mind'
]
set_achievements = {
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
    'Sharp Mind'
}

def gen_player_achievements() -> set[str]:

    return set(random.choices(
        achievements, k = random.randrange(1, 13)
        ))


def main() -> None:
    print("=== Achievement Tracker System ===")
    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()

    # print(f"\nPlayer Alice: {alice}")
    # print(f"Player Bob: {bob}")
    # print(f"Player Charlie: {charlie}")
    # print(f"Player Dylan: {dylan}")

    all_achievements = set()
    all_achievements.union(achievements)
    print(
        "\nAll distinct achievements: "
        f"{all_achievements}"
        )

    # print(f"\nCommon achievements: {set_achievements.intersection(alice, bob, charlie, dylan)}")

    # print(f"\nOnly Alice has: {alice.difference(bob, charlie, dylan)}")
    # print(f"Only Bob has: {bob.difference(alice, charlie, dylan)}")
    # print(f"Only Charlie has: {charlie.difference(alice, bob, dylan)}")
    # print(f"Only Dylan has: {dylan.difference(alice, bob, charlie)}")

    # print(f"\nAlice is missing: {set_achievements.difference(alice)}")
    # print(f"Bob is missing: {set_achievements.difference(bob)}")
    # print(f"Charlie is missing: {set_achievements.difference(charlie)}")
    # print(f"Dylan is missing: {set_achievements.difference(dylan)}")


if __name__ == "__main__":
    main()
