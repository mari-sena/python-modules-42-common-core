def pandas_availability() -> bool:
    try:
        import pandas

        print(f"[OK] pandas ({pandas.__version__}) - Data manipulation ready")
        return True
    except ImportError:
        print("[MISSING] pandas")
        return False


def numpy_availability() -> bool:
    try:
        import numpy

        print(
            f"[OK] numpy ({numpy.__version__})"
            " - Numerical computation ready"
        )
        return True
    except ImportError:
        print("[MISSING] numpy")
        return False


def main() -> None:
    print("\n REAGENT STATUS: Loading reagents...\n")
    print("Checking dependencies: ")

    pandas_check = pandas_availability()
    numpy_check = numpy_availability()

    print("\npip vs Poetry:")
    print(
        " requirements.txt declares what to install; "
        "pip resolves dependencies at install time."
    )
    print(
        " pyproject.toml declares the same constraints, "
        "and Poetry pins the resolved"
    )
    print(" versions in poetry.lock so every install is identical.")

    if pandas_check and numpy_check:
        print("\nAll reagents present and accounted for.")
    else:
        print("\nSome reagents are missing.")
        print("To install dependencies:")
        print("Using pip: python3 -m pip install -r ex0/requirements.txt")
        print("Using Poetry: cd ex0 && pip install poetry && poetry install")


if __name__ == "__main__":
    main()
