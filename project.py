from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os

os.makedirs("data", exist_ok=True)
options = Options()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
query = input("Enter the product to search: ")
file = 0
for i in range(1, 20):
    driver.get(f"http://www.amazon.in/s?k={query}&page={i}&crid=234WC15ZUST3N&sprefix=lap%2Caps%2C432&ref=nb_sb_noss_2")
    elems = driver.find_elements(By.CLASS_NAME, "puis-card-container")
    print(f"{len(elems)} items found")
    for elem in elems:
        d = elem.get_attribute("outerHTML")
        with open(f"data/{query}_{file}.html","w",encoding = "utf-8") as f:
            if d is not None:
                f.write(d)
            file +=1

    time.sleep(2)
driver.close()