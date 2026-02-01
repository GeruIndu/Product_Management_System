from sqlalchemy.orm import sessionmaker
from sqlalchemy import select, update
from connect import engine
from models import Product, Category
from sqlalchemy.exc import SQLAlchemyError

Session = sessionmaker(bind=engine)

def fetch_all_products():
    with Session() as session:
        products = session.scalars(select(Product)).all()
        print("\n--- Products ---")
        for p in products:
            print(f"{p.name} |Price: {p.price}  |Description: {p.description}")
        return products


def bulk_price_update(category_name: str):
    session = Session()
    try:
        with session.begin():
            category = session.scalar(
                select(Category).where(Category.name == category_name)
            )

            if not category:
                raise ValueError(f"Category {category} not found")

            statement = (
                update(Product)
                .where(Product.category_id == category.id)
                .values(price=Product.price * 1.10)
            )

            session.execute(statement)

        print("Bulk price update successful")

    except (SQLAlchemyError, ValueError) as e:
        session.rollback()
        print("Transaction failed:", e)

    finally:
        session.close()

def fetch_all_categories():
    with Session() as session:
        categories = session.query(Category).all()
        print("\nAvailable Categories:")
        for idx, c in enumerate(categories, 1):
            print(f"{idx}. {c.name}")
        return categories


if __name__ == "__main__":
    print("All products available")
    fetch_all_products()

    categories = fetch_all_categories()

    while True:
        try:
            option = int(input("\nEnter the category index that you want to update : "))
            if 1 <= option <= len(categories):
                selected_category = categories[option - 1].name
                break
            else:
                print("Invalid number, try again.")
        except ValueError:
            print("Please enter a valid integer.")

    bulk_price_update(selected_category)

    print("\nAll products after update:")
    fetch_all_products()