import csv
from sqlalchemy.exc import IntegrityError

from core import db, app
from core.models import Book


def seed_data():
    with app.app_context():
        # Open the CSV file
        with open("data.csv", newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

            # Iterate over the rows in the CSV file
            for row in reader:
                # Create a new Book instance
                book = Book(
                    title=row['Book Name'],
                    author=row['Author Name']
                )

                # Add the book to the session
                db.session.add(book)

            try:
                # Commit the session to write the books to the database
                db.session.commit()
                print("Books added successfully.")
            except IntegrityError as e:
                db.session.rollback()
                print(f"Error occurred: {e}")


if __name__ == "__main__":
    seed_data()
