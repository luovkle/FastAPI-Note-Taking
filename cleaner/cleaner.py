#!/usr/bin/env python3

import datetime
import logging
import os
import sys
import time


def get_logger() -> logging.Logger:
    logger = logging.getLogger("logger")
    logger.setLevel(logging.DEBUG)
    console_handler = logging.StreamHandler(sys.stdout)
    logger.addHandler(console_handler)
    return logger


def get_dir(logger: logging.Logger) -> str:
    try:
        s_dir = sys.argv[1]
    except IndexError:
        logger.error("[✗] A directory must be specified")
        exit(1)
    else:
        if not os.path.isdir(s_dir):
            logger.error("[✗] Directory does not exist")
            exit(1)
        else:
            return s_dir


def clear(path: str, logger: logging.Logger) -> None:
    dt_u = datetime.datetime.utcnow()
    dir_list = os.listdir(path)
    files = []
    for element in dir_list:
        if os.path.isfile(f"{path}/{element}"):
            files.append(element)
    for file in files:
        c_time = os.path.getctime(f"{path}/{file}")
        dt_c = datetime.datetime.fromtimestamp(c_time)
        if abs(dt_u - dt_c).days >= 1:
            if file[-3:] == "zip":
                os.remove(f"{path}/{file}")
                logger.info(f"[•] File {file} has been deleted")


def main() -> None:
    logger = get_logger()
    logger.info("[•] Running script")
    s_dir = get_dir(logger)
    path = f"{os.getcwd()}/{s_dir}"
    while True:
        clear(path, logger)
        time.sleep(60 * 60)  # 1 hour


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit(0)
