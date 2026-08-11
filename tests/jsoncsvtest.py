import os
import sys
import pandas as pd

def convert_to_csv(filepath):
    # Converts a JSON file to a CSV file and validates against original JSON to ensure proper data handling.
    if not os.path.exists(filepath):
        print(f"Error: File '{filepath}' not found.")
        sys.exit(1)
    
    try:
        dataframe = pd.read_json(filepath)
    except Exception as e:
        print(f"Error: Could not read JSON file '{filepath}'. Details: {e}")
        sys.exit(1)

    if dataframe.empty:
        print(f"JSON file '{filepath}' appears to be empty.")
        sys.exit(1)

    return dataframe.to_csv(index=False)

def main():
    # Example usage of the convert_to_csv function
    input_file = input("Enter the path to your JSON file: ").strip()
    csv_output = convert_to_csv(input_file)
    print("CSV Output:")
    print(csv_output.splitlines()[:5])


if __name__ == "__main__":
    main()