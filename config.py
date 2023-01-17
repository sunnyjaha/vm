import os


class Config(object):
    API_HASH = os.environ.get("API_HASH", "e49a46ce63b238c429d618c4aa37f52e")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5926043698:AAG4daQ4MdWocRmbiBk6s7UCcslQdDbE808")
    TELEGRAM_API = os.environ["TELEGRAM_API", "16734393"]
    OWNER = os.environ.get("OWNER", "5543917190")
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "@Am_Robots")
    PASSWORD = os.environ.get("PASSWORD", "1234")
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://mirror:mirror@cluster0.lhuiojc.mongodb.net/?retryWrites=true&w=majority")
    LOGCHANNEL = os.environ.get("LOGCHANNEL", "-1001806844111")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID","1VSSyVvO1hpuK9HtPFtW3rAj-TLhAHBzl")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "BQD_WLkAcrBw6ci1KZQHQeEMKvukl11axSfW4kwdyiXSH12Je99jkyEWUCGlW0OGbF6vN1EVrUtr7rW5BpInMmT1YbqyAC37yPrnc9K3QvBV09xVznvXWATobZPiw6ZPQ-wCYUcHakHlM_ik53Gvmh77lnbGjIWAqOcCHAjiOLWVXW37yvtLI3AbqcgO2dubSoZAaoagiNIPMZhHm2EtphLtgo0XWMRmDgNPuA_OfsWaF5SKofm4q-GtOp1fqjBYn5c46xf_V2Pq-xxxDdsC1t9ppgNeRo4to0zbS_JpQbblM43_-BtLzHm_3RgvrmW2d3piUqjEZwm_q4V6CjzorYWnuTZ62QAAAABOHUhrAA")
    IS_PREMIUM = True
    MODES = ["video-video", "video-audio", "video-subtitle","extract-streams"]
