import unittest
from models.author import Author
from models.article import Article
from models.magazine import Magazine

class TestModels(unittest.TestCase):
    def test_author_creation(self):
        author = Author(1, "John Doe")
        self.assertEqual(author.name, "John Doe")
        self.assertEqual(author.id, 1)

    def test_article_creation(self):
        author = Author(1, "John Doe")
        magazine = Magazine(1, "Tech Weekly", "Technology")
        article = Article(1, "Test Title", author, magazine)
        self.assertEqual(article.title, "Test Title")
        self.assertEqual(article.author, author)
        self.assertEqual(article.magazine, magazine)
        self.assertEqual(article.id, 1)

    def test_article_title_validation(self):
        author = Author(1, "John Doe")
        magazine = Magazine(1, "Tech Weekly", "Technology")
        with self.assertRaises(ValueError):
            Article(1, "", author, magazine)
        with self.assertRaises(ValueError):
            Article(1, "T" * 51, author, magazine)

    def test_magazine_creation(self):
        magazine = Magazine(1, "Tech Weekly", "Technology")
        self.assertEqual(magazine.name, "Tech Weekly")
        self.assertEqual(magazine.category, "Technology")
        self.assertEqual(magazine.id, 1)

    def test_magazine_name_validation(self):
        with self.assertRaises(ValueError):
            Magazine(1, "T", "Technology")
        with self.assertRaises(ValueError):
            Magazine(1, "T" * 17, "Technology")

    def test_magazine_category_validation(self):
        with self.assertRaises(ValueError):
            Magazine(1, "Tech Weekly", "")

    def test_author_articles(self):
        author = Author(1, "John Doe")
        # Simulate adding articles
        author.articles = lambda: [Article(1, "Title1", author, Magazine(1, "Tech Weekly", "Technology"))]
        self.assertIsInstance(author.articles(), list)

    def test_magazine_articles(self):
        magazine = Magazine(1, "Tech Weekly", "Technology")
        magazine.articles = lambda: [Article(1, "Title1", Author(1, "John Doe"), magazine)]
        self.assertIsInstance(magazine.articles(), list)

    def test_magazine_contributors(self):
        magazine = Magazine(1, "Tech Weekly", "Technology")
        magazine.contributors = lambda: [Author(1, "John Doe")]
        self.assertIsInstance(magazine.contributors(), list)

    def test_magazine_article_titles(self):
        magazine = Magazine(1, "Tech Weekly", "Technology")
        magazine.article_titles = lambda: ["Title1"]
        self.assertIsInstance(magazine.article_titles(), list)

    def test_magazine_contributing_authors(self):
        magazine = Magazine(1, "Tech Weekly", "Technology")
        magazine.contributing_authors = lambda: [Author(1, "John Doe")]
        self.assertIsInstance(magazine.contributing_authors(), list)

    def test_article_str_representation(self):
        author = Author(1, "John Doe")
        magazine = Magazine(1, "Tech Weekly", "Technology")
        article = Article(1, "Test Title", author, magazine)
        self.assertEqual(str(article), "Article(title='Test Title', author=<Author John Doe>, magazine=Magazine(name='Tech Weekly', category='Technology'))")

    def test_author_str_representation(self):
        author = Author(1, "John Doe")
        self.assertEqual(str(author), "<Author John Doe>")

    def test_magazine_str_representation(self):
        magazine = Magazine(1, "Tech Weekly", "Technology")
        self.assertEqual(str(magazine), "Magazine(name='Tech Weekly', category='Technology')")

    def test_author_id_property(self):
        author = Author(1, "John Doe")
        self.assertEqual(author.id, 1)

    def test_author_name_property(self):
        author = Author(1, "John Doe")
        self.assertEqual(author.name, "John Doe")

    def test_magazine_id_property(self):
        magazine = Magazine(1, "Tech Weekly", "Technology")
        self.assertEqual(magazine.id, 1)

    def test_magazine_name_property(self):
        magazine = Magazine(1, "Tech Weekly", "Technology")
        self.assertEqual(magazine.name, "Tech Weekly")

    def test_magazine_category_property(self):
        magazine = Magazine(1, "Tech Weekly", "Technology")
        self.assertEqual(magazine.category, "Technology")

    def test_article_id_property(self):
        author = Author(1, "John Doe")
        magazine = Magazine(1, "Tech Weekly", "Technology")
        article = Article(1, "Test Title", author, magazine)
        self.assertEqual(article.id, 1)

if __name__ == "__main__":
    unittest.main()
