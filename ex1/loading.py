import importlib
import sys


def main() -> None:
    dependencies = ["pandas", "numpy", "matplotlib"]

    missing_dep = False
    print("Checking Dependencies:")
    for dep in dependencies:
        try:
            mod = importlib.import_module(dep)
            version = getattr(mod, "__version__", "unknown")
            print(f"[OK] {dep} {version} is ready")
        except ImportError:
            print(f"[KO] {dep} is missing")
            missing_dep = True

    if missing_dep:
        print("\nError: Missing required dependencies.")
        print("Please install them using one of the following commands:")
        print("  pip:    pip install -r requirements.txt")
        print("  poetry: poetry install")
        sys.exit(1)

    # some code using the modules


if __name__ == "__main__":
    main()
