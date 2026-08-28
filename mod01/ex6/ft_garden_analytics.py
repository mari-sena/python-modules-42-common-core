#!/usr/bin/env python3
class Plant:
    def __init__(
        self,
        name,
        age,
        height=0.0
    ):
        self.name = name
        self.age = age
        self.height = height

    def show(self):
        print(
            f"{self.name}: {self.height}cm "
            f"{self.age} days old"
        )


class Flower(Plant):
    def __init__(self, name, height=0.0, age=0):
        super().__init__(name, age, height)

    def show():
        super().show()


def main() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print("Is 30 days more than a year? -> False")
    print("Is 400 days more than a year? -> True")

    print()
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10)
    rose.show()


if __name__ == "__main__":
    main()
