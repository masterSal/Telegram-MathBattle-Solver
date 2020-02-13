#!/usr/bin/env python3
import time
import logging
from selenium import webdriver

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.INFO)

class MathBattleCheat:
    def __init__(self, url, gdriver, score, delay=1):
        self.url = str(url) # url
        self.gecko = str(gdriver) # geckodriver
        self.delay = int(delay) # delay before evaultion the next math challenge
        self.score = int(score) # how many challenges to solve
        self.firefox = webdriver.Firefox(executable_path=self.gecko) # driver
        self.x = None # x value
        self.y = None # y value
        self.op = None # opration
        self.res = None # challange result

        logging.info("Init...")
    

    def bopen(self):
        logging.info("Opening url...")
        self.firefox.get(self.url) # open browser and load url
    
    
    def bclose(self):
        logging.info("Closing broswer...")
        self.firefox.close() # close browser
    
    
    def startGame(self):
        logging.info("Starting the game...")
        self.firefox.find_elements_by_class_name("icon_play")[0].click() # find element by class name and click
    
    
    def right(self):
        logging.info("Right answer...")
        self.firefox.find_element_by_id("button_correct").click() # click correct button
    

    def wrong(self):
        logging.info("Wrong answer...")
        self.firefox.find_element_by_id("button_wrong").click() # click wrong button
    

    def getOp(self):
        o = self.firefox.find_element_by_id("task_op").text # get the opration
        # this part is need because when the opreation is fetched from
        # the game the eval() function throws and error because it's not the
        # correct oprator
        #
        # e.g.
        #   '×' - python can't evaluate '×' as *(times) so it need to be changed to *
        #   '–' - and this minu charator is diffrent from the regular '-' char
        #       
        #   '–' != '-'
        if o == "":
            return '*'
        elif o == "–":
            return '-'
        return o

    
    def getValues(self):
        # get all four values
        # x value
        # y value
        # oprator
        # and the result
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
        eValue = eval(self.x + self.op + self.y) # eval the values
        logging.info("eValue: " + str(eValue))

        # change into int and compare
        if int(eValue) == int(self.res):
            self.right() # if its correct, click button_correct
        else:
            self.wrong() # if its not, click button_wrong

    def start(self):
        self.bopen() # open browser
        self.startGame() # click the play button

        # delay
        time.sleep(2) # give it 2 sec to start the game
        
        while self.score != 0:
            self.getValues() # get all values
            self.evalute() # evaluate
            
            # decrease
            self.score -= 1
            logging.info("Sleeping for {} sec...".format(str(self.delay)))
            time.sleep(self.delay) # delay
        
        # delay
        logging.info("15 Second delay.")
        time.sleep(15)
        self.bclose() # close the browser





def main():
    try:
        mbc = MathBattleCheat(
            url="https://tbot.xyz/math/#eyJ1Ijo2NTgyNTg3NDIsIm4iOiJI4oiGZGVzICIsImciOiJNYXRoQmF0dGxlIiwiY2kiOiIyMjA5OTM3NjE3NTQ0NDAzMTUiLCJpIjoiQkFBQUFNNEFBQURMZ2NTeUdqLVRORVY3YXF3In05MmM1N2Y2YTc3OGQzMTU0NTBlOTNjMzA4M2I1MjY2ZA==", 
            gdriver="./geckodriver", 
            score=100
            )
        mbc.start() # start the whole process.
    except Exception as e:
        logging.error("Exception: " + e.msg)



if __name__ == "__main__":
    main()