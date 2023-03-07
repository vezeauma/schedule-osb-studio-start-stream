#!/usr/bin/env python3

from obswebsocket import obsws, requests
import time
import logging
from datetime import datetime
import os
from sys import exit
from dotenv import load_dotenv

class ScheduleStart:

    def __init__(self, ip, port, secret,begin,end):
        self.ws = obsws(ip, port, secret)
        self.begin = begin
        self.end = end

    def start_live(self):
        # Commencer le streaming
        logging.info("Call StartStream")
        self.ws.call(requests.StartStream())

        # Attendre que le streaming soit en cours
        while True:
            status = self.ws.call(requests.GetStreamStatus())
            if status.getOutputActive():
                logging.info("Start to stream")
                break
            time.sleep(1)

    def finish_live(self):
        
        self.ws.call(requests.StopStream())
        while True:
            status = self.ws.call(requests.GetStreamStatus())
            if not status.getOutputActive():
                logging.info("Stream ending...")
                break
            time.sleep(1)

    def watcher(self,start):
        if start:
            while True:
                now = datetime.now()
                if now > self.end:
                    logging.fatal("Impossible to start")
                    exit(1)

                if now > self.begin:
                    break
                logging.info("Wait...")
                time.sleep(5)
        else:
            while True:
                now = datetime.now()
                if now > self.end:
                    break
                logging.info("Stream in progress...")
                time.sleep(5)



    def main(self):
        
        self.watcher(True)
        self.ws.connect()

        ScheduleStart.start_live(self)

        self.watcher(False)

        ScheduleStart.finish_live(self)

        # Fermer la connexion WebSocket
        self.ws.disconnect()


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler("debug.log"),
            logging.StreamHandler()
        ]
    )


    # charge les variables d'environnement du fichier .env
    load_dotenv()
    # utilise la variable d'environnement 'dans .env'
    ip = os.environ.get('IP')
    port = os.environ.get('PORT')
    secret = os.environ.get('SECRET')
    begin_str = os.environ.get('BEGIN')
    end_str = os.environ.get('END')
    begin = datetime.strptime(begin_str, '%m/%d/%y %H:%M:%S')
    end = datetime.strptime(end_str, '%m/%d/%y %H:%M:%S')

    schedule = ScheduleStart(ip, port, secret, begin, end)
    schedule.main()