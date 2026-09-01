def input_temperature(temp_str: str) -> int:
    try:
        temp = int(temp_str)
        return temp
    except ValueError:
        if int(temp_str) > 40:
            raise ValueError(f"{int(temp_str)}°C is too hot for plants (max 40°C)")
        if int(temp_str) < 0:
            raise ValueError(f"{int(temp_str)}°C is too cold for plants (min 0°C)")


def test_temperature() -> None:
    print("Input data is '25'")
    try:
        test1 = input_temperature("25")
        print(f"Temperature is now {test1}°C")
    except ValueError:
        print(f"Caught input_temperature error: {ValueError}")

    print()
    print("Input data is 'abc'")
    try:
        test2 = input_temperature("abc")
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
