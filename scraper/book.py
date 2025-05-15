
class Book:
    def __init__(self, title: str, price: float, availability: str, rating: str):
        self.title = title
        self.price = price
        self.availability = availability
        self.rating = rating

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "price": self.price,
            "availability": self.availability,
            "rating": self.rating
        }

    def __repr__(self):
        return f"Book(title={self.title!r}, price={self.price}, availability={self.availability!r}, rating={self.rating!r})"
