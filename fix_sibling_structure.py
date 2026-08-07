import re

def refactor():
    filepath = r"D:\Project\QQ\odoo-template\elyworld_website_home\views\homepage.xml"
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Modify the templates to add oe_structure and unique IDs
    content = re.sub(
        r'<section class="s_text_block ew-hero o_colored_level" data-snippet="s_text_block" data-name="Hero Block">',
        r'<section id="ew_hero_edit" class="s_text_block ew-hero o_colored_level oe_structure" data-snippet="s_text_block" data-name="Hero Block">',
        content
    )
    content = re.sub(
        r'<section class="s_text_block ew-section ew-categories o_colored_level" data-snippet="s_text_block" data-name="Categories Block">',
        r'<section id="ew_categories_edit" class="s_text_block ew-section ew-categories o_colored_level oe_structure" data-snippet="s_text_block" data-name="Categories Block">',
        content
    )
    content = re.sub(
        r'<section class="s_text_block ew-section ew-about o_colored_level" data-snippet="s_text_block" data-name="About Block">',
        r'<section id="ew_about_edit" class="s_text_block ew-section ew-about o_colored_level oe_structure" data-snippet="s_text_block" data-name="About Block">',
        content
    )
    content = re.sub(
        r'<section class="s_text_block ew-section ew-gallery o_colored_level" data-snippet="s_text_block" data-name="Gallery Block">',
        r'<section id="ew_gallery_edit" class="s_text_block ew-section ew-gallery o_colored_level oe_structure" data-snippet="s_text_block" data-name="Gallery Block">',
        content
    )
    content = re.sub(
        r'<section class="s_text_block ew-section ew-news o_colored_level" data-snippet="s_text_block" data-name="News Block">',
        r'<section id="ew_news_edit" class="s_text_block ew-section ew-news o_colored_level oe_structure" data-snippet="s_text_block" data-name="News Block">',
        content
    )
    # Contact already has id="contact", we just add oe_structure
    content = re.sub(
        r'<section id="contact" class="s_text_block ew-section ew-contact o_colored_level" data-snippet="s_text_block" data-name="Contact Block">',
        r'<section id="contact" class="s_text_block ew-section ew-contact o_colored_level oe_structure" data-snippet="s_text_block" data-name="Contact Block">',
        content
    )

    # 2. Replace the xpath block
    xpath_pattern = r'<xpath expr="//div\[@id=\'wrap\'\]" position="attributes">.*?</xpath>'
    content = re.sub(xpath_pattern, '', content, flags=re.DOTALL)
    
    xpath_inside_pattern = r'<xpath expr="//div\[@id=\'wrap\'\]" position="inside">.*?</xpath>'
    
    new_xpath = """<xpath expr="//div[@id='wrap']" position="replace">
            <div id="wrap" class="ew-homepage">
                <div class="oe_structure oe_empty" id="ew_zone_1"/>
                <t t-call="elyworld_website_home.s_ew_hero"/>
                <div class="oe_structure oe_empty" id="ew_zone_2"/>
                <t t-call="elyworld_website_home.s_ew_categories"/>
                <div class="oe_structure oe_empty" id="ew_zone_3"/>
                <t t-call="elyworld_website_home.s_ew_about"/>
                <div class="oe_structure oe_empty" id="ew_zone_4"/>
                <t t-call="elyworld_website_home.s_ew_gallery"/>
                <div class="oe_structure oe_empty" id="ew_zone_5"/>
                <t t-call="elyworld_website_home.s_ew_news"/>
                <div class="oe_structure oe_empty" id="ew_zone_6"/>
                <t t-call="elyworld_website_home.s_ew_contact"/>
                <div class="oe_structure oe_empty" id="ew_zone_7"/>
            </div>
        </xpath>"""
        
    content = re.sub(xpath_inside_pattern, new_xpath, content, flags=re.DOTALL)
    
    # Remove empty lines left by the first xpath removal
    content = re.sub(r'\n\s*\n\s*<xpath expr="//div\[@id=\'wrap\'\]" position="replace">', 
                     '\n        <xpath expr="//div[@id=\'wrap\']" position="replace">', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Refactoring to sibling oe_structure complete.")

if __name__ == '__main__':
    refactor()
