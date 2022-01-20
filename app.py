from configparser import ConfigParser
from PIL import ImageGrab
import os
import time
import win32api
import win32con
import logging
import asyncio


class MyBot():
    def __init__(self) -> None:
        logging.basicConfig(format='%(asctime)s %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p', filename='app.log', level=logging.INFO,)
        self.configObject = ConfigParser()
        self.configObject.read("config.ini")
        self.grab = ImageGrab
        self.mainPath = os.path.dirname(__file__)
        self.pathPhoto = os.path.join(self.mainPath, "photo")
        self.box = ()
        self.start_time = 0
        self.time_loop_swap = 0
        self.time_loop_refresh = 0
        self.posConnectWallet = (int(self.configObject["POSITIONS"]["CONNECT_WALLET_X"]), int(
            self.configObject["POSITIONS"]["CONNECT_WALLET_Y"]))
        self.posMetaSign = (int(self.configObject["POSITIONS"]["META_SIGN_X"]), int(
            self.configObject["POSITIONS"]["META_SIGN_Y"]))
        self.posHeroes = (int(self.configObject["POSITIONS"]["HEROES_X"]), int(
            self.configObject["POSITIONS"]["HEROES_Y"]))
        self.posReset = (int(self.configObject["POSITIONS"]["RESET_X"]), int(
            self.configObject["POSITIONS"]["RESET_Y"]))
        self.posAll = (int(self.configObject["POSITIONS"]["ALL_X"]), int(
            self.configObject["POSITIONS"]["ALL_Y"]))
        self.posExitHeroes = (int(self.configObject["POSITIONS"]["EXIT_HEROES_X"]), int(
            self.configObject["POSITIONS"]["EXIT_HEROES_Y"]))
        self.posTreasureHunt = (int(self.configObject["POSITIONS"]["TREASUREHUNT_X"]), int(
            self.configObject["POSITIONS"]["TREASUREHUNT_Y"]))
        self.posWallet = (int(self.configObject["POSITIONS"]["WALLET_X"]), int(
            self.configObject["POSITIONS"]["WALLET_Y"]))
        self.posExitWallet = (int(self.configObject["POSITIONS"]["EXIT_WALLET_X"]), int(
            self.configObject["POSITIONS"]["EXIT_WALLET_Y"]))
        self.posPauseAndSelectHeroes = (int(self.configObject["POSITIONS"]["PAUSE_AND_SELECT_HEROES_X"]), int(
            self.configObject["POSITIONS"]["PAUSE_AND_SELECT_HEROES_Y"]))
        self.delayLoopSwapPage = 60 * \
            int(self.configObject["POSITIONS"]["DELAY_LOOP_SWAP_PAGE"])
        self.delayLoopRefreshStamina = 60 * \
            int(self.configObject["POSITIONS"]["DELAY_LOOP_REFRESH_STAMINA"])
        self.processing = False
        self.loop = asyncio.get_event_loop()

    def mouseClick(self, cord):
        win32api.SetCursorPos((cord[0], cord[1]))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(0.3)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    def startGame(self):
        logging.info('Start Game')
        self.mouseClick(self.posConnectWallet)
        logging.info('Connect Wallet')
        time.sleep(5)
        self.mouseClick(self.posMetaSign)
        logging.info('Connect Meta Sign')
        time.sleep(10)
        self.mouseClick(self.posHeroes)
        time.sleep(1)
        self.mouseClick(self.posHeroes)
        logging.info('Select Button Heroes')
        time.sleep(3)
        self.mouseClick(self.posReset)
        time.sleep(1)
        self.mouseClick(self.posReset)
        logging.info('Select Button Reset')
        time.sleep(3)
        self.mouseClick(self.posAll)
        time.sleep(1)
        self.mouseClick(self.posAll)
        logging.info('Select Button All')
        time.sleep(3)
        self.mouseClick(self.posExitHeroes)
        time.sleep(1)
        self.mouseClick(self.posExitHeroes)
        logging.info('Select Button Exit')
        time.sleep(3)
        self.mouseClick(self.posTreasureHunt)
        time.sleep(1)
        self.mouseClick(self.posTreasureHunt)
        logging.info('Go to Game')
        time.sleep(1)
        self.start_time = int(time.time() * 1000)

    def loopSwapPage(self):
        now = int(time.time() * 1000)
        if self.start_time > 0 and self.start_time > 0 and now - self.time_loop_swap > self.delayLoopSwapPage * 1000:
            logging.info("Loop Swap Page Start")
            self.time_loop_swap = int(time.time() * 1000)
            print('Loop Swap Page Start')
            self.mouseClick(self.posWallet)
            time.sleep(1)
            self.mouseClick(self.posWallet)
            time.sleep(3)
            self.mouseClick(self.posExitWallet)
            time.sleep(1)
            self.mouseClick(self.posExitWallet)
            logging.info(
                f"Loop Swap Page Stop Pending {self.delayLoopSwapPage} Second")

    def loopRefreshStamina(self):
        now = int(time.time() * 1000)
        if self.start_time > 0 and now - self.time_loop_refresh > self.delayLoopRefreshStamina * 1000:
            self.time_loop_refresh = int(time.time() * 1000)
            logging.info("Loop Refresh Stamina Start")
            print("Loop Refresh Stamina Start")
            self.mouseClick(self.posPauseAndSelectHeroes)
            logging.info("Select Button Pause Game")
            time.sleep(3)
            self.mouseClick(self.posPauseAndSelectHeroes)
            logging.info("Select Button Heroes")
            time.sleep(3)
            self.mouseClick(self.posReset)
            time.sleep(1)
            self.mouseClick(self.posReset)
            logging.info("Select Button Reset")
            time.sleep(3)
            self.mouseClick(self.posAll)
            time.sleep(1)
            self.mouseClick(self.posAll)
            logging.info("Select Button All")
            time.sleep(3)
            self.mouseClick(self.posExitHeroes)
            time.sleep(1)
            self.mouseClick(self.posExitHeroes)
            logging.info("Go to Game")
            time.sleep(3)
            self.mouseClick(self.posTreasureHunt)
            logging.info(
                f"Loop Refresh Stamina Stop Pending {self.delayLoopRefreshStamina} Second")
            self.processing = False

    def run(self):
        self.startGame()
        while True:
            self.loopSwapPage()
            self.loopRefreshStamina()
            print('sleep 10 second')
            time.sleep(10)

bot = MyBot()
event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(bot.run())
    event_loop.run_forever()
finally:
    event_loop.close()
