from scraper.scraper_books import BookScraper
from scraper.scraper_custom import ProductScraper
from scraper.exporter import export_books_to_csv
from analysis.stats import (
    load_data,
    price_clustering,
    summary_by_cluster,
    plot_price_histogram,
    plot_price_boxplot,
    plot_price_clusters,
    plot_cluster_distribution,
)
import os

def main():
    os.makedirs("data", exist_ok=True)

    scraper = BookScraper()
    books = scraper.scrape_all()

    print(f"\n✅ Total de livres récupérés : {len(books)}")

    export_books_to_csv(books, "data/books.csv")

    df = load_data("data/books.csv")

    df = price_clustering(df)

    print("\n=== Résumé par cluster de prix ===")
    print(summary_by_cluster(df))

    # Generate and save visualizations
    plot_price_histogram(df)
    plot_price_boxplot(df)
    plot_price_clusters(df)
    plot_cluster_distribution(df)

    print("\n Visualisations enregistrées dans le dossier 'data/'.")


    scraper = ProductScraper("https://books.toscrape.com")
    products = scraper.scrape_all(max_pages=20)
    scraper.export_to_csv(products, "data/custom_products.csv")

if __name__ == "__main__":
    main()
