from typing import Any
from data_processor import DataProcessor


class DataStream:
    def __init__(self, data: Any):
        self.data = data

    def register_processor(self, proc: DataProcessor) -> None:
        try:
            # proc.data
        except:
            if data.length() == 0
                print("No processor found, no data")
            else:
                process_stream(proc.data)
    
    def process_stream(self, stream: list[Any]) -> None:
        pass # self.stream
    
    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        print("No processor found, no data")

        # print("Numeric Processor: ")

        # print("Numeric Processor: ")
        # print("Text Processor: ")
        # print("Log Processor: ")

        # print("Numeric Processor: ")
        # print("Text Processor: ")
        # print("Log Processor: ")


def main() -> None:
    print("=== Code Nexus - Data Stream ===")

    print("\nInitialize Data Stream...")
    numeric = DataStream()
    numeric.print_processors_stats()
    tulipa = [
        'Hello world',
        [3.14, -1, 2.71],
        [
            {
                'log_level': 'WARNING',
                'log_message': 'Telnet access! Use ssh instead'
            },
            {
                'log_level': 'INFO',
                'log_message': 'User wil is connected'
            }
        ],
        42,
        ['Hi', 'five']
    ]

    print("Registering Numeric Processor\n")

    print(
        "Send first batch of data on stream: "
        f"{numeric.register_processor(tulipa)}"
    )
    # print("DataStream error - " )
    # print("DataStream error - {()}")
    # print("DataStream error - {(['Hi', 'five'])}")
    # numeric.print_processors_stats()

    # print("Registering other data processors")
    # print("Send the same batch again")
    # numeric.print_processors_stats()
    

    # print("Consume some elements from the data processors: ")
    # numeric.print_processors_stats()


if __name__ == "__main__":
    main()
