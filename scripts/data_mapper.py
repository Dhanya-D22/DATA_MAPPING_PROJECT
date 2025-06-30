import pandas as pd

try:
    print(" Reading input files")
    raw = pd.read_csv('data/raw_data.csv')
    reference = pd.read_excel('data/reference_data.xlsx')

    print(" Extracting unique lookup_keys")
    lookup_keys = raw['lookup_key'].drop_duplicates()
    print(f"Found {len(lookup_keys)} unique lookup_keys.")

    print(" Performing INNER JOIN to include only matched records")
    # Keep only records where lookup_key is present in both raw and reference
    merged = pd.merge(raw, reference, on='lookup_key', how='inner')
    print(f"Matched rows: {len(merged)}")

    # Save the final output (only matched rows with full raw + reference columns)
    merged.to_csv('data/mapped_output.csv', index=False)

    # Save unmatched raw lookup_keys for reporting
    unmatched = raw[~raw['lookup_key'].isin(reference['lookup_key'])]
    unmatched.to_csv('results/unmatched_keys.csv', index=False)
    print(f"Unmatched keys saved: {len(unmatched)}")

    print(" Mapping complete. Output written to 'data/mapped_output.csv'")

except Exception as e:
    print(" Error:", e)
