# India Today Market News Scraper

A lightweight Python web scraper built with **Selenium** that extracts the top 5 latest business and market news headlines from [India Today](https://www.indiatoday.in/business/market) and saves them into a structured JSON file.

## Features
* **Headless Execution:** Runs Chrome in headless mode without opening a visible browser window.
* **Fast Loading:** Uses `eager` page load strategy to skip waiting on third-party ads and heavy media.
* **Resilient Selectors:** Targets article URL patterns (`/business/market/story/`) instead of fragile CSS class names.
* **Deduplication:** Filters out duplicate links and image-only anchor tags.
* **Structured Output:** Exports ranked headlines, article URLs, and a scrape timestamp to `indiatoday_market_news.json`.

## Tech Stack
* Python 3.x
* Selenium 4

## Setup & Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/](https://github.com/)<your-username>/<your-repo-name>.git
   cd <your-repo-name>
   ```

2. **Install dependencies:**
   ```bash
   pip install selenium
   ```

3. **Run the scraper:**
   ```bash
   python scrape_indiatoday_market.py
   ```

## Sample Output (`indiatoday_market_news.json`)

```json
{
    "source": "India Today - Business Market",
    "scraped_at": "2026-11-21 15:27:00",
    "count": 5,
    "articles": [
        {
            "rank": 1,
            "title": "Sensex falls nearly 300 points, Nifty below 25,500; Axis Bank down 3%",
            "url": "[https://www.indiatoday.in/business/market/story/sensex-falls-nearly-300-points-nifty-below-25500-axis-bank-down-3-3042859-2026-11-20](https://www.indiatoday.in/business/market/story/sensex-falls-nearly-300-points-nifty-below-25500-axis-bank-down-3-3042859-2026-11-20)"
        }
    ]
}
```
