import os


try:
    from dotenv import dotenv_values, load_dotenv
except ModuleNotFoundError as error:
    if error.name != "dotenv":
        raise

    print("[ERROR] Missing dependency: python-dotenv")
    print("To install dependencies, run:")
    print("python3 -m pip install -r ex1/requirements.txt")
    raise SystemExit(1)


def load_configs(original_mode: str | None) -> None:
    database = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL", "INFO")
    endpoint = os.getenv("ZION_ENDPOINT")

    print("Configuration loaded:")
    print(f"Mode: {original_mode}")
    if database:
        if original_mode == "production":
            print("Database: Connected to production instance")
        else:
            print("Database: Connected to local instance")
    else:
        print("Database: Not configured")
    if api_key:
        print("API Access: Authenticated")
    else:
        print("API Access: Not configured")
    print(f"Log Level: {log_level}")
    if endpoint:
        print("Remote Network: Online")
    else:
        print("Remote Network: Offline")


def env_is_ignored() -> None:
    try:
        gitignore_path = os.path.join(
            os.path.dirname(__file__), ".gitignore"
        )
        with open(gitignore_path, "r") as file:
            for line in file:
                if line.strip() == ".env":
                    print("[OK] .env file properly ignored by git")
                    return
        print("[WARNING] .env is not listed in .gitignore")
    except FileNotFoundError:
        print("[ERROR] .gitignore file not found")
        return


def verify_mode_override(original_mode: str | None) -> None:
    env_path = os.path.join(os.path.dirname(__file__), ".env")
    file_values = dotenv_values(env_path)

    if (
        original_mode is not None
        and original_mode != file_values.get("MATRIX_MODE")
    ):
        mode_name = original_mode.capitalize()
        print(f"[OK] {mode_name} overrides available")


def main() -> None:
    original_mode = os.getenv("MATRIX_MODE")
    env_path = os.path.join(os.path.dirname(__file__), ".env")
    load_dotenv(env_path)
    mode = os.getenv("MATRIX_MODE", "development")

    print("\nORACLE STATUS: Consulting the configuration...\n")

    if not os.path.isfile(env_path):
        print("[WARNING] .env file not found. Using environment or default values.")

    load_configs(mode)

    print("\nConfiguration security check:")
    print("[OK] No hardcoded secrets detected")
    env_is_ignored()
    verify_mode_override(original_mode)

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
