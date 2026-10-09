def secure_archive(
        filename: str,
        action: str = "r",
        content: str = ""
        ) -> tuple[bool, str]:
    try:
        if action == "w":
            with open(filename, mode="w") as file:
                file.write(content)
            return (True, "Content successfully written to file")

        if action == "r":
            with open(filename, mode="r") as file:
                return (True, file.read())
        return (False, "Invalid action")
    except OSError as error:
        return (False, str(error))

def main() -> None:
    print("=== Cyber Archives Security ===\n")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive('/not/existing/file'))

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive('master.passwd.txt'))

    print("\nUsing 'secure_archive' to read from a regular file:")
    print(secure_archive('ancient_fragment.txt'))

    print("\nUsing 'secure_archive' to write previous content to a new file:")
    print(secure_archive(
        'acient_fragment.txt', 'w',
        'Content successfully written to file'
        ))


if __name__ == "__main__":
    main()
