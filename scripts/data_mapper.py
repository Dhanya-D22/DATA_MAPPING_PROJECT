import pandas as pd

try:
    print(" Reading input files")
    raw = pd.read_csv('data/raw_data.csv')
    reference = pd.read_excel('data/reference_data.xlsx')

    print(" Extracting unique lookup_keys")
    lookup_keys = raw['lookup_key'].drop_duplicates()
    print(f"Found {len(lookup_keys)} unique lookup_keys.")

    print(" Matching reference data")
    matched = reference[reference['lookup_key'].isin(lookup_keys)]
    print(f"Matched rows: {len(matched)}")

    matched.to_csv('data/mapped_output.csv', index=False)

    #  Unmatched keys
    unmatched = raw[~raw['lookup_key'].isin(reference['lookup_key'])]
    unmatched.to_csv('results/unmatched_keys.csv', index=False)
    print(f"Unmatched keys saved: {len(unmatched)}")

    print(" Mapping complete. Output written to 'data/mapped_output.csv'")
except Exception as e:
    print(" Error:", e)
