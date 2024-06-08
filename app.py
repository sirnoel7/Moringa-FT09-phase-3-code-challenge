from database.setup import create_tables
from database.connection import get_db_connection
from models.author import Author
from models.article import Article
from models.magazine import Magazine

def main():
    create_tables()

    author_name = input("Enter author's name: ")
    magazine_name = input("Enter magazine name: ")
   
