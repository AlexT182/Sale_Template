import re

def refactor():
    filepath = r"D:\Project\QQ\odoo-template\elyworld_website_home\views\homepage.xml"
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # We want to add s_text_block and data-snippet to all sections
    # Current sections look like: <section class="ew-hero o_colored_level">
    
    # Hero
    content = re.sub(r'<section class="ew-hero o_colored_level">', 
                     r'<section class="s_text_block ew-hero o_colored_level" data-snippet="s_text_block" data-name="Hero Block">', content)
    # Categories
    content = re.sub(r'<section class="ew-section ew-categories o_colored_level">', 
                     r'<section class="s_text_block ew-section ew-categories o_colored_level" data-snippet="s_text_block" data-name="Categories Block">', content)
    # About
    content = re.sub(r'<section class="ew-section ew-about o_colored_level">', 
                     r'<section class="s_text_block ew-section ew-about o_colored_level" data-snippet="s_text_block" data-name="About Block">', content)
    # Gallery
    content = re.sub(r'<section class="ew-section ew-gallery o_colored_level">', 
                     r'<section class="s_text_block ew-section ew-gallery o_colored_level" data-snippet="s_text_block" data-name="Gallery Block">', content)
    # News
    content = re.sub(r'<section class="ew-section ew-news o_colored_level">', 
                     r'<section class="s_text_block ew-section ew-news o_colored_level" data-snippet="s_text_block" data-name="News Block">', content)
    # Contact
    content = re.sub(r'<section id="contact" class="ew-section ew-contact o_colored_level">', 
                     r'<section id="contact" class="s_text_block ew-section ew-contact o_colored_level" data-snippet="s_text_block" data-name="Contact Block">', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Added snippet attributes back.")

if __name__ == '__main__':
    refactor()
