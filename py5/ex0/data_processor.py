import abc
import typing


def main() -> None:
	print("=== Code Nexus - Data Processor ===")
	class DataProcessor(abc):
		def abs_validate(self, data: typing.Any) -> bool:
			pass
		def abs_ingest(self, data: typing.Any) -> None:
			pass
		def output(self):
			pass

	class NumericProcessor(DataProcessor):
		def __init(self, data: typing.Any) -> None:
			super().__init__(data)

	class TextProcessor(DataProcessor):
		pass

	class LogProcessor(DataProcessor):
		pass

	print("Testing Numeric Processor...")
	print(" Trying to validate input '42': ")
	print(" Trying to validate input 'Hello': ")
	print(" Test invalid ingestion of string 'foo' without prior validation:")
	print(" Got exception: ")
	print(" Processing data: ")
	print(" Extracting 3 values...")
	print(" Numeric value 0: ")
	print(" Numeric value 1: ")
	print(" Numeric value 2: ")

	print("Testing Text Processor...")
	print(" Trying to validate input '42': ")
	print(" Processing data: ")
	print(" Extracting 1 value...")
	print(" Text value 0: ")

	print("Testing Log Processor...")
	print(" Trying to validate input 'Hello': ")
	print(" Processing data: ")
	print(" Extracting 2 values...")
	print(" Log entry 0: ")
	print(" Log entry 1: ")



if __name__ == "__main__":
	main()
