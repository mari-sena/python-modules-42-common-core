import sys
import typing


def main() -> None:
    print("=== Cyber Archives Recovery & Preservation ===")
    args_len = len(sys.argv)
    if args_len == 1:
        print("Usage: ft_ancient_text.py <file>\n")
        return
    if args_len == 2:
        filename = sys.argv[1]
        print(f"Accessing file '{filename}'")
        try:
            file: typing.IO[str] = open(filename, "r")
            content = file.read()
            print("---\n")
            print(content)
            print("\n---")
            file.close()
            print(f"File '{filename}' closed.")

            print("Transform data:")
            print("---\n")
            f = open(input("Enter new file name (or empty): "), "x")
            print(f"Saving data to '{f.name}'")
            print(f"Data saved in file '{f.name}'.\n")
            f = content
            
        except PermissionError as error:
            print(f"Error opening file '{filename}': {error}\n")
            return
        except FileNotFoundError as error:
            print(
                f"Error opening file '{filename}': "
                f"{error}\n"
                )


if __name__ == "__main__":
    main()
