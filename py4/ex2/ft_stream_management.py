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
        print("Usage: ft_stream_management.py <file>\n")
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
        with open(filename, mode="r") as fn:
            for line in fn:
                print(f"{remove_new_line(line)}#")

        print("\n---")
        print("Enter new file name (or empty): ", end="", flush=True)
        new_filename = remove_new_line(sys.stdin.readline())

        if len(new_filename) == 0:
            print("Data not saved.")
            return

        print(f"Saving data to '{new_filename}'")
        try:
            with open(filename, mode="r") as fn:
                with open(new_filename, mode="w") as fn2:
                    for line in fn:
                        fn2.write(remove_new_line(line))
                        fn2.write("#\n")
            print(f"Data saved in file '{new_filename}'.\n")
        except PermissionError as error:
            print(
                f"[STDERR] Error opening file '{new_filename}': {error}",
                file=sys.stderr
            )
            print("Data not saved.", file=sys.stderr)
            return
    except PermissionError as error:
        print(
            f"[STDERR] Error opening file '{filename}': {error}\n",
            file=sys.stderr
        )
        return
    except FileNotFoundError as error:
        print(
            f"[STDERR] Error opening file '{filename}': {error}\n",
            file=sys.stderr
        )
        return


if __name__ == "__main__":
    main()
