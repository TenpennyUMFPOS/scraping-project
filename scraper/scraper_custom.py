import requests
from bs4 import BeautifulSoup
import csv
import time
import random

class Product:
    def __init__(self, title, price, source):
        self.title = title
        self.price = price
        self.source = source

    def to_dict(self):
        return {
            "title": self.title,
            "price": self.price,
            "source": self.source
        }

class ProductScraper:
    def __init__(self, base_url, headers=None):
        self.base_url = base_url
        self.headers = headers or {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/122.0.0.0 Safari/537.36"
        }

    def scrape_page(self, url):
        response = requests.get(url, headers=self.headers)
        if response.status_code != 200:
            print(f" Failed to load: {url} - Status {response.status_code}")
            return []

        soup = BeautifulSoup(response.text, 'html.parser')
        products = []

 
        items = soup.select('.product_pod') 
        for item in items:
            title = item.h3.a['title']
            price = item.select_one('.price_color').text.replace('£', '').strip()
            source = url
            products.append(Product(title, price, source))

        return products

    def scrape_all(self, max_pages=10):
        all_products = []
        for page in range(1, max_pages + 1):
            url = f"{self.base_url}/catalogue/page-{page}.html"
            print(f" Scraping page {page}...")
            products = self.scrape_page(url)
            all_products.extend(products)
            time.sleep(random.uniform(1, 2))  

            if len(products) == 0:
                break  

        return all_products

    def export_to_csv(self, products, filename):
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['title', 'price', 'source'])
            writer.writeheader()
            for product in products:
                writer.writerow(product.to_dict())
        print(f" {len(products)} produits exportés vers {filename}")
