def secure_archive(
        filename: str,
        action: str = "r",
        content: str = ""
        ) -> tuple[bool, str]:
    status = True
    message = ''
    try:
        if action == "w":
            with open(filename, mode="w") as file:
                file.write(content)
        with open(filename, mode="r") as file:
            message = file.read()
    except FileNotFoundError as error:
        status = False
        message = f"{error}"
    except PermissionError as error:
        status = False
        message = f"{error}"
    return (status, message)


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
