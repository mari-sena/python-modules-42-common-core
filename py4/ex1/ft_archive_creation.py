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
            # with open(filename, 'r') as reader:
            #     fineline = reader.readlines()
            # new_filename = sys.argv[2]
            # new_file = open(new_filename, "x")
            
            

            print("\n---")
                    
            
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
