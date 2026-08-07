import xmlrpc.client

url = "https://ely-world.ccvi.com.vn"
db = "odoo" # Try default docker db name, we will try others if this fails
username = "admin"
api_key = "693c960fe86d4212a3522973f880eeb76c602238"

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
print("Connecting to common...")
try:
    uid = common.authenticate(db, username, api_key, {})
    print(f"Authentication successful! UID: {uid}")
except Exception as e:
    print(f"Authentication failed with db '{db}': {e}")
    # Try to get db list
    try:
        db_list = common.list()
        print(f"Available databases: {db_list}")
    except Exception as e2:
        print(f"Could not list databases: {e2}")
