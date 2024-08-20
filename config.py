import os

API_ID = 952608

API_HASH = os.environ.get("API_HASH", "8d8d0ad8e3d4bcd54420190f57da78ad")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6599725318:AAH-Bvp6bX9mP4a8uwOOECrLPGU0x0LiQgM")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", "818269274" ))

LOG = ""

# UPDATE_GRP = , # bot sat group

# auth_chats = []

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "502980590").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


