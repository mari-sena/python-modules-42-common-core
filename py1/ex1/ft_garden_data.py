#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str, age: int, height: float) -> None:
        self.name = name
        self.age = age
        self.height = height

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")


def main() -> None:
    print("=== Garden Plant Registry ===")
    rose = Plant("Rose", 30, 25.0)
    sunflower = Plant("Sunflower", 45, 80.0)
    cactus = Plant("Cactus", 120, 15.0)

    rose.show()
    sunflower.show()
    cactus.show()


if __name__ == "__main__":
    main()
