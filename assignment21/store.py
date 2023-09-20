import qrcode
import sqlite3

BASKET=[]

def read_from_database():
    global connection,my_cursor,products_list
    connection=sqlite3.connect("store.db")
    my_cursor=connection.cursor()
    products_list=my_cursor.execute("SELECT * FROM products").fetchall()

def show_menu():
    print("0- Make QRcode")
    print("1- Add")
    print("2- Edit")
    print("3- Remove")
    print("4- Search")
    print("5- Show List")
    print("6- Buy")
    print("7- Exit")

def add():
    name=input("enter name: ")
    price=int(input("enter price: "))
    count=int(input("enter count: "))
    my_cursor.execute(f"INSERT INTO products(name, price, count) VALUES('{name}','{price}','{count}')")
    connection.commit()
    print("This product inserted successfully")

def edit():
    code=int(input("enter code: "))
    for product in products_list:
        if code==product[0]:
            print("code=",product[0],", name=",product[1],", price=",product[2],", count=",product[3])
            name=input("enter new name to edit or press the 'enter' key to escape: ")
            if name!='':
                my_cursor.execute(f"UPDATE products SET name='{name}' WHERE code='{code}'")

            price=input("enter new price to edit or press the 'enter' key to escape: ")
            if price!='':
                my_cursor.execute(f"UPDATE products SET price='{price}' WHERE code='{code}'")

            count=input("enter new count to edit or press the 'enter' key to escape: ")
            if count!='':
                my_cursor.execute(f"UPDATE products SET count='{count}' WHERE code='{code}'")

            connection.commit()
            
            print("This product updated successfully")
            break

    else:
        print("This code is not exist, please try again")

def remove():
    code=int(input("enter code to remove it: "))
    for product in products_list:
        if code==product[0]:
            my_cursor.execute(f"DELETE FROM products WHERE code='{code}'")
            connection.commit()
            print("This code successfully removed")
            break
    else:
        print("This code is not exist, please try again")

def search():
    user_input=input("enter product's code or name: ")
    result=my_cursor.execute(f"SELECT * FROM products WHERE code LIKE '%{user_input}%' OR name LIKE '%{user_input}%'").fetchall()
    if result==[]:
        print("Not found")
    for product in result:
        print(product[0],"\t", product[1],"\t","\t",product[2])

def show_list():
    print("(code, name, price)")
    for product in products_list:
        print(product[0:3])

def buy():
    while True:
        product_code=input("enter product code or press the 'enter' key to scape: ")
        if product_code=='':
            break

        for product in products_list:
            if product[0]==int(product_code):
                number_of_product=int(input("please enter number of products requested: "))
                if number_of_product <= product[3]:
                    product_name=product[1]
                    product_price=product[2]
                    product_count=number_of_product
                    basket_item=(product_code,product_name,product_price,product_count)
                    BASKET.append(basket_item)
                    my_cursor.execute(f"UPDATE products SET count='{product[3]-number_of_product}' WHERE code='{product_code}'")
                    connection.commit()
                    # print(BASKET)
                else:
                    print("There is not enough product stock.")
                break

        else:
            print("This code is not exist, please try again")

    # bill
    total=0
    print("name\tprice\tcount")
    for item in BASKET:
        print(item[1],"\t", item[2], "\t", item[3])
        total += item[2]*item[3]
    print("Total:",total)

def make_qrcode():
    code=int(input("enter code to generate qrcode: "))
    for product in products_list:
        if product[0]==code:
            qr_img=qrcode.make("code: " + str(product[0]) + "\n" + "name: " + product[1] + "\n" + "price: " + str(product[2]))
            qr_img.save("product_qrcode.jpg")
            break
    else:
        print("This code is not exist, please try again")

    
# ------------------------- #
print("Welcome to my store")
print("Loading...")
read_from_database()
print("Data loaded")

while True:
    show_menu()
    choice= int(input("enter your choice: "))

    if choice==0:
        make_qrcode()
    elif choice==1:
        add()
    elif choice==2:
        edit()
    elif choice==3:
        remove()
    elif choice==4:
        search()
    elif choice==5:
        show_list()
    elif choice==6:
        buy()
    elif choice==7:
        exit(0)
    else:
        print("Wrong choice, please try again")
        