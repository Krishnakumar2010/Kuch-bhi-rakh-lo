

from os import environ

API_ID = int(environ.get("API_ID", "21380713"))
API_HASH = environ.get("API_HASH", "3fa29c6d0bfe4909c6e9bac6fa1fecbc")
BOT_TOKEN = environ.get("BOT_TOKEN", "")

# Force Subscribe Configuration
FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "txt_uploder_bot1")  # Channel username without @, 
FORCE_SUB_CHANNEL_LINK = environ.get("FORCE_SUB_CHANNEL_LINK", "https://t.me/txt_uploder_bot1")  # Channel link

# Admin Configuration
ADMINS = list(map(int, environ.get("ADMINS", "8430030782").split()))

# Optional: Bot Owner ID
OWNER_ID = int(environ.get("OWNER_ID", "8430030782"))

# Database URL (if you want to add database support later)
DATABASE_URL = environ.get("DATABASE_URL", "")






