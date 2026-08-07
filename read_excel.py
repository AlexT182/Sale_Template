import pandas as pd
import sys

file_path = r"D:\OneDrive\CCVI Technology\C-Dev Team - Documents\Web ElyWordlAccess\DANH MUC SAN PHAM THE MANH.xlsx"

with open("excel_structure.txt", "w", encoding="utf-8") as f:
    try:
        xls = pd.ExcelFile(file_path)
        f.write(f"Sheet names: {xls.sheet_names}\n")
        
        for sheet_name in xls.sheet_names:
            f.write(f"\n--- Sheet: {sheet_name} ---\n")
            df = pd.read_excel(file_path, sheet_name=sheet_name)
            f.write(f"Columns: {df.columns.tolist()}\n")
            f.write(f"First 3 rows:\n")
            f.write(df.head(3).to_string() + "\n")
            f.write(f"Total rows: {len(df)}\n")
            
    except Exception as e:
        f.write(f"Error reading file: {e}\n")
