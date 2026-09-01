class Plant:
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        daily_growth: float
    ) -> None:
        self.name = name
        self.height = height
        self.days_old = age
        self.daily_growth = daily_growth
        self.day = 0

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.days_old} days old")

    def grow(self) -> None:
        self.height += self.daily_growth

    def age(self) -> None:
        self.days_old += 1
        self.day += 1


def main() -> None:
    print("=== Garden Plant Growth ===")

    rose = Plant("Rose", 25, 30, 0.8)
    initial_height = rose.height
    rose.show()

    for _ in range(7):
        rose.grow()
        rose.age()

        print(f"=== Day {rose.day} ===")
        rose.show()
    total_growth = round(rose.height - initial_height, 1)
    print(f"Growth this week: {total_growth}cm")


if __name__ == "__main__":
    main()
