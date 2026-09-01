#!/usr/bin/env python3
class Plant:
    class _Stats:
        def __init__(self) -> None:
            self.grow = 0
            self.days_old = 0
            self.show = 0

        def __str__(self) -> str:
            return (f"Stats: {self.grow} grow, "
                    f"{self.days_old} age, {self.show} show")

    def __init__(
        self,
        name: str,
        days_old: int = 0,
        height: float = 0.0
    ) -> None:
        self.name = name
        self.days_old = days_old
        self.height = height
        self._stats = Plant._Stats()

    def show(self) -> None:
        self._stats.show += 1
        print(
            f"{self.name}: {self.height:.1f}cm, "
            f"{self.days_old} days old"
        )

    def _display_stats(self) -> None:
        print(self._stats)

    def grow(self, centimeters: float) -> None:
        self.height += centimeters
        self._stats.grow += 1


class Flower(Plant):
    def __init__(self, name: str, height: float = 0.0, days_old: int = 0, color: str = "unknown") -> None:
        super().__init__(name, days_old, height)
        self.color = color
        self.bloomed = False

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self.bloomed:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name}: has not bloomed yet")

    def bloom(self) -> None:
        self.bloomed = True


class Tree(Plant):
    def __init__(
        self,
        name: str,
        height: float = 0.0,
        days_old: int = 0,
        trunk_diameter: float = 0.0
    ):
        super().__init__(name, days_old, height)
        self.trunk_diameter = trunk_diameter
        self.shade = 0

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter:.1f}cm")

    def _display_stats(self) -> None:
        super()._display_stats()
        print(f" {self.shade} shade")

    def produce_shade(self) -> None:
        print(
            f"Tree {self.name} now produces "
            f"a shade of {self.height:.1f}cm long "
            f"and {self.trunk_diameter:.1f}cm wide."
        )
        self.shade += 1

def main() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print("Is 30 days more than a year? -> False")
    print("Is 400 days more than a year? -> True")

    print()
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    rose._display_stats()
    print(f"[asking the rose to grow and bloom]")
    rose.grow(8)
    rose.bloom()
    rose.show()
    rose._display_stats()

    print()
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print(f"[statistics for {oak.name}]")
    oak._display_stats()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print(f"[statistics for {oak.name}]")
    oak._display_stats()


    print()
    print("=== Seed")


    print()
    print("=== Anonymous")


if __name__ == "__main__":
    main()
