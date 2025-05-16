from scraper.scraper_custom import ProductScraper
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
import pandas as pd

def main():
    os.makedirs("data/custom", exist_ok=True)

    base_url = "https://www.amazon.com/s?k=exterior+lamps"  
    scraper = ProductScraper(base_url)
    print(" Starting scraping custom products...")
    products = scraper.scrape_all(max_pages=5)

    if not products:
        print("No products scraped. Exiting.")
        return

    csv_path = "data/custom_products.csv"
    scraper.export_to_csv(products, csv_path)

   
    raw_df = pd.read_csv(csv_path)
    raw_df['price'] = raw_df['price'].astype(str).str.replace('..', '.', regex=False)
    raw_df.to_csv(csv_path, index=False)  

    
    df = load_data(csv_path)

    if df.empty:
        print("⚠️ DataFrame empty after loading CSV. Exiting.")
        return

    df = price_clustering(df)

    print("\n=== Résumé par cluster de prix ===")
    print(summary_by_cluster(df))


    plot_price_histogram(df, filename="data/histogram_price_custom.png")
    plot_price_boxplot(df, filename="data/boxplot_price_custom.png")
    plot_price_clusters(df, filename="data/clustering_price_custom.png")
    plot_cluster_distribution(df, filename="data/cluster_boxplot_custom.png")

    print("\n Visualisations enregistrées dans le dossier 'data/'.")

if __name__ == "__main__":
    main()
