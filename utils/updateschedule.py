import schedule
import time
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from utils.log import logger
from domain.covid import get as get_covid
from domain.air_quality import get as get_air_quality_pm10
from domain.air_quality import get as get_air_quality_pm25
from domain import update_cache

update_cache.run()

def job():
    get_covid.get()
    get_air_quality_pm10.get()
    get_air_quality_pm25.get()
    print("Data update is executed on :05")

schedule.every().hour.at(":05").do(job) #정시 05분마다 do job
#schedule.every(1).minutes.do(job) #테스트용 1분마다 do job
while True:
    schedule.run_pending()
    time.sleep(30)
    #print("waiting")
