import requests
from bs4 import BeautifulSoup
import csv
import time
import random
import os

class Product:
    def __init__(self, title, price, source, img_url=None):
        self.title = title
        self.price = price
        self.source = source
        self.img_url = img_url

    def to_dict(self):
        return {
            "title": self.title,
            "price": self.price,
            "source": self.source,
            "img_url": self.img_url
        }

class ProductScraper:
    def __init__(self, base_url, headers=None):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update(headers or {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/113.0.0.0 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
        })

    def scrape_page(self, url):
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f" Failed to load {url}: {e}")
            return []

        soup = BeautifulSoup(response.text, 'html.parser')
        products = []

        product_sections = soup.select('div.a-section.a-spacing-base')

        for section in product_sections:
            title_tag = section.select_one('h2.a-size-base-plus.a-spacing-none.a-color-base.a-text-normal')
            title = title_tag.get_text(strip=True) if title_tag else None

            img_tag = section.select_one('img.s-image')
            img_url = img_tag['src'] if img_tag and img_tag.has_attr('src') else None

            price_whole = section.select_one('span.a-price-whole')
            price_fraction = section.select_one('span.a-price-fraction')

            if title and price_whole:
                price = price_whole.get_text(strip=True).replace(',', '')
                if price_fraction:
                    price += '.' + price_fraction.get_text(strip=True)
                source = url

                product = Product(title, price, source, img_url)
                products.append(product)

        return products

    def scrape_all(self, max_pages=5):
        all_products = []
        for page in range(1, max_pages + 1):
            url = f"{self.base_url}&page={page}"
            print(f"🔎 Scraping page {page}...")
            products = self.scrape_page(url)
            if not products:
                print("No products found, stopping.")
                break
            all_products.extend(products)
            time.sleep(random.uniform(1, 3))

        print(f"Total products scraped: {len(all_products)}")
        return all_products

    def export_to_csv(self, products, filename="data/custom_products.csv"):
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, 'w', newline='', encoding='utf-8') as f:

            writer = csv.DictWriter(f, fieldnames=['title', 'price', 'source', 'img_url'])
            writer.writeheader()
            for product in products:
                writer.writerow(product.to_dict())
        print(f" {len(products)} products exported to {filename}")
