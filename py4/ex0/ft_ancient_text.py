import sys


def main() -> None:
	args_len = len(sys.argv)
	if args_len == 1:
		print("Usage: ft_ancient_text.py <file>\n")
		return
	if args_len == 2:
		print("=== Cyber Archives Recovery ===")
		print(f"Accessing file '{sys.argv[1]}'")
		try:
			hapen = open(sys.argv[1])
			print(hapen)
		except FileNotFoundError as error:
			print(
				f"Error opening file '{sys.argv[1]}': "
				f"{error}"
				)
	

if __name__ == "__main__":
	main()
