{
    "name": "Sale Website Home",
    "summary": "Custom Sale Website homepage, header, footer, pages and CRM contact form",
    "description": """
Sale website presentation layer for Odoo Community 19.
Replaces the default homepage and provides a branded public website layout.
    """,
    "version": "19.0.1.0.0",
    "category": "Website/Theme",
    "author": "CCVI Technology JSC",
    "website": "https://ccvi.vn",
    "license": "LGPL-3",
    "depends": [
        "website",
        "website_sale",
        "website_blog",
        "crm",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/layout.xml",
        "views/homepage.xml",
        "views/pages.xml",
        "views/toast_views.xml",
    ],
    "installable": True,
    "application": False,
}
