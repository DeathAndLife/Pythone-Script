from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import base64


options = Options()
options.add_argument("--mute-audio")
options.add_argument('headless')
options.binary_location = "/opt/google/chrome/google-chrome"
driver = webdriver.Chrome('chromedriver', options=options)
driver.minimize_window()
driver.get("https://proxy.yugogo.xyz/vmess/sub")


def get():
    reqResult = driver.find_element_by_tag_name("pre").text
    result = base64.b64decode(reqResult).decode("utf-8")
    print(str(result))
    driver.close()


if __name__ == "__main__":
    get()
