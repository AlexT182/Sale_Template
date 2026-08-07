{
    "name": "ElyWorld Website Home",
    "summary": "Custom ElyWorld homepage, header, footer and CRM contact form",
    "description": """
ElyWorld website presentation layer for Odoo Community 19.
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
        "views/layout.xml",
        "views/homepage.xml",
    ],
    "assets": {
        "web.assets_frontend": [
            "elyworld_website_home/static/src/scss/elyworld.scss",
            "elyworld_website_home/static/src/js/elyworld.js",
        ],
    },
    "installable": True,
    "application": False,
}
