class GardenError(Exception):
    def __init__(
            self,
            message: str = "Unknown garden error",
    ) -> None:
        Exception.__init__(self, message)


class PlantError(GardenError):
    def __init__(
            self,
            message: str = "Unknown plant error",
    ) -> None:
        GardenError.__init__(self, message)


class WaterError(GardenError):
    def __init__(
            self,
            message: str = "Unknown water error",
    ) -> None:
        GardenError.__init__(self, message)


def check_plant() -> None:
    raise PlantError("The tomato plant is wilting!")


def check_water() -> None:
    raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    print("Testing PlantError...")
    try:
        check_plant()
    except PlantError as error:
        print(f"Caught PlantError: {error}")

    print()
    print("Testing WaterError...")
    try:
        check_water()
    except WaterError as error:
        print(f"Caught WaterError: {error}")

    print()
    print("Testing catching all garden errors...")
    try:
        check_plant()
    except GardenError as error:
        print(f"Caught GardenError: {error}")

    try:
        check_water()
    except GardenError as error:
        print(f"Caught GardenError: {error}")

    print()
    print("All custom error types work correctly!")


def main() -> None:
    print("=== Custom Garden Errors Demo ===")
    print()
    test_custom_errors()


if __name__ == "__main__":
    main()
