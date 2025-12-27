import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE) #logs로 시작해서 LOG_FILE형식으로 이름이 지어짐
os.makedirs(logs_path,exist_ok=True)  #경로에 이미 존재하더라도 무시하고 추가

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO

)

if __name__=="__main__":
    logging.info("Logging has started")