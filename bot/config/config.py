import json
import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    LICENSE_KEY = os.getenv("LICENSE_KEY")

    API_ID = os.getenv("API_ID")
    API_HASH = os.getenv("API_HASH")

    REF_LINK = os.getenv("REF_LINK")
    ENABLE_AUTO_UPGRADE_BOOSTS = os.getenv("ENABLE_AUTO_UPGRADE_BOOSTS", "False")
    ENABLE_AUTO_TASKS = os.getenv("ENABLE_AUTO_TASKS", "True")

    PAINT_REWARD_MAX = int(os.getenv("PAINT_REWARD_MAX", "7"))
    ENERGY_LIMIT_MAX = int(os.getenv("ENERGY_LIMIT_MAX", "6"))
    RE_CHARGE_SPEED_MAX = int(os.getenv("RE_CHARGE_SPEED_MAX", "11"))

    BOOSTS_BLACK_LIST = json.loads(
        os.getenv(
            "BOOSTS_BLACK_LIST",
            '["INVITE_FRIENDS", "TON_TRANSACTION", "BOOST_CHANNEL", "ACTIVITY_CHALLENGE", "CONNECT_WALLET"]',
        )
    )
    TASKS_TODO_LIST = json.loads(
        os.getenv(
            "TASKS_TODO_LIST",
            '["x:notcoin", "x:notpixel", "paint20pixels", "leagueBonusSilver", "invite3frens", "leagueBonusGold", "channel:notpixel_channel", "channel:notcoin", "premium"]',
        )
    )

    DELAY_EACH_ACCOUNT = json.loads(os.getenv("DELAY_EACH_ACCOUNT", "[10, 15]"))
    DELAY_ALL_ACCOUNT = json.loads(os.getenv("DELAY_ALL_ACCOUNT", "[3600, 5000]"))
    USE_PROXY_FROM_FILE = os.getenv("USE_PROXY_FROM_FILE", "False")


settings = Settings()
