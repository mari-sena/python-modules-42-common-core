from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._data: list[tuple[int, str]] = []
        self._next_rank: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._data:
            raise IndexError("No data available")
        return self._data.pop(0)

    def _store(self, value: str) -> None:
        self._data.append((self._next_rank, value))
        self._next_rank += 1


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if type(data) in (int, float):
            return True
        if isinstance(data, list):
            return all(type(item) in (int, float) for item in data)
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")

        values = data if isinstance(data, list) else [data]

        for value in values:
            self._store(str(value))


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(item, str) for item in data)
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")

        values = data if isinstance(data, list) else [data]

        for value in values:
            self._store(value)


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return all(
                isinstance(key, str) and isinstance(value, str)
                for key, value in data.items()
            )

        if isinstance(data, list):
            return all(
                isinstance(entry, dict)
                and all(
                    isinstance(key, str) and isinstance(value, str)
                    for key, value in entry.items()
                )
                for entry in data
            )
        return False

    def ingest(
        self, data: dict[str, str] | list[dict[str, str]]
    ) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")

        entries = data if isinstance(data, list) else [data]

        for entry in entries:
            self._store(": ".join(entry.values()))


def main() -> None:
    print("=== Code Nexus - Data Processor ===")

    print("\nTesting Numeric Processor...")
    numeric = NumericProcessor()

    print(f" Trying to validate input '42': {numeric.validate(42)}")
    print(
        f" Trying to validate input 'Hello': "
        f"{numeric.validate('Hello')}"
    )
    print(" Test invalid ingestion of string 'foo' without prior validation:")
    try:
        numeric.ingest("foo")
    except ValueError as error:
        print(f" Got exception: {error}")

    numbers = [1, 2, 3, 4, 5]
    print(f" Processing data:{numbers} ")
    numeric.ingest(numbers)

    print(" Extracting 3 values...")
    for _ in range(3):
        rank, value = numeric.output()
        print(f" Numeric value {rank}: {value}")

    print("\nTesting Text Processor...")
    text = TextProcessor()

    print(f" Trying to validate input '42': {text.validate(42)}")

    words = ["Hello", "Nexus", "World"]
    text.validate(words)
    print(f" Processing data: {words}")
    text.ingest(words)

    print(" Extracting 1 value...")
    rank, value = text.output()
    print(f" Text value {rank}: {value}")

    print("\nTesting Log Processor...")
    logs = LogProcessor()

    print(
        " Trying to validate input 'Hello': "
        f"{logs.validate('Hello')}"
    )

    entries = [
        {
            "log_level": "NOTICE",
            "log_message": "Connection to server"
        },
        {
            "log_level": "ERROR",
            "log_message": "Unauthorized access!!"
        }
    ]

    logs.validate(entries)
    print(f" Processing data: {entries}")
    logs.ingest(entries)
    print(" Extracting 2 values...")
    for _ in range(2):
        rank, value = logs.output()
        print(f" Log entry {rank}: {value}")


if __name__ == "__main__":
    main()
