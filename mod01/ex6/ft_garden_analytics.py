#!/usr/bin/env python3
class Plant:
    class _Stats:
        def __init__(self):
            self.grow = 0
            self.age = 0
            self.show = 0

        def __str__(self):
            return (f"Stats: {self.grow} grow, "
                    f"{self.age} age, {self.show} show")

    def __init__(
        self,
        name: str,
        age: int = 0,
        height: float = 0.0
    ):
        self.name = name
        self.age = age
        self.height = height
        self._stats = Plant._Stats()

    def show(self):
        self._stats.show += 1
        print(
            f"{self.name}: {self.height:.1f}cm, "
            f"{self.age} days old"
        )

    def _display_stats(self):
        print(f"[statistics for {self.name}]")
        print(self._stats)

    def grow(self, centimeters: float):
        self.height += centimeters
        self._stats.grow += 1


class Flower(Plant):
    def __init__(self, name, height=0.0, age=0, color="unknown"):
        super().__init__(name, age, height)
        self.color = color
        self.bloomed = False

    def show(self):
        super().show()
        print(f" Color: {self.color}")
        if self.bloomed:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name}: has not bloomed yet")

    def bloom(self):
        self.bloomed = True


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


if __name__ == "__main__":
    main()
