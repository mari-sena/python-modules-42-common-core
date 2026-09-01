def input_temperature(temp_str: str) -> int:
    return int(temp_str)


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
    print("All testes completed - program didn't crash!")


def main() -> None:
    print("=== Garden Temperature ===")
    print()
    test_temperature()


if __name__ == "__main__":
    main()
