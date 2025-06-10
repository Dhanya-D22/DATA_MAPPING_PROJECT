 Data Mapping and Filtering Using Reference Excel Sheet

##  Project Overview

This project filters and maps records from a reference Excel file (`reference_data.xlsx`) based on identifiers provided in a raw CSV file (`raw_data.csv`). It generates a clean, deduplicated dataset (`mapped_output.csv`) containing only matched entries.



## 🧾 User Story

**Title:**  
As a developer, I want to filter rows from a reference Excel file based on values present in a raw_data file so that I can generate a mapped output dataset.

**Description:**  
- The `raw_data.csv` contains 100 records with a column named `lookup_key`.
- The `reference_data.xlsx` contains detailed records including the same `lookup_key` column.
- The script matches `lookup_key` values from raw data against the reference, extracts matching rows, and saves the output to `mapped_output.csv`.

**Acceptance Criteria:**
- Only rows with matching `lookup_key` values from raw data are included.
- The output contains all columns from the reference sheet.
- Duplicate `lookup_key` entries in raw data are handled (no duplicate rows in the output).
- The output is saved as `mapped_output.csv`.

---

 Project Structure

```

DATA\_MAPPING\_PROJECT/
│
├── data/
│   ├── raw\_data.csv              # Raw input data
│   ├── reference\_data.xlsx       # Master reference dataset
│   └── mapped\_output.csv         # Final output with matched rows
│
├── results/
│   └── unmatched\_keys.csv        #  Optional: Lookup keys not found in reference
│
├── scripts/
│   └── data\_mapper.py            #  Main Python script
│
├── requirements.txt              #  Required packages
└── README.md                     #  Project documentation

````

---

##  How to Run

 1. Install Required Libraries

Make sure Python is installed, then run:

```bash
pip install -r requirements.txt
````

Or manually:

```bash
pip install pandas openpyxl
```

---

2. Run the Script

From the project root folder:

```bash
python scripts/data_mapper.py
```

---

##  Output Files

* `data/mapped_output.csv`: Rows from reference file matched to raw data keys.
* `results/unmatched_keys.csv`: (Optional) Keys from raw data not found in reference.

---

##  Technologies Used

* **Python 3**
* **pandas** – Data manipulation
* **openpyxl** – Excel file reading




