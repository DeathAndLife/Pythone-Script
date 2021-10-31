from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import threading
import time
import os
import QRCode

options = Options()
options.add_argument("--mute-audio")
options.add_argument('headless')
options.binary_location = "/opt/apps/cn.google.chrome/files/google-chrome"
driver = webdriver.Chrome('chromedriver', options=options)
driver.minimize_window()
driver.get("https://www.youtube.com/watch?v=a_8_CRE_RhU")


def get_QR_doe():
    play = driver.find_element_by_class_name("ytp-play-button").get_attribute("aria-label")
    if "播放" in play:
        driver.find_element_by_class_name("ytp-play-button").click()

    png = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
    driver.get_screenshot_as_file(r"%s.png" % png)

    QRCode.get_ewm(os.getcwd() + "/" + png + ".png")

    t = threading.Timer(30, get_QR_doe)
    t.start()


if __name__ == "__main__":
    get_QR_doe()
