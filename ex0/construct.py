import sys
import os
import site


def is_env() -> bool:
    return sys.prefix != sys.base_prefix


def main() -> None:
    if not is_env():
        print(f"MATRİX STATUS: You're still plugged in")
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print("To enter the construct, run:\n"
                "python -m venv matrix_env\n"
                "source matrix_env/bin/activate # On Unix\n"
                "matrix_env\\Scripts\\activate # On Windows\n"
                "Then run this program again.")

    else:
        print(f"MATRİX STATUS: Welcome to the construct")
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
        print(f"Environment Path: {sys.prefix}")
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")

        print("Package installation path:")
        print(site.getsitepackages())

if __name__ == "__main__":
    main()