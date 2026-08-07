import pandas as pd
import json
import re

file_path = r"D:\OneDrive\CCVI Technology\C-Dev Team - Documents\Web ElyWordlAccess\DANH MUC SAN PHAM THE MANH.xlsx"

def clean_data(sheet_name):
    df = pd.read_excel(file_path, sheet_name=sheet_name, header=None, skiprows=3)
    df = df.iloc[:, :7]
    df.columns = ["stt", "category", "product_name", "sourcing_by", "features", "inner_pack", "outer_pack"]
    
    df["category"] = df["category"].ffill()
    df["features"] = df["features"].ffill()
    df["inner_pack"] = df["inner_pack"].ffill()
    df["outer_pack"] = df["outer_pack"].ffill()
    
    df = df.dropna(subset=["product_name"])
    df = df[~df["product_name"].astype(str).str.upper().isin(["TÊN SP", "PRODUCT NAME", "NAN"])]
    
    records = []
    for _, row in df.iterrows():
        cat = str(row["category"]).strip()
        cat = re.sub(r'^\d+\.\s*', '', cat)
        
        raw_names = str(row["product_name"]).strip()
        features = str(row["features"]).strip() if pd.notnull(row["features"]) else ""
        inner_pack = str(row["inner_pack"]).strip() if pd.notnull(row["inner_pack"]) else ""
        outer_pack = str(row["outer_pack"]).strip() if pd.notnull(row["outer_pack"]) else ""
        
        names = [n.strip() for n in raw_names.split('\n') if n.strip()]
        
        for name in names:
            records.append({
                "category": cat,
                "product_name": name,
                "features": features,
                "inner_pack": inner_pack,
                "outer_pack": outer_pack
            })
            
    return records

try:
    vi_records = clean_data("VI")
    en_records = clean_data("EN")
    
    print(f"Cleaned VI: {len(vi_records)} products.")
    print(f"Cleaned EN: {len(en_records)} products.")
    
    # Write to a single markdown file
    with open("All_Products_Review.md", "w", encoding="utf-8") as f:
        f.write("# DANH SÁCH TOÀN BỘ SẢN PHẨM ĐÃ CHUẨN HÓA (VI & EN)\n\n")
        
        # Determine the length to loop
        max_len = max(len(vi_records), len(en_records))
        
        for i in range(max_len):
            f.write(f"## SẢN PHẨM {i+1}\n")
            if i < len(vi_records):
                vi = vi_records[i]
                f.write("**[TIẾNG VIỆT]**\n")
                f.write(f"- **Danh mục:** {vi['category']}\n")
                f.write(f"- **Tên sản phẩm:** {vi['product_name']}\n")
                f.write(f"- **Đặc tính:** {vi['features']}\n")
                f.write(f"- **Bao bì (Trong/Ngoài):** {vi['inner_pack']} / {vi['outer_pack']}\n\n")
            else:
                f.write("**[TIẾNG VIỆT]** Không có dữ liệu tương ứng.\n\n")
                
            if i < len(en_records):
                en = en_records[i]
                f.write("**[TIẾNG ANH]**\n")
                f.write(f"- **Category:** {en['category']}\n")
                f.write(f"- **Product Name:** {en['product_name']}\n")
                f.write(f"- **Features:** {en['features']}\n")
                f.write(f"- **Packaging (Inner/Outer):** {en['inner_pack']} / {en['outer_pack']}\n\n")
            else:
                f.write("**[TIẾNG ANH]** Không có dữ liệu tương ứng.\n\n")
            
            f.write("---\n\n")
            
    print("Successfully generated All_Products_Review.md")

except Exception as e:
    print(f"Error: {e}")
