from scraper_custom import ProductScraper

def main():
    scraper = ProductScraper("https://books.toscrape.com")
    products = scraper.scrape_all(max_pages=20)
    scraper.export_to_csv(products, "../data/custom_products.csv")

if __name__ == "__main__":
    main()
