from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time
import random

driver_path = r"D:\chromedriver-win64\chromedriver.exe"
service = Service(driver_path)

options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36")

driver = webdriver.Chrome(service=service, options=options)

keyword = "top 10 betting sites"
driver.get("https://www.google.com")
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys(keyword)
search_box.send_keys(Keys.RETURN)

data = []

for page in range(1, 11):
    print(f"Scraping page {page}...")
    time.sleep(random.uniform(3, 6))
    
    results = driver.find_elements(By.XPATH, "//*[@id='rso']/div")

    for rank, result in enumerate(results, start=1):
        try:
          
            url = result.find_element(By.XPATH, ".//a").get_attribute("href")
        except:
            url = ""
        
        try:
          
            title = result.find_element(By.XPATH, ".//h3").text
        except:
            title = ""
        
        try:

            description = result.find_element(By.XPATH, ".//div[contains(@class, 'VwiC3b')]").text
        except:
            description = ""

        data.append({
            "Url": url,
            "Title": title,
            "Description": description,
            "Rank": rank,
            "Page Number": page
        })

    try:
        next_button = driver.find_element(By.XPATH, "//a[@id='pnnext']")
        next_button.click()
    except:
        print("No more pages available.")
        break

output_file = "google_search_selenium_results.csv"
df = pd.DataFrame(data)
df.to_csv(output_file, index=False)
print(f"Data saved to {output_file}")
driver.quit()
