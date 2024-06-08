from database.connection import get_db_connection 
from models.author import Author
from models.magazine import Magazine

class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str) or not (5 <= len(value) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters.")
        self._title = value

    def author(self):
        from models.author import Author
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT authors.* FROM authors JOIN articles ON articles.author_id = authors.id WHERE articles.id = ?', (self.id,))
        row = cursor.fetchone()
        conn.close()
        return Author(row['id'], row['name'])

    def magazine(self):
        from models.magazine import Magazine
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT magazines.* FROM magazines JOIN articles ON articles.magazine_id = magazines.id WHERE articles.id = ?', (self.id,))
        row = cursor.fetchone()
        conn.close()
        return Magazine(row['id'], row['name'], row['category'])

    def __repr__(self):
        return f"Article(title='{self.title}', author={self.author}, magazine={self.magazine})"
