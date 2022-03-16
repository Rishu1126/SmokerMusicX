from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "11616195"))
API_HASH = getenv("API_HASH", "ae9a6a6d10156fd905ef5c59125d0357")
BOT_TOKEN = getenv("BOT_TOKEN","5131219426:AAHV3ED4lXnecIGE8vFoNbvVEOjBuJf8xFY")
BOT_NAME = getenv("BOT_NAME"," 𝐓𝐒𝐆 𝐌𝐔𝐒𝐈𝐂 𝐁𝐎𝐓❤️")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "120"))
SESSION_NAME = getenv("SESSION_NAME", "AQBTStydQc-uVWtVwV0uJMv_h2FROQNPPwT6SVC73_FSllX9Dt3oi84Ug-URyJbpTTpKSnCCdjdWpBFrhkr9bmLOVamqagYJ1E_4fjjsWaIOe33R_MIj9jsNBcjLDA9qnB0WgQnIzqw31RAH9Wu7VGME6UZVj8PqhVZs2iQZzU313wNz2NogfyVUW55GMOuKZ19vZA4baKQN6WLZmDWMHNkKosBioHbLqwwLguRO6EKLN0wxgPj8IMYywV7FIj9ffds22kmIaheVTPRDRxnB_vfCxamoRwLsGJIJT7dkUv5gQKnlWBY75XWVROYHK7P8QJ6sqWs3693LM4fx--Fa5TmoAAAAASpvZCkA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5073888641").split()))
