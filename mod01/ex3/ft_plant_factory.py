class Plant:
  def __init__(
    self,
    name: str,
    starting_height: float,
    starting_age: int,
    daily_growth: float = 2.0
  ):
    self.name = name
    self.height = starting_height
    self.days_old = starting_age
    self.daily_growth = daily_growth

  def show(self):
    print(f"{self.name}: {round(self.height)}cm, {self.days_old} days old")
  
  def grow(self):
    self.height += self.daily_growth

  def age(self):
    self.days_old += 1

	
def main() -> None:
  print("=== Plant Factory Output ===")

  plant_data = [
    {"name": "Rose", "starting_height": 25, "starting_age": 30, "daily_growth": 1.5},
    {"name": "Tulip", "starting_height": 10, "starting_age": 5, "daily_growth": 0.8},
    {"name": "Sunflower", "starting_height": 15, "starting_age": 12, "daily_growth": 3.0},
    {"name": "Cactus", "starting_height": 8, "starting_age": 40, "daily_growth": 0.2},
    {"name": "Bamboo", "starting_height": 50, "starting_age": 20, "daily_growth": 5.0},
  ]

  plants = []

  for data in plant_data:
    plant = Plant(
      data["name"],
      data["starting_height"],
      data["starting_age"],
      data.get("daily_growth", 2.0)
    )
    plants.append(plant)

  for plant in plants:
    plant.grow()
    plant.age()
    plant.show()


if __name__ == "__main__":
  main()
