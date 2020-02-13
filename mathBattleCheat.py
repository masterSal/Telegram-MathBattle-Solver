#!/usr/bin/env python3
import time
import logging
from selenium import webdriver

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.INFO)

class MathBattleCheat:
    def __init__(self, url, gdriver, score, delay=1):
        self.url = str(url)
        self.gecko = str(gdriver)
        self.delay = int(delay)
        self.score = int(score)
        self.firefox = webdriver.Firefox(executable_path=self.gecko)
        self.x = None
        self.y = None
        self.op = None
        self.res = None

        logging.info("Init...")
    

    def bopen(self):
        logging.info("Opening url...")
        self.firefox.get(self.url)
    
    
    def bclose(self):
        logging.info("Closing broswer...")
        self.firefox.close()
    
    
    def startGame(self):
        logging.info("Starting the game...")
        self.firefox.find_elements_by_class_name("icon_play")[0].click()
    
    
    def right(self):
        logging.info("Right answer...")
        self.firefox.find_element_by_id("button_correct").click()
    

    def wrong(self):
        logging.info("Wrong answer...")
        self.firefox.find_element_by_id("button_wrong").click()
    

    def getOp(self):
        o = self.firefox.find_element_by_id("task_op").text
        if o == "×":
            return '*'
        elif o == "–":
            return '-'
        return o

    
    def getValues(self):
        logging.info("Getting x...")
        self.x = self.firefox.find_element_by_id("task_x").text
        logging.info("Getting y...")
        self.y = self.firefox.find_element_by_id("task_y").text
        logging.info("Getting op...")
        self.op = self.getOp()
        logging.info("Getting res...")
        self.res = self.firefox.find_element_by_id("task_res").text
    

    def evalute(self):
        logging.info("Evaulating {}{}{}".format(str(self.x), str(self.op), str(self.y)))
        eValue = eval(self.x + self.op + self.y)
        logging.info("eValue: " + str(eValue))

        if int(eValue) == int(self.res):
            self.right()
        else:
            self.wrong()

    def start(self):
        self.bopen()
        self.startGame()

        # delay
        time.sleep(2)
        
        while self.score != 0:
            self.getValues()
            self.evalute()
            
            # decrease
            self.score -= 1
            logging.info("Sleeping for {} sec...".format(str(self.delay)))
            time.sleep(self.delay)
        
        # delay
        logging.info("15 Second delay.")
        time.sleep(15)
        self.bclose()





def main():
    try:
        mbc = MathBattleCheat(
            url="https://tbot.xyz/math/#eyJ1Ijo2NTgyNTg3NDIsIm4iOiJI4oiGZGVzICIsImciOiJNYXRoQmF0dGxlIiwiY2kiOiIyMjA5OTM3NjE3NTQ0NDAzMTUiLCJpIjoiQkFBQUFNNEFBQURMZ2NTeUdqLVRORVY3YXF3In05MmM1N2Y2YTc3OGQzMTU0NTBlOTNjMzA4M2I1MjY2ZA==", 
            gdriver="./geckodriver", 
            score=100
            )
        mbc.start()
    except Exception as e:
        logging.error("Exception: " + e.msg)



if __name__ == "__main__":
    main()