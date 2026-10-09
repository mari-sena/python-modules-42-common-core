import sys
import os
import site


def show_python_info() -> None:
    print(f"Current Python: {sys.executable}")

    if is_virtual_environment():
        print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
        print(f"Environment Path: {sys.prefix}")
    else:
        print("Virtual Environment: None detected")


def is_virtual_environment() -> bool:
    return sys.prefix != sys.base_prefix


def main() -> None:
    if is_virtual_environment():
        print("\nLABORATORY STATUS: The laboratory is sealed\n")

        show_python_info()
        print("\nSUCCESS: You are working in an isolated environment!")
        print("Safe to install reagents without affecting")
        print("the global system.\n")

        print("Reagent installation path: ")
        for path in site.getsitepackages():
            print(path)
    else:
        print("\nLABORATORY STATUS: You are working in the open\n")

        show_python_info()

        print("WARNING: You are in the global environment!")
        print("Every reagent you install here leaks into the whole system.\n")

        print("To seal the laboratory, run:")
        print("python3 -m venv lab_env")
        print("source lab_env/bin/activate # On Unix")
        print(r"lab_env\Scripts\activate # On Windows")

        print("Then run this program again.")


if __name__ == "__main__":
    main()
