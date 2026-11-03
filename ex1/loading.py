import importlib
import importlib.metadata
import sys

REQUIRED = {
    "pandas": "Data manipulation ready",
    "numpy": "Numerical computation ready",
    "matplotlib": "Visualization ready",
}


def check_dependencies() -> list[str]:
    missing: list[str] = []
    print("Checking dependencies:")
    for name, description in REQUIRED.items():
        try:
            importlib.import_module(name)
            version = importlib.metadata.version(name)
            print(f"[OK] {name} ({version}) - {description}")
        except ImportError:
            print(f"[MISSING] {name} - not installed")
            missing.append(name)
    return missing


def compare_managers() -> None:
    print("\npip vs Poetry:")
    print("pip:    requirements.txt, no lock file")
    print("Poetry: pyproject.toml + poetry.lock, reproducible")
    manager = "Poetry" if "pypoetry" in sys.prefix else "pip/venv"
    print(f"Running in: {manager} ({sys.prefix})")


def analyze_and_plot() -> None:
    np = importlib.import_module("numpy")
    pd = importlib.import_module("pandas")
    matplotlib = importlib.import_module("matplotlib")
    matplotlib.use("Agg")
    plt = importlib.import_module("matplotlib.pyplot")

    df = pd.DataFrame({"signal": np.random.normal(size=1000)})
    print("\nAnalyzing Matrix data...")
    print(f"Processing {len(df)} data points...")
    print("Generating visualization...")
    plt.plot(df["signal"])
    plt.savefig("matrix_analysis.png")
    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


def main() -> None:
    print("LOADING STATUS: Loading programs...\n")
    missing = check_dependencies()
    if missing:
        print(f"\nMissing: {', '.join(missing)}")
        print("pip:    pip install -r requirements.txt")
        print("Poetry: poetry install")
        sys.exit(1)
    analyze_and_plot()
    compare_managers()


if __name__ == "__main__":
    main()