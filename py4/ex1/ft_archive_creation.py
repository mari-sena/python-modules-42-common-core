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
            print(f"File '{filename}' closed.\n")

            print("Transform data:")
            print("---\n")
            with open(filename, mode="r") as fn:
                for line in fn:
                    print(f"{line.strip()}#")

            print("\n---")
            new_filename = input("Enter new file name (or empty): ")
            print(f"Saving data to '{new_filename}'")
            with open(filename, mode="r") as fn:
                with open(new_filename, mode="w") as fn2:
                    for line in fn:
                        fn2.write(line.strip())
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
