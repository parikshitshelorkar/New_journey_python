import mysql.connector

# Connect to MySQL
dbConnection = mysql.connector.connect(
    host="localhost",
    user="parikshit",
    password="mintOs123",
    database="productsdb"
)

dbCommand = dbConnection.cursor()


# CREATE
def add_products():
    id = int(input("Enter ID: "))
    name = input("Enter Product Name: ")
    price = input("Enter Price: ")

    sql = "INSERT INTO products (ID, Name, Price) VALUES (%s, %s, %s)"
    values = (id, name, price)

    dbCommand.execute(sql, values)
    dbConnection.commit()

    print("Product added successfully")


# READ
def get_products():
    dbCommand.execute("SELECT * FROM products")
    products = dbCommand.fetchall()

    for product in products:
        print(product)


# UPDATE
def update_product():
    id = int(input("Enter ID: "))
    name = input("Enter new Name: ")
    price = input("Enter new Price: ")

    sql = "UPDATE products SET Name=%s, Price=%s WHERE ID=%s"
    values = (name, price, id)

    dbCommand.execute(sql, values)
    dbConnection.commit()

    print("Products updated successfully")


# DELETE
def delete_product():
    id = int(input("Enter ID: "))

    sql = "DELETE FROM products WHERE ID=%s"

    dbCommand.execute(sql, (id,))
    dbConnection.commit()

    print("Products deleted successfully")


# Menu
while True:

    print("\n1. Add Product")
    print("2. Show products")
    print("3. Update Product")
    print("4. Delete Product")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_products()

    elif choice == "2":
        get_products()

    elif choice == "3":
        update_product()

    elif choice == "4":
        delete_product()

    elif choice == "5":
        break

    else:
        print("Invalid choice")


dbCommand.close()
dbConnection.close()