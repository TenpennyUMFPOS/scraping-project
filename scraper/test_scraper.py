from day4.product_analysis_project.scraper.scraper_books import BookScraper
from exporter import export_books_to_csv

def main():
    scraper = BookScraper()
    url = "https://books.toscrape.com/index.html"
    books = scraper.scrape_page(url)

    print(f"\n✅ {len(books)} livres trouvés sur la page d'accueil.\n")
    for book in books[:5]: 
        print(book)

    export_books_to_csv(books, "books.csv")

if __name__ == "__main__":
    main()
