import json
import os
import re
import random
from unidecode import unidecode
from PIL import Image, ImageDraw, ImageFont

def slugify(text):
    text = unidecode(text).lower()
    return re.sub(r'[\W_]+', '-', text).strip('-')

def get_random_color():
    colors = [
        (109, 76, 65),  # Brown
        (141, 110, 99), # Light Brown
        (216, 67, 21),  # Deep Orange
        (0, 105, 92),   # Teal
        (46, 125, 50),  # Green
        (21, 101, 192), # Blue
        (69, 39, 160),  # Purple
        (198, 40, 40),  # Red
    ]
    return random.choice(colors)

def draw_text_wrapped(draw, text, max_width, font, x, y, fill):
    words = text.split()
    lines = []
    current_line = []
    
    for word in words:
        current_line.append(word)
        line_w = draw.textlength(" ".join(current_line), font=font) if hasattr(draw, 'textlength') else font.getlength(" ".join(current_line))
        if line_w > max_width:
            current_line.pop()
            lines.append(" ".join(current_line))
            current_line = [word]
    if current_line:
        lines.append(" ".join(current_line))
        
    y_offset = y
    for line in lines:
        line_w = draw.textlength(line, font=font) if hasattr(draw, 'textlength') else font.getlength(line)
        draw.text(((max_width - line_w) / 2 + x, y_offset), line, font=font, fill=fill)
        y_offset += 40 # line height

def main():
    with open('cleaned_products_vi.json', 'r', encoding='utf-8') as f:
        products = json.load(f)
        
    img_dir = "product_images"
    os.makedirs(img_dir, exist_ok=True)
    
    print(f"Generating placeholder images for {len(products)} products...")
    
    # Try to load a default font, fallback to basic PIL font
    try:
        # Attempt to use a basic arial font if on Windows
        font = ImageFont.truetype("arial.ttf", 32)
    except IOError:
        font = ImageFont.load_default()

    for idx, p in enumerate(products):
        name = p.get('product_name', '')
        if not name: continue
        
        slug_name = slugify(name)
        filename = f"{idx+1:03d}_{slug_name}.jpg"
        filepath = os.path.join(img_dir, filename)
        
        if os.path.exists(filepath):
            print(f"[{idx+1}/{len(products)}] Skipping {name} - already exists")
            continue
            
        print(f"[{idx+1}/{len(products)}] Generating image for: {name} ... ", end="", flush=True)
        
        # Create a 600x600 image
        bg_color = get_random_color()
        img = Image.new('RGB', (600, 600), color=bg_color)
        draw = ImageDraw.Draw(img)
        
        # Draw category and name
        category = p.get('category', 'SẢN PHẨM')
        
        draw_text_wrapped(draw, category, 560, font, 20, 200, fill=(255, 255, 255))
        draw_text_wrapped(draw, name, 560, font, 20, 260, fill=(255, 215, 0)) # Gold text for name
        
        img.save(filepath, quality=90)
        print("OK")

if __name__ == '__main__':
    main()
