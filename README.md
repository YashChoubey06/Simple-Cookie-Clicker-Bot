# Cookie Clicker Automation Bot

This is a simple Python bot that automatically plays the web game "Cookie Clicker" for five minutes. It's designed to demonstrate skills in browser automation, web scraping, and dynamic element handling.

The bot's strategy is to:
1.  Continuously click the main cookie.
2.  Instantly buy any available upgrade.
3.  Every 5 seconds, buy the most expensive product (e.g., Cursor, Grandma) currently available.

After 5 minutes, the script stops and prints the final "Cookies per Second" rate to the console.

## 🚀 Skills & Technologies Showcased

This project demonstrates proficiency in several key areas of web automation and scripting:

* **Python:** The core scripting language.
* **Selenium WebDriver:** The primary tool used for automating browser interaction.
* **Strategic Element Location:** Uses a mix of `ID`, `CSS_SELECTOR`, and `XPATH` to precisely target game elements.
* **Dynamic Wait Handling:** Implements `WebDriverWait` and `expected_conditions` to pause the script until elements are loaded and clickable, ensuring stability.
* **Data Scraping & Parsing:**
    * Extracts product prices from web elements.
    * Cleans and parses the text data (e.g., removing commas, converting to integers) to make it usable for comparison.
* **Algorithmic Logic:** Uses a `lambda` function within `max()` to programmatically determine the "most expensive" item to buy.
* **Robust Exception Handling:** Catches `StaleElementReferenceException` to prevent the script from crashing when the game's HTML is updated after a purchase.
* **JavaScript Execution:** Uses `driver.execute_script("arguments[0].click();", ...)` for more robust clicks on elements that might be obscured or tricky to interact with.
