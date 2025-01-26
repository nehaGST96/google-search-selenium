from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_data_with_selenium():

    service = Service('D:\chromedriver-win64\chromedriver.exe')
    driver = webdriver.Chrome(service=service)

    try:
        
        url = "https://bongda24h.vn/nhan-dinh-bong-da-c344-p1.html"
        driver.get(url)

    
        wait = WebDriverWait(driver, 10)
        articles = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.section-content > article')))

        match_data = []

        
        for article in articles:
            try:
                match_title = article.find_element(By.CSS_SELECTOR, 'header > h3').text.strip()
            except:
                match_title = "N/A"

            try:
                match_time = article.find_element(By.CSS_SELECTOR, 'header > p.article-meta > span').text.strip()
            except:
                match_time = "N/A"

            try:
                league = article.find_element(By.CSS_SELECTOR, 'header > p.article-meta').text.strip()
            except:
                league = "N/A"

            try:
                home_team = article.find_element(By.CSS_SELECTOR, 'header > p.article-meta > a:nth-of-type(1)').text.strip()
            except:
                home_team = "N/A"

            try:
                away_team = article.find_element(By.CSS_SELECTOR, 'header > p.article-meta > a:nth-of-type(2)').text.strip()
            except:
                away_team = "N/A"

            try:
                home_logo = article.find_element(By.CSS_SELECTOR, 'p > a > picture > img').get_attribute('src')
            except:
                home_logo = "N/A"

            try:
                away_logo = article.find_element(By.CSS_SELECTOR, 'p > a:nth-of-type(2) > picture > img').get_attribute('src')
            except:
                away_logo = "N/A"

            try:
                content = article.find_element(By.CSS_SELECTOR, 'header > p.article-summary').text.strip()
            except:
                content = "N/A"

            match_data.append({
                "Title": match_title,
                "MatchTime": match_time,
                "League": league,
                "HomeName": home_team,
                "AwayName": away_team,
                "HomeLogo": home_logo,
                "AwayLogo": away_logo,
                "Content": content
            })

        return match_data

    finally:
        
        driver.quit()

if __name__ == "__main__":
    data = scrape_data_with_selenium()
    for item in data:
        print(item)
