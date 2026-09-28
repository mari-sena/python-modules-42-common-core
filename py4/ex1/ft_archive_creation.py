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
    else:
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
            with open(filename, mode="r") as fn:
                for line in fn:
                    print(f"{remove_new_line(line)}#")

            print("\n---")
            new_filename = input("Enter new file name (or empty): ")
            print(f"Saving data to '{new_filename}'")
            with open(filename, mode="r") as fn:
                with open(new_filename, mode="w") as fn2:
                    for line in fn:
                        fn2.write(remove_new_line(line))
                        fn2.write("#\n")
            print(f"Data saved in file '{new_filename}'.\n")

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
