class Plant:
  def __init__(
      self,
      name: str,
      height: float,
      age: int
    ):
      self._name = name
      self._height = height
      self._days_old = age
      self._day = 0

  def show(self) -> None:
    print(f"Plant created: {self._name}: {round(self._height)}cm, {self._days_old} days old")

  def age(self) -> None:
     self._days_old += 1
     self._day += 1

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
     print(f"Height updated: {round(self._height)}cm")

  def set_age(self, age: int) -> None:
     if age < 0:
        print(f"{self._name}: Error, age can't be negative")
        print("Age update rejected")
        return
     self._days_old = age
     print(f"Age updated: {self._days_old} days")


def main() -> None:
  print("=== Garden Security System ===")
  rose = Plant("Rose", 25.1, 10)
  rose.show()

  print()
  rose.set_height(50)
  rose.set_age(50)
  print()

  rose.set_height(-5)
  rose.set_age(-10)

  print(f"\nCurrent state: {rose.get_name()}: {round(rose.get_height(), 1)}cm, {rose.get_age()} days old")


if __name__ == "__main__":
  main()
