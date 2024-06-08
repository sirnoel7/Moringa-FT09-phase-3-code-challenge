from database.connection import get_db_connection

class Author:
    def __init__(self, id, name):
        self._id = id
        self.name = name

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Name must be a non-empty string.")
        self._name = value

    def articles(self):
        from models.article import Article
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM articles WHERE author_id = ?', (self.id,))
        rows = cursor.fetchall()
        conn.close()
        return [Article(row['id'], row['title']) for row in rows]

    def magazines(self):
        from models.magazine import Magazine 
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT DISTINCT magazines.* FROM magazines
            JOIN articles ON articles.magazine_id = magazines.id
            WHERE articles.author_id = ?
        ''', (self.id,))
        rows = cursor.fetchall()
        conn.close()
        return [Magazine(row['id'], row['name'], row['category']) for row in rows]

    def __repr__(self):
        return f'<Author {self.name}>'
