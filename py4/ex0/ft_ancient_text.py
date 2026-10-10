import sys
import typing


def main() -> None:
    args_len = len(sys.argv)
    if args_len != 2:
        print("Usage: ft_ancient_text.py <file>\n")
        return
    filename = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")
    try:
        file: typing.IO[str] = open(filename, "r")
        try:
            content = file.read()
        finally:
            file.close()
    except OSError as error:
        print(f"Error opening file '{filename}': {error}\n")
        return

    print("---\n")
    print(content)
    print("\n---")
    print(f"File '{filename}' closed.")


if __name__ == "__main__":
    main()
