import json
import os
import requests
import re
import time
from duckduckgo_search import DDGS
from unidecode import unidecode
import sys

def slugify(text):
    text = unidecode(text).lower()
    return re.sub(r'[\W_]+', '-', text).strip('-')

def main():
    with open('cleaned_products_vi.json', 'r', encoding='utf-8') as f:
        products = json.load(f)
        
    img_dir = "product_images"
    os.makedirs(img_dir, exist_ok=True)
    
    print(f"Downloading images for {len(products)} products (with 15s delay)...")
    
    ddgs = DDGS()
    
    for idx, p in enumerate(products):
        name = p.get('product_name', '')
        category = p.get('category', '')
        if not name: continue
        
        search_query = f"{category} {name} sản phẩm"
        slug_name = slugify(name)
        filename = f"{idx+1:03d}_{slug_name}.jpg"
        filepath = os.path.join(img_dir, filename)
        
        if os.path.exists(filepath):
            print(f"[{idx+1}/{len(products)}] Skipping {name} - already exists")
            continue
            
        print(f"[{idx+1}/{len(products)}] Searching for: {search_query} ... ", end="", flush=True)
        try:
            results = ddgs.images(search_query, max_results=1)
            results_list = list(results)
            
            if results_list and len(results_list) > 0:
                img_url = results_list[0]['image']
                
                # Download
                headers = {'User-Agent': 'Mozilla/5.0'}
                r = requests.get(img_url, headers=headers, timeout=10)
                if r.status_code == 200:
                    with open(filepath, 'wb') as img_file:
                        img_file.write(r.content)
                    print("OK")
                else:
                    print(f"Failed to download (HTTP {r.status_code})")
            else:
                print("No results found.")
                
        except Exception as e:
            error_msg = str(e).lower()
            print(f"Error: {e}")
            if "ratelimit" in error_msg or "403" in error_msg:
                print("\n[!] Bị DuckDuckGo chặn (Rate limit 403). Đang dừng tiến trình lại theo yêu cầu.")
                sys.exit(1)
            
        # Nghỉ 15 giây giữa các lần gọi
        print("Đang nghỉ 15s để tránh bị chặn...")
        time.sleep(15)

if __name__ == '__main__':
    main()
