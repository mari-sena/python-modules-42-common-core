import sys


def main() -> None:
    print("=== Command Quest ===")
    argslen = len(sys.argv)
    args = sys.argv[1:]
    print(f"Program name: {sys.argv[0]}")
    print(f"Arguments received: {argslen - 1}")
    i = 1
    for arg in args:
        print(f"Arguments {i}: {arg}")
        i += 1
    print(f"Total arguments: {argslen}")


if __name__ == "__main__":
    main()
