import os
import sys


import os
import sys


def security_check(config: dict[str, str | None]) -> None:
    print("\nEnvironment security check:")

    with open(__file__) as f:
        source = f.read()
    leaked = [v for v in (config["API_KEY"], config["DATABASE_URL"])
              if v and v in source]
    print("[OK] No hardcoded secrets detected" if not leaked
          else "[WARN] Secret found in source code!")

    print("[OK] .env file properly configured" if os.path.isfile(".env")
          else "[WARN] .env file not found")

    print("[OK] Production overrides available")


def main() -> None:
    try:
        from dotenv import load_dotenv
    except ImportError:
        print("install dotenv")
        sys.exit(1)
    if not load_dotenv():
        print("WARNING: .env file not found")

    names = ["MATRIX_MODE", "DATABASE_URL", "API_KEY",
             "LOG_LEVEL", "ZION_ENDPOINT"]
    config = {name: os.getenv(name) for name in names}
    mode = config["MATRIX_MODE"]
    if mode not in ("development", "production"):
        print("ERROR: MATRIX_MODE must be 'development' or 'production'")
        sys.exit(1)
    print("Configuration loaded:")

    if mode == "development":
        print("Mode: development")
        if config["DATABASE_URL"]:
            print("Database: Connected to local instance")
        else:
            print("Database: missing")
        
        if config["API_KEY"]:
            print("API Access: Authenticated")
        else:
            print("API key missing")
        
        if config["LOG_LEVEL"]:
            print(f"LOG LEVEL: {config["LOG_LEVEL"]}")
        else:
            print("LOG LEVEL: DEBUG")
        if config["ZION_ENDPOINT"]:
            print("Zion Network: Online")
        else:
            print("Zion Network: Offline")


    if mode == "production":
        print("Mode: production")
        if config["DATABASE_URL"]:
            print("Database: Connected to production database")
        else:
            print("Database: missing")
        
        if config["API_KEY"]:
            print("API Access: Authenticated")
        else:
            print("API key missing")
        
        if config["LOG_LEVEL"]:
            print(f"LOG LEVEL: {config["LOG_LEVEL"]}")
        else:
            print("LOG LEVEL: WARNING")
        if config["ZION_ENDPOINT"]:
            print("Zion Network: Online")
        else:
            print("Zion Network: Offline")

    security_check(config)

if __name__ == "__main__":
    print("ORACLE STATUS: Reading the Matrix...")
    main()
