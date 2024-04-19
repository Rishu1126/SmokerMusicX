from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "11187664"))
API_HASH = getenv("API_HASH", "3e1cbd955611b5d7d3b9836a65771b2f")
BOT_TOKEN = getenv("BOT_TOKEN","6853139517:AAGfcsnZ9O44IIu_Khx5Lo7FRdlrrOPDTzA")
BOT_NAME = getenv("BOT_NAME"," KRISHU 𝐌𝐔𝐒𝐈𝐂 𝐁𝐎𝐓❤️")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "120"))
SESSION_NAME = getenv("SESSION_NAME", "BQB_R-rmr9FPpTRe0yIKFtpcbhnKZ7UG_uOPRk09rkQyjsBAFmBefu2flKM1Eonw4OXmVm1Pmr9ojMhxHrtqV9ETUkoLXRVhiTCagYqshJiZpFzlXvZCD3nPEX8q1RW2YbHs0BEqWNzlp3PHBhCaq183_Gw-P4rIIrQal5ZifUH4uQ8ZIEVn9Ir9zIVYPnNKZT_PNmEh332uys898ZDkP1iAVmhGN_0Ks6qNmlRC8QQq3jr6epFyswMzYHYxfFagieqXGVf-89VUq0VuU7pvsrlvLf0T-7_Vm1V8YcSL9byELHj_EiUGZ-6riXbtpvtjofrUOf55E82p5E44tXVTNf1YAAAAAZOKfY8A")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5516578116").split()))
