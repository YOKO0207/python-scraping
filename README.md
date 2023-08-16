# python scraping
#### Video Demo: https://youtu.be/PhwVrb_dw4I
#### Description:
This is a python script to scrape amzon products.
Scraping is a powerful tool to collect huge amounf of data. Collected data could be used to get marketing insights or even used for machine learning data.
<br>
There are useful library to use with Python. This time, I used beautiful soup for scraping.
<br>
When scraping web pages, one thing to note is that those libraries can only get server side contents, so contens that are loaded after the page gets rendered cannot be retrieved with thoese scraping libraries. Since a lot of modern web pages use javascript frameworks such as React, Vuejs to improve UX performance, I needed to consider how to get web contents in that kind of web pages. In order to address this issue I used one library called selenium to enable scraping on javascript loaded contents.
<br>
After scraping amazon products data, I export those data to csv file with title as the product name and price as the product price name.

here is the walk through of provided code.
```python
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
```
First, I stored web page url to scrape on. Next, I created chrome driver to open a web browser to scrape. In try block, I wrote a program to wait until it gets targeted div element, finally, I stored page contents, and quit driver.

```python
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
```
In above code, I pass scraped object to beautiful soup to convert it to beautiful soup object to get targeted contents.
After that, I iterate each object and store contents in csv file.