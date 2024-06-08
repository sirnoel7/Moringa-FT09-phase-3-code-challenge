from database.connection import get_db_connection
from models.author import Author
from models.magazine import Magazine

class Article:
    def __init__(self, id, title, author, magazine):
        self._id = id
        self.title = title
        self.author = author
        self.magazine = magazine

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str) or not (1 <= len(value) <= 50):
            raise ValueError("Title must be a string between 1 and 50 characters.")
        self._title = value

    def __repr__(self):
        return f"Article(title='{self.title}', author={self.author}, magazine={self.magazine})"
