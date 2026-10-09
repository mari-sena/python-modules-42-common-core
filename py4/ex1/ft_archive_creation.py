import sys
import typing


def remove_new_line(line: str) -> str:
    if len(line) > 0 and line[-1] == "\n":
        return line[:-1]
    return line


def main() -> None:
    print("=== Cyber Archives Recovery & Preservation ===")
    args_len = len(sys.argv)
    if args_len != 2:
        print("Usage: ft_ancient_text.py <file>\n")
        return
    filename = sys.argv[1]
    print(f"Accessing file '{filename}'")
    try:
        file: typing.IO[str] = open(filename, "r")
        content = file.read()
        print("---\n")
        print(content)
        print("\n---")
        file.close()
        print(f"File '{filename}' closed.\n")

        print("Transform data:")
        print("---\n")
        fn = open(filename, mode="r")
        for line in fn:
            print(f"{remove_new_line(line)}#")

        print("\n---")
        new_filename = input("Enter new file name (or empty): ")

        if len(new_filename) == 0:
            print("Data not saved.")
            return

        print(f"Saving data to '{new_filename}'")
        fn2 = open(filename, mode="r")
        fn3 = open(new_filename, mode="w")
        for line in fn2:
            fn3.write(remove_new_line(line))
            fn3.write("#\n")
        print(f"Data saved in file '{new_filename}'.\n")
    except PermissionError as error:
        print(f"Error opening file '{new_filename}': {error}\n")
        return
    except FileNotFoundError as error:
        print(
            f"Error opening file '{filename}': "
            f"{error}\n"
        )
        return
    fn.close()
    fn2.close()
    fn3.close()


if __name__ == "__main__":
    main()
