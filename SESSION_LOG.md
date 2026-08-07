# ElyWorld Odoo 19 Deployment & Customization Session Log

**Date**: August 3, 2026  
**Target System**: `https://ely-world.ccvi.com.vn/`  
**Odoo Version**: `19.0-20260723`  
**Database**: `odoo`  
**Company**: `ELy World Access Company Limited`  

---

## 1. System Connectivity & Verification

- Verified XML-RPC connectivity using API key authentication (`username: admin`, UID: `2`).
- Validated server info and company setup via standard Odoo XML-RPC endpoints (`/xmlrpc/2/common` & `/xmlrpc/2/object`).
- Script used: [`test_odoo_api.py`](file:///D:/Project/QQ/odoo-template/test_odoo_api.py).

---

## 2. Issue Resolution & Configuration Summary

### Issue A: Heading Layout Wrapping in Vietnamese ("HÌNH ẢNH TỪ NÔNG TRẠI")
- **Symptom**: In the Vietnamese UI (`/vi_VN`), the section title "HÌNH ẢNH TỪ NÔNG TRẠI" was crunched into a narrow block rather than expanding horizontally like English ("IMAGES FROM THE FARM").
- **Root Cause**: View record `2275` (`elyworld_website_home.s_ew_gallery`) contained nested WYSIWYG animation/size tags (`<span class="h2-fs">`, `<span class="o_animated_text o_animate o_anim_fade_in o_visible">`) and non-breaking space entities (`&nbsp;`) between words, gluing text together and constraining container width.
- **Action Taken**:
  - Sanitized the XML `arch_db` in `vi_VN` context directly in Odoo database via XML-RPC.
  - Replaced dirty HTML markup with clean standard tags: `<h2>HÌNH ẢNH TỪ NÔNG TRẠI</h2>`.
- **Status**: **RESOLVED** (Verified on live website).

---

### Issue B: Hardcoded Vietnamese Text in "CONTACT US" Section on English Page
- **Symptom**: Switching website to English (`/en_US`) still displayed Vietnamese text for contact form placeholders, headings, contact card info, and dropdown category options (*Thực phẩm tiện lợi, Trái cây & Nông sản sấy...*).
- **Root Cause**:
  - Website Editor saved custom Copy-on-Write (COW) view records (`2278` & `2269`) with Vietnamese as the base source text.
  - In Odoo 19, missing `en_US` translation mappings in `ir.ui.view` JSONB field translation tables caused fallback to Vietnamese source text.
- **Action Taken**:
  - Restructured base architecture (`arch_base` and `arch_db`) for views `2269` and `2278`.
  - Applied `update_field_translations` API to map all form elements to English:
    - **Title**: `Get Product & Export Consultation`
    - **Placeholders**: `Company Name`, `Contact Name *`, `Email *`, `Phone Number / WhatsApp`, `Your Message`
    - **Dropdown Options**: `Convenience Food`, `Dried Fruit & Agricultural Products`, `Nuts & Snacks`, `Spices & Dried Vegetables`, `Canned Beverages`, `Gift Sets & Baskets`, `Packaging & Kraft Paper`, `Export Products`, `Other`
    - **Info Card**: `Contact Information`, `Address`, `Working Hours`, `Chat via WhatsApp`
- **Status**: **RESOLVED** (Verified live rendering for both `/en_US` and `/vi_VN`).

---

### Task C: Admin User Creation & Full Access Permission Setup
- **Request**: Create accounts for **Nhật Dương** (`nhatduong153@gmail.com`) and **Tường Vy** (`maituongvy2907@gmail.com`) with full content editing/administrator rights and default password `ElyWorld@123!`.
- **Action Taken**:
  - Provisioned/Updated both accounts in `res.users` with administrator roles (`group_system`, Website Editor & Designer, Sales Manager, System Administrator).
  - Assigned default password: `ElyWorld@123!`.
  - Validated authentication for both users via XML-RPC login API.
- **User Accounts Created**:
  1. **Nhật Dương**: `nhatduong153@gmail.com` (UID: `6`)
  2. **Tường Vy**: `maituongvy2907@gmail.com` (UID: `7`)
- **Status**: **COMPLETED & VERIFIED**.

---

## 3. Maintenance Instructions for Future Updates

1. **Heading Animation/Formatting Issues**:
   - If headings crunch on Website Editor, edit page in admin mode, select the heading element, and click **Clear Formatting** to strip inline `&nbsp;` and animation spans.
2. **Multilingual Form Options**:
   - Avoid hardcoding static `<option>` text directly in Vietnamese inside base XML views. Use English as base source text and maintain translations via Odoo's Translation interface or XML-RPC `update_field_translations`.
3. **User Management**:
   - New editor/admin accounts retain full rights to edit Website Builder components, Manage Products, and access Administrative Settings.
