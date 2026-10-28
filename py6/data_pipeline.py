from typing import Protocol
from data_processor import NumericProcessor, TextProcessor, LogProcessor
from data_stream import DataStream as BaseDataStream


class ExportPlugin(Protocol):
    def process_output(
        self,
        data: list[tuple[int, str]]
    ) -> None:
        ...


class CSVExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        fields: list[str] = []

        for _, value in data:
            if any(char in value for char in (",", '"', "\n", "\r")):
                value = '"' + value.replace('"', '""') + '"'
            fields.append(value)

        print("CSV Output:")
        print(",".join(fields))


class JSONExportPlugin:
    @staticmethod
    def _escape(value: str) -> str:
        escaped = ""

        for char in value:
            if char == '"':
                escaped += '\\"'
            elif char == "\\":
                escaped += "\\\\"
            elif char == "\n":
                escaped += "\\n"
            elif char == "\r":
                escaped += "\\r"
            elif char == "\t":
                escaped += "\\t"
            elif ord(char) < 32:
                escaped += f"\\u{ord(char):04x}"
            else:
                escaped += char

        return escaped

    def process_output(self, data: list[tuple[int, str]]) -> None:
        items = [
            f'"item_{rank}": "{self._escape(value)}"'
            for rank, value in data
        ]

        print("JSON Output:")
        print("{" + ", ".join(items) + "}")


class DataStream(BaseDataStream):
    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        if nb < 0:
            raise ValueError("nb must be non-negative")

        for processor in self.processors:
            data: list[tuple[int, str]] = []

            for _ in range(nb):
                try:
                    data.append(processor.output())
                except IndexError:
                    break

            if data:
                plugin.process_output(data)


def main() -> None:
    print("=== Code Nexus - Data Pipeline ===")

    print("\nInitialize Data Stream...")
    data_stream = DataStream()
    data_stream.print_processors_stats()

    print("\nRegistering Processors")
    data_stream.register_processor(NumericProcessor())
    data_stream.register_processor(TextProcessor())
    data_stream.register_processor(LogProcessor())

    first_batch = [
            'Hello world',
            [3.14, -1, 2.71],
            [
                {
                    'log_level': 'WARNING',
                    'log_message': 'Telnet access! Use ssh instead'
                },
                {
                    'log_level': 'INFO',
                    'log_message': 'User wil isvconnected'
                }
            ],
            42,
            ['Hi', 'five']
        ]
    print(f"\nSend first batch of data on stream: {first_batch}")
    data_stream.process_stream(first_batch)
    print()
    data_stream.print_processors_stats()

    print("\nSend 3 processed data from each processor to a CSV plugin:")
    data_stream.output_pipeline(3, CSVExportPlugin())
    print()
    data_stream.print_processors_stats()

    second_batch = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {
                "log_level": "ERROR",
                "log_message": "500 server crash"
            },
            {
                "log_level": "NOTICE",
                "log_message": "Certificate expires in 10 days"
            }
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello"
    ]

    print(f"\nSend another batch of data: {second_batch}")
    data_stream.process_stream(second_batch)
    print()
    data_stream.print_processors_stats()

    print("\nSend 5 processed data from each processor to a JSON plugin:")
    data_stream.output_pipeline(5, JSONExportPlugin())
    print()
    data_stream.print_processors_stats()


if __name__ == "__main__":
    main()
