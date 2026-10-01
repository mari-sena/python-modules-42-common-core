import abc
import typing


def main() -> None:
	print("")
	class DataProcessor(abc):
		def validate(self):
			pass
		def ingest(self):
			pass

	class NumericProcessor(DataProcessor):
		pass

	class TextProcessor(DataProcessor):
		pass

	class LogProcessor(DataProcessor):
		pass


if __name__ == "__main__":
	main()
