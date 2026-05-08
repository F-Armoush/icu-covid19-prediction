# run.py
# Purpose: Entry point to train models, evaluate them, and display results

from src.train import train_models


def main():
    # Train models and get results
    best_model, results, X_test, y_test = train_models()

    print("\nModel Performance Summary:")
    print("-" * 40)

    for name, metrics in results.items():
        print(f"\n{name.upper()}")
        for metric_name, value in metrics.items():
            print(f"{metric_name}: {value:.4f}")

    print("\nBest model has been saved along with metrics.")


if __name__ == "__main__":
    main()

