import os
import glob
import pandas as pd

def load_all_csvs(data_dir="data"):
    # Find all CSV files in the data folder
    pattern = os.path.join(data_dir, "*.csv")
    files = glob.glob(pattern)
    if not files:
        raise FileNotFoundError(f"No CSV files found in {data_dir}/")
    frames = []
    for f in files:
        df = pd.read_csv(f)
        df["source_file"] = os.path.basename(f)  # optional: track origin
        frames.append(df)
    return pd.concat(frames, ignore_index=True)

def clean_and_transform(df):
    # Normalize column names (handle variations like 'Product', 'Date', etc.)
    df.columns = [c.strip().lower() for c in df.columns]

    required_cols = {"product", "quantity", "price", "date", "region"}
    missing = required_cols - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    # Normalize product values to ensure consistent filtering
    df["product"] = df["product"].astype(str).str.strip().str.lower()

    # Keep only Pink Morsels
    df = df[df["product"] == "pink morsel"]

    # Ensure numeric types for calculation
    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
    df["price"] = pd.to_numeric(df["price"], errors="coerce")

    # Drop rows where quantity/price is missing or invalid
    df = df.dropna(subset=["quantity", "price"])

    # Compute sales
    df["sales"] = df["quantity"] * df["price"]

    # Parse date safely (keeps original text if parsing fails)
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    # Drop rows with unparseable dates
    df = df.dropna(subset=["date"])

    # Optionally standardize region formatting
    df.loc[:,"region"] = df["region"].astype(str).str.strip()

    # Select and rename to match exact output field casing
    final = df.loc[:, ["sales", "date", "region"]].copy()
    final.columns = ["Sales", "Date", "Region"]

    # Sort for readability (optional)
    final = final.sort_values(by=["Date", "Region"]).reset_index(drop=True)
    return final

def main():
    # Load → transform → save
    df = load_all_csvs("data")
    final = clean_and_transform(df)
    out_path = "formatted_output.csv"
    final.to_csv(out_path, index=False)
    print(f"Saved: {out_path}")
    print(final.head(10))  # preview first 10 rows

if __name__ == "__main__":
    main()