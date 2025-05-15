
import csv
from scraper.book import Book

def export_books_to_csv(books: list[Book], filepath: str):
    if not books:
        print("Aucun livre à exporter.")
        return

    with open(filepath, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["title", "price", "availability", "rating"])
        writer.writeheader()
        for book in books:
            writer.writerow(book.to_dict())

    print(f"✅ Export terminé : {len(books)} livres enregistrés dans {filepath}")
