from scraper.book import Book
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://books.toscrape.com/"

class BookScraper:
    def __init__(self):
        self.books = []

    def scrape_page(self, url: str) -> list[Book]:
        response = requests.get(url)
        response.encoding = 'utf-8'

        if response.status_code != 200:
            print(f"Erreur lors du chargement de {url} (code {response.status_code})")
            return []

        soup = BeautifulSoup(response.text, 'html.parser')
        articles = soup.select('article.product_pod')
        page_books = []

        for article in articles:
            title = article.h3.a['title']

            # Nettoyage du prix
            price_str = article.select_one('.price_color').text
            price_clean = price_str.replace('Â', '').replace('£', '').strip()
            try:
                price = float(price_clean)
            except ValueError:
                price = 0.0  # fallback si erreur

            availability = article.select_one('.availability').text.strip()
            rating = article.p.get('class')[1] if article.p and 'class' in article.p.attrs else 'Unrated'

            book = Book(title=title, price=price, availability=availability, rating=rating)
            page_books.append(book)

        return page_books

    def scrape_all(self, pages: int = 50) -> list[Book]:
        all_books = []

        for i in range(1, pages + 1):
            if i == 1:
                url = BASE_URL + "index.html"
            else:
                url = BASE_URL + f"catalogue/page-{i}.html"

            print(f"Scraping : {url}")
            books_on_page = self.scrape_page(url)

            if not books_on_page:
                print("Arrêt du scraping : plus de pages valides.")
                break

            all_books.extend(books_on_page)

        self.books = all_books
        return all_books
