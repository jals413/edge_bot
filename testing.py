from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
import time

edge_Options = Options()

edge_Options.add_experimental_option("detach", True)


PATH = "C:/Program Files (x86)/msedgedriver.exe"
edge_Service = Service(PATH)

driver = webdriver.Edge(options=edge_Options)

driver.get("https://www.bing.com/")
driver.maximize_window()
time.sleep(3)

l=["hello", "hi", "netflix", "school", "amazon", "youtube", "goods", "rail", "gullible", "friend",
   "potato", "interest", "crash", "rampant", "adventurous", "slave", "star", "invention", "fail", "bocchi",
   "summer", "rain", "nori", "mackeral", "kagejitsu", "random", "yamero", "shakespeare", "udemy", "coursera",
   "rickroll", "amogus", "sus", "rent a girlfriend", "Jammu kashmir", "holiday spots", "my anime list", "team", "titans", "quantum"
   ]

for i in l:
    driver.get("https://www.bing.com/")
    time.sleep(1)
    input_text = driver.find_element(By.ID, 'sb_form_q')
    input_text.send_keys(i)
    input_text.send_keys(Keys.ENTER)
    time.sleep(1)

driver.quit()
