import os
from enum import Enum

# database
db_name = "data.db"


# version = RunVersion.debug
class RunVersion(Enum):
    debug = "DEBUG"
    demo = "DEMO"


version = RunVersion.demo

# arduino
# port = "COM3"
# port = "/dev/cu.Bluetooth-Incoming-Port"
port = "/dev/cu.usbmodem1101"
baudrate = 9600

# chrome driver
current_dir = os.path.dirname(os.path.abspath(__file__))
driver_path = os.path.join(current_dir, './chromedriver/chromedriver')

covid_url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%BD%94%EB%A1%9C%EB%82%98"

cold_seongbuk_gu_code = 11290
