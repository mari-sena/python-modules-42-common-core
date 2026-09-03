import sys


def main() -> None:
    print("=== Command Quest ===")
    argslen = len(sys.argv)
    print(f"Program name: {sys.argv[0]}")
    print(f"Arguments received: {argslen - 1}")
    for i in range(1, argslen):
        print(f"Arguments {i}: {sys.argv[i]}")
    print(f"Total arguments: {argslen}")


if __name__ == "__main__":
    main()
