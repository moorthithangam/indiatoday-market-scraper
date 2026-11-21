import json
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def scrape_top_5_market_news():
    url = "https://www.indiatoday.in/business/market"

    options = Options()
    options.page_load_strategy = "eager"  # Don't wait for ads/images to finish
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--log-level=3")  # Suppress console errors
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    )

    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(20)

    try:
        driver.get(url)

        wait = WebDriverWait(driver, 15)
        wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "a[href*='/business/market/story/']")
            )
        )

        link_elements = driver.find_elements(
            By.CSS_SELECTOR, "a[href*='/business/market/story/']"
        )

        news_list = []
        seen_urls = set()

        for elem in link_elements:
            title = elem.text.strip()
            href = elem.get_attribute("href")

            if title and len(title) > 20 and href not in seen_urls:
                seen_urls.add(href)
                news_list.append({
                    "rank": len(news_list) + 1,
                    "title": title,
                    "url": href
                })

            if len(news_list) == 5:
                break

        return news_list

    finally:
        driver.quit()


def save_to_json(news_data, filename="indiatoday_market_news.json"):
    output = {
        "source": "India Today - Business Market",
        "scraped_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "count": len(news_data),
        "articles": news_data
    }

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=4, ensure_ascii=False)

    print(f"Successfully saved {len(news_data)} articles to {filename}")


if __name__ == "__main__":
    top_news = scrape_top_5_market_news()

    if top_news:
        save_to_json(top_news)
    else:
        print("No articles found.")