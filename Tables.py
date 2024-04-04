import mysql. connector as a
#In the password sector in the connect function place your database's password and it leave empty in case you didn't set one
con=a.connect (host=" localhost", user=" root", password="mysql", database="stock")
#Returns 'True' if there is a connection
print(con.is_connected())
c=con.cursor()

def add_item():
 bn=input("enter the item name : ")
 f=input("enter item code:")
 c=int(input( "enter the item quantity: "))
 data=(bn,f,c)
 sql='insert into product values(%s,%s,%s)'
 c=con. cursor()
 c. execute( sql,data)
 con.commit()
 print (" =============")
 print("ITEM ADDED SUCCESSFULLY")
 anykey=input("Press and Enter anykey to return to menu:")

def delete_item():
 f=input("enter item code:")
 data=(f,)
 sql="delete from product where PRCODE=%s"
 c=con. cursor()
 c. execute( sql,data)
 con.commit()
 print (" =============")
 print("ITEM DELETED SUCCESSFULLY")
 anykey=input("Press and Enter anykey to return to menu:")

def update_item():
 ac=input("enter  item code:")
 bc=input("enter item name:")
 c=input("enter item quantity:")
 a="UPDATE product SET PRNAME=%s,QUANTITY=%s WHERE PRCODE=%s"
 data=(bc,c,ac)
 c=con. cursor()
 c.execute(a,data)
 con.commit()
 print("ITEM UPDATED SUCCESSFULLY")
 anykey=input("Press and Enter anykey to return to menu:")

def add_staff():
 bn=input("enter staff name : ")
 f=input("enter regno:")
 c=int(input( "enter staff phone number: "))
 data=(bn,f,c)
 sql='insert into staff values(%s,%s,%s)'
 c=con. cursor()
 c. execute( sql,data)
 con.commit()
 print (" =============")
 print("STAFF ADDED SUCCESSFULLY")
 anykey=input("Press and Enter anykey to return to menu:")

def delete_staff():
 f=input("enter regno:")
 data=(f,)
 sql="delete from staff where REGNO=%s"
 c=con. cursor()
 c. execute( sql,data)
 con.commit()
 print (" =============")
 print("STAFF DELETED SUCCESSFULLY")
 anykey=input("Press and Enter anykey to return to menu:")

def update_staff():
 ac=input("enter  staff code:")
 bc=input("enter staff name:")
 c=input("enter staff phone number:")
 a="UPDATE staff SET NAME=%s,PHONE_NO=%s WHERE REGNO=%s"
 data=(bc,c,ac)
 c=con. cursor()
 c.execute(a,data)
 con.commit()
 print("STAFF UPDATED SUCCESSFULLY")
 anykey=input("Press and Enter anykey to return to menu:")


#MAIN MENU FUNCT
def Print_menu():
    print(">---------------<")
    print("1. Add item")
    print("2. Delete item")
    print("3. Update item ")
    print("4. Add staff")
    print("5. Delete staff")
    print("6. Update staff ")
    
while True:
    Print_menu()
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_item()
    elif choice == 2:
        delete_item()
    elif choice == 3:
        update_item()
    elif choice == 4:
        add_staff()
    elif choice == 5:
        delete_staff()
    elif choice == 6:
        update_staff()
    else:
        print("Invalid choice.Enter 1-6...")


    

