import json
import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    LICENSE_KEY = os.getenv("LICENSE_KEY")

    API_ID = os.getenv("API_ID")
    API_HASH = os.getenv("API_HASH")

    REF_ID = os.getenv("REF_ID", "f441146600_s574068")
    AUTO_UPGRADE_PAINT_REWARD = os.getenv("AUTO_UPGRADE_PAINT_REWARD", "True")
    AUTO_UPGRADE_RECHARGE_SPEED = os.getenv("AUTO_UPGRADE_RECHARGE_SPEED", "True")
    AUTO_UPGRADE_RECHARGE_ENERGY = os.getenv("AUTO_UPGRADE_RECHARGE_ENERGY", "True")
    AUTO_TASK = os.getenv("AUTO_TASK", "True")

    USE_PUMPKIN_BOMBS = os.getenv("USE_PUMPKIN_BOMBS", "True")

    USE_CUSTOM_TEMPLATE = os.getenv("USE_CUSTOM_TEMPLATE", "False")
    CUSTOM_TEMPLATE_ID = int(os.getenv("CUSTOM_TEMPLATE_ID", "1006282664"))
    PAINT_COLOR = (os.getenv("PAINT_COLOR", "000000"))
    USE_RANDOM_TEMPLATES = os.getenv("USE_RANDOM_TEMPLATES", "True")
    RANDOM_TEMPLATES_ID = json.loads(os.getenv("RANDOM_TEMPLATES_ID", "[917981974, 7319890725, 1972552043]"))

    NIGHT_MODE = os.getenv("NIGHT_MODE", "False")
    SLEEP_TIME = json.loads(os.getenv("SLEEP_TIME", "[0, 7]")) # your time zone 

    DELAY_EACH_ACCOUNT = json.loads(os.getenv("DELAY_EACH_ACCOUNT", "[10, 15]"))
    SLEEP_TIME_BETWEEN_EACH_ROUND = json.loads(os.getenv("SLEEP_TIME_BETWEEN_EACH_ROUND", "[1000, 1500]"))
    USE_PROXY_FROM_FILE = os.getenv("USE_PROXY_FROM_FILE", "False")


settings = Settings()
