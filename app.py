from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import csv

url = "https://www.amazon.com/s?k=nike"

driver = webdriver.Chrome()
driver.get(url)

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "a-section a-spacing-base"))
		)
finally:
    page_sourse = driver.page_source
    driver.quit()
    
soup = BeautifulSoup(page_sourse, "html.parser")
items = soup.find_all("div", class_=('a-section a-spacing-base'))

if not items is None:
	with open("products.csv", "w") as file:
			writer = csv.DictWriter(file, fieldnames=["title", "price"])
			writer.writeheader()
			for item in items:
				if not item is None:
					title = item.find("span", class_="a-size-base-plus a-color-base a-text-normal")
					price_symbol = item.find("span", class_="a-price-symbol")
					price_whole = item.find("span", class_="a-price-whole")
					price_fraction = item.find("span", class_="a-price-fraction")

					if not title is None and not price_symbol is None and not price_whole is None and not price_fraction is None:
						title = title.text.strip()
						price = price_symbol.text + price_whole.text + price_fraction.text
						writer.writerow({"title": title, "price": price})
    
