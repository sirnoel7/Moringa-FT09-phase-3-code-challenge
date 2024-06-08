from database.setup import create_tables
from database.connection import get_db_connection
from models.article import Article
from models.author import Author
from models.magazine import Magazine

def main():
    # Initialize the database and create tables
    create_tables()

    # Collect user input
    author_name = input("Enter author's name: ")
    magazine_name = input("Enter magazine name: ")
    magazine_category = input("Enter magazine category: ")
    article_title = input("Enter article title: ")

    # Connect to the database
    conn = get_db_connection()
    cursor = conn.cursor()

    # Create an author
    cursor.execute('INSERT INTO authors (name) VALUES (?)', (author_name,))
    author_id = cursor.lastrowid

    # Create a magazine
    cursor.execute('INSERT INTO magazines (name, category) VALUES (?, ?)', (magazine_name, magazine_category))
    magazine_id = cursor.lastrowid

    # Create an article with placeholder content
    cursor.execute('INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)',
                   (article_title, "Placeholder content", author_id, magazine_id))
    article_id = cursor.lastrowid

    conn.commit()

    # Fetch the article from the database
    cursor.execute('SELECT * FROM articles WHERE id = ?', (article_id,))
    article_data = cursor.fetchone()

    # Create the Article object
    article = Article(article_data["id"], article_data["title"], Author(author_id, author_name), Magazine(magazine_id, magazine_name, magazine_category))

    conn.close()

    # Display the article
    print("\nArticle:")
    print(article)

if __name__ == "__main__":
    main()
