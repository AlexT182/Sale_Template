import re
from xml.etree import ElementTree as ET

def refactor():
    filepath = r"D:\Project\QQ\Sale_template\sale_website_home\views\homepage.xml"
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    sections_match = re.search(r'<div id="wrap"[^>]*>(.*?)</div>\s*</xpath>', content, re.DOTALL)
    if not sections_match:
        print("Could not find wrap div content")
        return
        
    wrap_content = sections_match.group(1)
    
    sections = re.findall(r'(<!--.*?-->\s*<section.*?</section>)', wrap_content, re.DOTALL)
    
    if len(sections) != 6:
        print(f"Found {len(sections)} sections instead of 6")
        return
        
    names = ['s_ew_hero', 's_ew_categories', 's_ew_about', 's_ew_gallery', 's_ew_news', 's_ew_contact']
    
    templates = []
    snippets_calls = []
    
    for i, section in enumerate(sections):
        name = names[i]
        template = f"""    <template id="{name}" name="{name.replace('s_ew_', 'Sale ').title()}">
{section}
    </template>
"""
        templates.append(template)
        snippets_calls.append(f'                <t t-snippet="sale_website_home.{name}"/>')
        
    templates_str = '\n'.join(templates)
    snippets_str = '\n'.join(snippets_calls)
    
    new_content = f"""<?xml version="1.0" encoding="utf-8"?>
<odoo>
{templates_str}
    <template id="sale_homepage"
              inherit_id="website.homepage"
              name="Sale Website Homepage"
              priority="1000">
        <xpath expr="//div[@id='wrap']" position="replace">
            <div id="wrap" class="oe_structure oe_empty ew-homepage">
{snippets_str}
            </div>
        </xpath>
    </template>
</odoo>
"""
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print("Refactoring complete.")

if __name__ == '__main__':
    refactor()
