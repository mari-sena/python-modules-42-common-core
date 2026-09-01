def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp > 40:
        raise ValueError(
            f"{temp}°C is too hot for plants (max 40°C)"
        )
    if temp < 0:
        raise ValueError(
            f"{temp}°C is too cold for plants (min 0°C)"
        )
    return temp


def test_temperature() -> None:
    print("Input data is '25'")
    try:
        test1 = input_temperature("25")
        print(f"Temperature is now {test1}°C")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")

    print()
    print("Input data is 'abc'")
    try:
        input_temperature("abc")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")

    print()
    print("Input data is '100'")
    try:
        input_temperature("100")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")

    print()
    print("Input data is '-50'")
    try:
        input_temperature("-50")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")

    print()
    print("All testes completed - program didn't crash!")


def main() -> None:
    print("=== Garden Temperature ===")
    print()
    test_temperature()


if __name__ == "__main__":
    main()
