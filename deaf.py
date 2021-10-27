#!/usr/bin/python3

import logging
import time
from threading import Thread
from kalliope import Utils 

logging.basicConfig()
logger = logging.getLogger("kalliope")


class Deaf(Thread):
    def __init__(self, **kwargs):
        super(Deaf, self).__init__()
        logger.debug("[trigger:deaf] __init__()")

    def run(self):
        logger.debug("[trigger:deaf] run()")
        while True:
            time.sleep(1)

    def pause(self):
        logger.debug("[trigger:deaf] pause()")

    def unpause(self):
        logger.debug("[trigger:deaf] unpause()")

