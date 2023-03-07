import os
import time
import sys
from loguru import logger

logger.add(sys.stderr, format="{time:UTC} {level} {message}", filter="my_module", level="INFO")

sleep_time = 5


def print_env_variables():
    logger.info("I am printing env variables for this container. \n  {}".format(os.environ))


print_env_variables()

temp = True
i = 1
while temp:
    logger.info("Time is {}, iteration is --> {}".format(time.time(), i))
    i += 1
    time.sleep(sleep_time)
    # if i == 200:
    #     logger.info("I am done, stopping the container after 16 mins. Good bye :)")
    #     break