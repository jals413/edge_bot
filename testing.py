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

driver.get("https://www.bing.com/ ")
# For maximizing window
driver.maximize_window()

driver.implicitly_wait(5)

