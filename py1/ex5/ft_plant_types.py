#!/usr/bin/env python3


class Plant:
    def __init__(
        self,
        name: str,
        height: float = 0.0,
        days_old: int = 0
    ) -> None:
        self._name = name
        self._height = height
        self._days_old = days_old

    def grow(self, amount: float = 1.0) -> None:
        self._height += amount

    def age(self, days: int = 1) -> None:
        self._days_old += days

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm, {self._days_old} days old")


class Flower(Plant):
    def __init__(
        self,
        name: str,
        height: float = 0.0,
        days_old: int = 0,
        color: str = "unknown"
    ) -> None:
        super().__init__(name, height, days_old)
        self.color = color
        self.bloomed = False

    def bloom(self) -> None:
        self.bloomed = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self.bloomed:
            print(f" {self._name} is blooming beautifully!")
        else:
            print(f" {self._name} has not bloomed yet")


class Tree(Plant):
    def __init__(
        self,
        name: str,
        height: float = 0.0,
        days_old: int = 0,
        trunk_diameter: float = 0.0
    ) -> None:
        super().__init__(name, height, days_old)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(
            f"Tree {self._name} now produces a shade of "
            f"{self._height:.1f}cm long and "
            f"{self.trunk_diameter:.1f}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter:.1f}cm")


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: float = 0.0,
        days_old: int = 0,
        harvest_season: str = "Unknown",
    ) -> None:
        super().__init__(name, height, days_old)
        self.harvest_season = harvest_season
        self.nutritional_value: float = 0

    def grow(self, amount: float = 1.0) -> None:
        super().grow(amount)
        self.nutritional_value += 0.5

    def age(self, days: int = 1) -> None:
        super().age(days)
        self.nutritional_value += 0.5

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {round(self.nutritional_value)}")


def main() -> None:
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()

    print()
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()

    print()
    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for _ in range(20):
        tomato.grow(2.1)
        tomato.age()
    tomato.show()


if __name__ == "__main__":
    main()
