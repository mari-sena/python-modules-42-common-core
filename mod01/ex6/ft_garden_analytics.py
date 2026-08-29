#!/usr/bin/env python3
class Plant:
    def __init__(
        self,
        name,
        age=0,
        height=0.0
    ):
        self.name = name
        self.age = age
        self.height = height

    def show(self):
        print(
            f"{self.name}: {self.height:.1f}cm, "
            f"{self.age} days old"
        )


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

    def statistics(self):
        print(f"[statistics for {self.name}]")


def main() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print("Is 30 days more than a year? -> False")
    print("Is 400 days more than a year? -> True")

    print()
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    rose.statistics()


if __name__ == "__main__":
    main()
