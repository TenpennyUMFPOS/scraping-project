from analysis import stats

def main():

    df = stats.load_data("data/custom_products.csv")


    print("\n Statistiques descriptives des prix :")
    print(stats.describe_prices(df))


    df = stats.price_clustering(df)


    print("\n Résumé par cluster de prix :")
    print(stats.summary_by_cluster(df))


    stats.plot_price_histogram(df, filename="data/histogram_price_custom.png")
    stats.plot_price_boxplot(df, filename="data/boxplot_price_custom.png")
    stats.plot_price_clusters(df, filename="data/clustering_price_custom.png")
    stats.plot_cluster_distribution(df, filename="data/cluster_boxplot_custom.png")

    print("\n Analyse personnalisée terminée, fichiers PNG enregistrés dans data/")

if __name__ == "__main__":
    main()
