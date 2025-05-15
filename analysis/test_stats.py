from stats import load_books, describe_prices, availability_counts, summary_by_rating

def main():
    filepath = '../data/books.csv'


    df = load_books(filepath)

    # Statistiques descriptives sur les prix
    print("=== Statistiques des prix ===")
    print(describe_prices(df))

    # Comptage disponibilité par rating
    print("\n=== Disponibilité par rating ===")
    print(availability_counts(df))

    # Prix moyen par rating
    print("\n=== Prix moyen par rating ===")
    print(summary_by_rating(df))

if __name__ == "__main__":
    main()
