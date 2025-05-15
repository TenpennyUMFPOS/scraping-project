from scraper_custom import ProductScraper

def main():
  
    base_url = (
        "https://www.amazon.fr/s?k=lampes+d%27extérieur"
        "&rh=n%3A282861"  
    )

    scraper = ProductScraper(base_url)
    products = scraper.scrape_all(max_pages=5)  
    scraper.export_to_csv(products, "data/custom_products.csv")

if __name__ == "__main__":
    main()
