class Plant:
    def __init__(self, name, height=0.0, age=0):
        self.name = name
        self.height = height
        self.age = age

    def grow(self, amount=1.0):
        self.height += amount

    def age_plant(self, days=1):
        self.age += days

    def show(self):
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")


class Flower(Plant):
    def __init__(self, name, height=0.0, age=0, color="unknown"):
        super().__init__(name, height, age)
        self.color = color
        self.bloomed = False

    def bloom(self):
        self.bloomed = True

    def show(self):
        super().show()
        print(f" Color: {self.color}")
        if self.bloomed:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(
        self,
        name,
        height=0.0,
        age=0,
        trunk_diameter=0.0
    ):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self.height:.1f}cm long and "
            f"{self.trunk_diameter:.1f}cm wide."
        )

    def show(self):
        print("=== Tree")
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter:.1f}cm")
        print(f"[asking the {self.name.lower()} to produce shade]")
        self.produce_shade()


class Vegetable(Plant):
    def __init__(
        self,
        name,
        height=0.0,
        age=0,
        harvest_season="Unknown",
        nutricional_value=0
    ):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutricional_value = nutricional_value

    def grow(self, amount=1.0):
        super().grow(amount)

    def age_plant(self, days=1):
        super().age_plant(days)
        self.nutricional_value += days

    def show(self):
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutricional value: {self.nutricional_value}")


def main() -> None:
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()

    print()
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()

    print()
    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April", 0)
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    tomato.grow(42)
    tomato.age_plant(20)
    tomato.show()


if __name__ == "__main__":
    main()
