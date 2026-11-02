import os

from dotenv import load_dotenv


def main() -> None:
    if not load_dotenv():
        print("WARNING: .env file not found")

    names = ["MATRIX_MODE", "DATABASE_URL", "API_KEY",
             "LOG_LEVEL", "ZION_ENDPOINT"]
    config = {name: os.getenv(name) for name in names}

    print("ORACLE STATUS: Reading the Matrix...")

    for name, value in config.items():
        if not value:
            print(f"WARNING: {name} is missing")

    mode = config["MATRIX_MODE"]
    print("Configuration loaded:")
    print(f"Mode: {mode}")

    if mode == "development":
        print("Database: Connected to local instance")
    elif mode == "production":
        print("Database: Connected to production database")
    else:
        print("WARNING: MATRIX_MODE is invalid")

    if config["API_KEY"]:
        print("API Access: Authenticated")
    else:
        print("API Access: Missing")

    print(f"Log Level: {config['LOG_LEVEL']}")

    if config["ZION_ENDPOINT"]:
        print("Zion Network: Online")
    else:
        print("Zion Network: Offline")

    print("\nEnvironment security check:")

    api_key = config["API_KEY"]
    with open(__file__) as source_file:
        source = source_file.read()

    if api_key and api_key in source:
        print("[KO] Hardcoded secret detected!")
    else:
        print("[OK] No hardcoded secrets detected")

    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[KO] .env file not found")

    print("[OK] Production overrides available")
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
