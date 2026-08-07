# ElyWorld Website Home — Odoo Community 19

This module replaces `website.homepage`, customizes the public header/footer,
and creates CRM leads from the homepage contact form.

## Install

1. Copy the folder to the host custom addons directory:

   `/home/cadmin/odoo-elyworld/addons/elyworld_website_home`

2. Restart Odoo and update the app list.
3. Install **ElyWorld Website Home**.
4. Configure company/website logo, phone, email and menus in Odoo Website.
5. Replace SVG placeholder images under `static/src/img/` with licensed production images.

## Upgrade from command line

```bash
cd /home/cadmin/odoo-elyworld
docker compose exec -T odoo odoo -d elyworld -u elyworld_website_home --stop-after-init
# then recreate/start the normal service if required
docker compose up -d odoo
```

Use the actual database name if it differs from `elyworld`.
