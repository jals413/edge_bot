import time
import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service

user_agent = "Mozilla/5.0 (Linux; Android 8.1.0; Pixel Build/OPM4.171019.021.D1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.109 Mobile Safari/537.36 EdgA/42.0.0.2057"
edge_Options = Options()
edge_Options.add_argument(f"--user-agent={user_agent}")

PATH = "C:/Program Files (x86)/msedgedriver.exe"
edge_Service = Service(PATH)

driver = webdriver.Edge(options=edge_Options)

driver.get("https://www.bing.com/")
driver.maximize_window()
time.sleep(3)

l=["hello", "hi", "netflix", "school", "amazon", "youtube", "goods", "rail", "gullible", "friend",
   "potato", "interest", "crash", "rampant", "adventurous", "slave", "star", "invention", "fail", "bocchi",
   ]
driver.get("https://www.bing.com/?step=signin&wlexpsignin=1")
time.sleep(15)
hamburger = driver.find_element(By.ID, "mHamburger")
hamburger.click()
# sign_in = driver.find_element(By.ID, "hb_n")
# sign_in.click()
time.sleep(4)


for i in l:
    driver.get("https://www.bing.com/")
    time.sleep(1)
    input_text = driver.find_element(By.ID, 'sb_form_q')
    input_text.send_keys(i)
    input_text.send_keys(Keys.ENTER)
    time.sleep(1)

driver.quit()
