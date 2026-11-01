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


def ensure_dependencies() -> None:
    missing = check_dependencies()
    if missing:
        print(f"\nMissing: {', '.join(missing)}")
        print("Install with pip:    pip install -r requirements.txt")
        print("Install with Poetry: poetry install")
        sys.exit(1)


def analyze_and_plot() -> None:
    np = importlib.import_module("numpy")
    pd = importlib.import_module("pandas")
    matplotlib = importlib.import_module("matplotlib")
    matplotlib.use("Agg")
    plt = importlib.import_module("matplotlib.pyplot")

    data = np.random.normal(size=1000)
    df = pd.DataFrame({"signal": data})
    print("Analyzing Matrix data...")
    print(f"Processing {len(df)} data points...")
    print("Generating visualization...")
    plt.plot(df["signal"])
    plt.savefig("matrix_analysis.png")
    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


def main() -> None:
    print("LOADING STATUS: Loading programs...\n")
    ensure_dependencies()
    print()
    analyze_and_plot()


if __name__ == "__main__":
    main()