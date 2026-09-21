import mysql.connector

dbconnection=mysql.connector.connect(
        host="localhost",
        user="parikshit",
        password="mintOs123",
        database="productsdb"
    )
dbCommand = dbconnection.cursor()


def get_product():
    dbCommand.execute("select * from product")
    result=dbCommand.fetchall()
    for row in result:
        print(row)




def delete_product():
    id= int(input("Enter ID: "))
    sql = "DELETE FROM product WHERE ID=%s"  
    dbCommand.execute(sql, (id,))
    dbconnection.commit()
    print("product deleted successfully")


# CREATE
def add_product():
    id = int(input("Enter ID: "))
    product_name = input("Enter product_name: ")
    price = input("Enter price: ")
    sql = "INSERT INTO product (ID,product_name,price ) VALUES (%s, %s, %s)"
    values = (id, product_name, price)
    dbCommand.execute(sql, values)
    dbconnection.commit()
    print("product added successfully")


# UPDATE

def update_product():
    id = int(input("Enter ID: "))
    product_name = input("Enter new Name: ")
    price = input("Enter new price: ")

    sql = "UPDATE product SET product_Name=%s, price=%s WHERE ID=%s"
    values = (product_name, price, id)

    dbCommand.execute(sql, values)
    dbconnection.commit()

    print("product updated successfully")


# menu

print("dfsdfsd")

while True:
    print("\n1. Add product")
    print("2. Show product")
    print("3. Update product")
    print("4. Delete product")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_product()

    elif choice == "2":
        get_product()

    elif choice == "3":
        update_product()

    elif choice == "4":
        delete_product()

    elif choice == "5":
        break

    else:
        print("Invalid choice")

dbCommand.close()
dbconnection.close()