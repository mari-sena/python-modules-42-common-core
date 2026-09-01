class Plant:
    def __init__(
        self,
        name: str,
        starting_height: float,
        starting_age: int,
        daily_growth: float = 2.0
    ) -> None:
        self.name = name
        self.height = starting_height
        self.days_old = starting_age
        self.daily_growth = daily_growth

        print(
            f"Created: {self.name}: "
            f"{self.height:.1f}cm, "
            f"{self.days_old} days old"
        )

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.days_old} days old")

    def grow(self) -> None:
        self.height += self.daily_growth

    def age(self) -> None:
        self.days_old += 1


def main() -> None:
    print("=== Plant Factory Output ===")

    plants = [
        Plant("Rose", 25.0, 30),
        Plant("Oak", 200.0, 365),
        Plant("Cactus", 5.0, 90),
        Plant("Sunflower", 80.0, 45),
        Plant("Fern", 15.0, 120),
    ]

    for plant in plants:
        plant.grow()
        plant.age()
        plant.show()


if __name__ == "__main__":
    main()
