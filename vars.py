#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "26738089"))
API_HASH = environ.get("API_HASH", "5e28dcf17a1c58cfe7cf75d175f359a1")
BOT_TOKEN = environ.get("BOT_TOKEN", "8091073054:AAGMIxW4ThK0qIrnMaVWxT_bBcGQdJw4Ylk")
OWNER = int(environ.get("OWNER", "8109989096"))
CREDIT = "VISH BOTS"
AUTH_USER = os.environ.get('AUTH_USERS', '5680454765').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
