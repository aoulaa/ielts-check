import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))

group_username = ['@essay_check_admins']
# admins = [
#     os.getenv("ADMIN_ID"),
# ]
admins = [
    61888314,
]
channels = ['@ielts_essay_writing']

ip = os.getenv("ip")

aiogram_redis = {
    'host': ip,
}

redis = {
    'address': (ip, 6379),
    'encoding': 'utf8'
}
