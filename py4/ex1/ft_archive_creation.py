import sys
import typing


def transform_content(content: str) -> str:
    transformed = ""
    for line in content.splitlines(keepends=True):
        if line.endswith("\r\n"):
            transformed += line[:-2] + "#\r\n"
        elif line.endswith("\n") or line.endswith("\r"):
            transformed += line[:-1] + "#" + line[-1]
        else:
            transformed += line + "#"
    return transformed


def main() -> None:
    args_len = len(sys.argv)
    if args_len != 2:
        print("Usage: ft_ancient_text.py <file>\n")
        return

    filename = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    try:
        file: typing.IO[str] = open(filename, "r")
        try:
            content = file.read()
        finally:
            file.close()
    except OSError as error:
        print(f"Error opening file '{filename}': {error}")
        return

    print("---\n")
    print(content, end="")
    print("\n---")
    print(f"File '{filename}' closed.\n")

    transformed = transform_content(content)
    print("Transform data:")
    print("---\n")
    print(transformed, end="")
    print("\n---")

    try:
        new_filename = input("Enter new file name (or empty): ")
    except EOFError:
        print("Data not saved.")
        return

    if len(new_filename) == 0:
        print("Data not saved.")
        return

    print(f"Saving data to '{new_filename}'")
    try:
        new_file: typing.IO[str] = open(new_filename, "w")
        try:
            new_file.write(transformed)
        finally:
            new_file.close()
    except OSError as error:
        print(f"Error opening file '{new_filename}': {error}\n")
        print("Data not saved.")
        return

    print(f"Data saved in file '{new_filename}'.\n")


if __name__ == "__main__":
    main()
