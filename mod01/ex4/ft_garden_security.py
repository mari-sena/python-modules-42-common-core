#!/usr/bin/env python3


class Plant:
    def __init__(
        self,
        name: str,
        height: float,
        days_old: int
    ) -> None:
        self._name = name
        self._height = 0.0
        self._days_old = 0
        self.set_height(height)
        self.set_age(days_old)
        print(
            f"Plant created: {self._name}: "
            f"{round(self._height, 1)}cm, "
            f"{self._days_old} days old"
        )

    def show(self) -> None:
        print(
            f"{self._name}: "
            f"{round(self._height, 1)}cm, "
            f"{self._days_old} days old"
        )

    def age(self) -> None:
        self._days_old += 1

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._days_old

    def get_name(self) -> str:
        return self._name

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
            return
        self._height = height

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
            return
        self._days_old = age


def main() -> None:
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)

    print()
    rose.set_height(25.0)
    print(f"Height updated: {round(rose.get_height())}cm")
    rose.set_age(30)
    print(f"Age updated: {rose.get_age()} days")

    print()
    rose.set_height(-5)
    rose.set_age(-10)

    print(
        f"\nCurrent state: {rose.get_name()}: "
        f"{rose.get_height()}cm, "
        f"{rose.get_age()} days old"
    )


if __name__ == "__main__":
    main()
