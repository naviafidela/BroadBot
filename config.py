import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7508753099:AAHLs4Xcn7e9N2tXQu9EjGWnAn4efFAMmAs")
API_ID = int(os.environ.get("API_ID", "20786693"))
API_HASH = os.environ.get("API_HASH", "6eebbb7d9f9825a2d200c034bfbb7102")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002548704888"))
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "8181491671").split())
DB_URL = os.environ.get("DB_URL", "mongodb+srv://naviafidela:xILLUSION@10@broadcastbot.t920fzc.mongodb.net/")
DB_NAME = os.environ.get("DB_NAME", "naviafidela")

# broadcast settings

BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
MAX_CONCURRENT = int(os.environ.get("MAX_CONCURRENT", "10"))  # Maximum concurrent message sends. You can set this value up to 1000 if you are using a paid broadcast.
UPDATE_INTERVAL = int(os.environ.get("UPDATE_INTERVAL", "2"))  # Update interval in seconds to avoid flood waits
