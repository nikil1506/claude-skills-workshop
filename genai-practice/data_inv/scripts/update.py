import sqlite3
from contextlib import closing

user_data={
    "id": 1,
    "product": "Water Bottle",
    "size_liters": 0.5,
    "quantity": 100,
    "price": 9.99
}

user_search_keywords="Milk"

def init_db(connection):
    cursor = connection.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS inventory ("
        "id INTEGER PRIMARY KEY, product TEXT, size_liters FLOAT,quantity INTEGER, price REAL)"
    )
    connection.commit()

def add_product(connection):
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO inventory (id, product, size_liters, quantity, price) VALUES (?, ?, ?, ?, ?)"
    , (user_data["id"], user_data["product"], user_data["size_liters"], user_data["quantity"], user_data["price"]))
   
    connection.commit()

def delete_product(connection, product_id):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM inventory WHERE id = ?", (product_id,))
    connection.commit()

def display_products(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM inventory")
    print(cursor.fetchall())

def main():
    with closing(sqlite3.connect("inv.db")) as connection:
        init_db(connection)
        add_product(connection)
        display_products
        (connection)

if __name__ == "__main__":
    main()