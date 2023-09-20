import qrcode

PRODUCTS = []
BASKET=[]

def read_from_database():
    f=open("database.txt","r")

    for line in f:

        result= line.rstrip("\n").split(",")
        my_dict = {"code":result[0],"name":result[1],"price":int(result[2]),"count":int(result[3])}

        PRODUCTS.append(my_dict)
        # print(PRODUCTS)

    f.close()
    
def write_to_database():
    f=open("database.txt","w")
    for product in PRODUCTS:
        f.write(product['code']+",")
        f.write(product['name']+",")
        f.write(str(product['price'])+",")
        f.write(str(product['count'])+"\n")
    f.close()

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
    code=input("enter code: ")
    for product in PRODUCTS:
        if code==product['code']:
            print("The code is duplicated, please enter another code")
            break
    else:
        name=input("enter name: ")
        price=int(input("enter price: "))
        count=int(input("enter count: "))
        new_product={'code':code,'name':name,'price':price,'count':count}
        PRODUCTS.append(new_product)

def edit():
    code=input("enter code: ")
    for product in PRODUCTS:
        if code==product['code']:
            print("code=",product["code"],", name=",product["name"],", price=",product["price"],", count=",product["count"])
            name=input("enter new name to edit or press the 'enter' key to escape: ")
            if name!='':
                product['name']=name

            price=input("enter new price to edit or press the 'enter' key to escape: ")
            if price!='':
                product['price']=int(price)

            count=input("enter new count to edit or press the 'enter' key to escape: ")
            if count!='':
                product['count']=int(count)
            
            print("This product updated successfully")
            break

    else:
        print("This code is not exist, please try again")

def remove():
    code=input("enter code to remove it: ")
    for product in PRODUCTS:
        if product['code']==code:
            PRODUCTS.remove(product)
            print("This code successfully removed")
            break
    else:
        print("This code is not exist, please try again")
    # PRODUCTS[:]=[product for product in PRODUCTS if product.get('code')!=code]

def search():
    user_input=input("type your keyword: ")
    for product in PRODUCTS:
        if product["code"]==user_input or product['name']==user_input:
            print(product["code"],"\t", product["name"],"\t","\t",product["price"])
            break
    else:
        print("not found")

def show_list():
    print("code\tname\t\tprice")
    for product in PRODUCTS:
        print(product["code"],"\t", product["name"],"\t","\t",product["price"])

def buy():
    while True:
        product_code=input("enter product code or press the 'enter' key to scape: ")
        if product_code=='':
            break

        for product in PRODUCTS:
            if product["code"]==product_code:
                number_of_product=int(input("please enter number of products requested: "))
                if number_of_product <= product["count"]:
                    basket_item={"code":product["code"],"name":product["name"],"price":product["price"],"count":number_of_product}
                    BASKET.append(basket_item)
                    # print(BASKET)
                    product["count"] -= number_of_product
                else:
                    print("There is not enough product stock.")
                break

        else:
            print("This code is not exist, please try again")

    # bill
    total=0
    print("name\tprice\tcount")
    for item in BASKET:
        print(item["name"],"\t", item["price"], "\t", item["count"])
        total += item["price"]*item["count"]
    print("Total:",total)

def make_qrcode():
    code=input("enter code to generate qrcode: ")
    for product in PRODUCTS:
        if product["code"]==code:
            qr_img=qrcode.make("code: " + product["code"] + "\n" + "name: " + product["name"] + "\n" + "price: " + str(product["price"]))
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
        write_to_database()
        exit(0)
    else:
        print("wrong choice, please try again")
        