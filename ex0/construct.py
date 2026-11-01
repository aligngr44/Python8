import os
import site
import sys


def in_virtual_env() -> bool:
    return sys.prefix != sys.base_prefix


def main() -> None:
    if not in_virtual_env():
        print("MATRIX STATUS: You're still plugged in\n")
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected\n")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate # On Windows\n")
        print("Then run this program again.")
    else:
        print("MATRIX STATUS: Welcome to the construct\n")
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
        print(f"Environment Path: {sys.prefix}\n")
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.\n")
        print("Package installation path:")
        print(site.getsitepackages()[0])


if __name__ == "__main__":
    main()