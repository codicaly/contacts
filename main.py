import mysql.connector as my

#connections
mydb = my.connect(host="localhost",user="root",password="aswin")
mycursor = mydb.cursor()
mycursor.execute("create database if not exists mycontacts")
mycursor.execute("use mycontacts")
mycursor.execute("create table if not exists password (val varchar(25))")
mycursor.execute("create table if not exists contacts (Name varchar(25), countryCode varchar(5), number varchar(13))")

def viewAllContacts() :
    print("--------- Contacts ---------")
    mycursor.execute("select * from contacts")
    t = tuple(mycursor)
    for i in t:
        print("\nName :",i[0],"\nNumber :",i[1],i[2])
    print("\n")  
    contactsInterface()      

def deleteContact() :
    print("\nEnter 1 to delete contact by entering name.\nEnter 2 to delete ny entering number.\nEnter 0 to exit.")
    userInput = int(input("Enter : "))
    if userInput == 1 :
        name = input("Enter full name : ")
        sql = "select * from contacts where name = %s"
        val = (name,)
        mycursor.execute(sql,val)
        t = tuple(mycursor)
        if len(t) == 0 :
            print("Sorry. You didn't saved any contacts with name",name,". Kindly enter again...")
            deleteContact()
        else :
            sql = "delete from contacts where name = %s"
            val = (name,)
            mycursor.execute(sql,val)
            mydb.commit()
            print("\nSuccessfully deleted the contact....\n")
            contactsInterface()

    elif userInput == 2 :
        number = input("Enter number : ")
        sql = "select * from contacts where number = %s"
        val = (number,)
        mycursor.execute(sql,val)
        t = tuple(mycursor)
        if len(t) == 0:
            print("Sorry. You didn't saved any contacts with number",number,". Kindly enter again...")
            deleteContact()
        else :
            sql = " delete from contacts where number = %s"
            val = (number,)
            mycursor.execute(sql,val)
            mydb.commit()
            print("\nSuccessfully deleted the contact....\n")
            contactsInterface()
    
    elif userInput == 0 :
        print("Exiting Delete Contacts...\n")
        contactsInterface()
    
    else :
        print("Invalid Input...Kindly Enter again...\n")
        deleteContact()

def modifyContact():
    print("\nEnter 1 to modify name.\nEnter 2 to modify number.\nEnter 0 to exit.")
    userInput = int(input("Enter : "))
    if userInput == 1 :
        oldName = input("Enter old name : ")
        sql = "select * from contacts where name = %s"
        val = (oldName,)
        mycursor.execute(sql,val)
        t = tuple(mycursor)
        if len(t) == 0 :
            print("Sorry. You didn't saved any contacts with name",oldName,". Kindly enter again...")
            modifyContact()
        else :
            newName = input("Enter new Name : ")
            sql = "update contacts set name = %s where name = %s"
            val = (newName,oldName)
            mycursor.execute(sql,val)
            mydb.commit()
            print("\nSuccessfully updated the name...\n")
            contactsInterface()
    
    elif userInput == 2 :
        oldNumber = input("Enter old number : ")
        sql = "select * from contacts where number = %s"
        val = (oldNumber,)
        mycursor.execute(sql,val)
        t = tuple(mycursor)
        if len(t) == 0 :
            print("Sorry. You didn't saved any contacts with number",oldNumber,". Kindly enter again....")
            modifyContact()
        
        else :
            newNumber = input("Enter new number : ")
            sql = "update contacts set number = %s where number = %s"
            val = (newNumber,oldNumber)
            mycursor.execute(sql,val)
            mydb.commit()
            print("\nSuccessfully updated the number...\n")
            contactsInterface()
    
    elif userInput == 0 :
        print("Exiting update contacts\n")
        contactsInterface()
    
    else :
        print("Invalid input. Kindly enter again...")
        modifyContact()

def searchContact() :
    print("\nEnter 1 to search by Name.\nEnter 2 to search ny Number.\nEnter 3 to exit.")
    userInput = int(input("\nEnter : "))
    if userInput == 1 :
        name = input("Enter full name : ")
        sql = "select * from contacts where name = %s"
        val = (name,)
        mycursor.execute(sql,val)
        t = tuple(mycursor)
        if len(t) == 0:
            print("You have no contact saved with the name",name,'\n')
            searchContact()
        else :
            for i in t :
                print("\nName : ",i[0],"\nPhone Number : ",i[1],i[2],'\n')
                contactsInterface() 

    elif userInput == 2 :
        number = input("Enter full number : ")
        sql = "select * from contacts where number = %s"
        val = (number,)
        mycursor.execute(sql,val)
        a = tuple(mycursor)
        if  len(a) == 0 :
            print("You have no contact saved with the number",number,'\n')
            searchContact()
        else :
            for i in a :
                print("\nName : ",i[0],"\nPhone Number : ",i[1],i[2],'\n')
                contactsInterface()
    
    elif userInput == 0 :
        print("Exiting Search Contacts...\n")
        contactsInterface()
    
    else :
        print("!!! Invalid Input.Kindly enter again !!!")
        searchContact()

def storeContact(name,countryCode,number):
    sql = "INSERT INTO contacts Values (%s,%s,%s)"
    val = (name,countryCode,number)
    mycursor.execute(sql,val)
    mydb.commit()

def isNumberIn(number):
    mycursor.execute("select number from contacts")
    for i in mycursor:
        if i[0] == number :
            print("!!!This number is already stored.Enter again!!!")
            createContact()

def isNameIn(name): #used to find whether the name is already stored
    mycursor.execute("select Name from contacts")
    for i in mycursor:
        if i[0] == name :
            print("!!!This name is already stored. Enter a different name!!!")
            createContact()

def createContact() :
    name = input("Enter full name : ")
    isNameIn(name)
    countryCode = input("Enter country code : ")
    number = input("Enter full number :")
    isNumberIn(number)
    storeContact(name,countryCode,number)
    print("Your contact is sucessfully saved....\n")
    contactsInterface()

def contactsInterface():
    print("Enter 1 to create new contact.\nEnter 2 to search contacts.\nEnter 3 to modify a contact.\nEnter 4 to delete a contact.\nEnter 5 to view all the contacts.\nEnter 0 to exit.\n")
    userInput = int(input("Enter your choice : "))
    if userInput == 1:
        createContact()
    elif userInput == 2 :
        searchContact()
    elif userInput == 3 :
        modifyContact()
    elif userInput == 4 :
        deleteContact()
    elif userInput == 5 : 
        viewAllContacts()
    elif userInput == 0 :
        print("Exiting Contacts... Bye Bye... Have a nice day...")
    else :
        print("Invalid Input... Kindly Enter again... \n")
        contactsInterface()    

def login(password):
    mycursor.execute("select * from password")
    for i in mycursor:
        if i[0] == password:
            return "login"
        else :
            print("You have entered wrong password. Enter again.\n")
            main()

def countr(): #counts the number of records in password table
    mycursor.execute("select count(*) from password")
    for i in mycursor:
        return int(i[0])

def createPassword(password):
    sql = "INSERT INTO password VALUES (%s)"
    val = (password,)
    mycursor.execute(sql,val)
    mydb.commit()

def passwordValidity(password):
    l, u,  d = 0, 0, 0
    if (len(password) >= 6):
        for i in password:
            if (i.islower()):
                l += 1
            if (i.isupper()):
                u += 1
            if (i.isdigit()):
                d += 1
    if (l>=1 and u>=1 and d>=1 and len(password) >= 6):
        return "valid"
    else :
        print("Your password is weak. Note : Your password should atleast contain on upper case letter, one lower case letter, one digit and the length should be alteast 6 characters.\n")
        return "invalid"
    
def main():
    no_rec = countr()
    if no_rec == 0 : #new user with no password created
        print("\nYou have to create password for future use. Kindly enter password of atleast 6 characters !!!")
        pswd = input("Enter a password : ")
        print("\n")
        s = passwordValidity(pswd)
        if (s == "valid"):
            createPassword(pswd)
            contactsInterface()
        else :
            main()
    else: #user already created password and need to login
        print("\nYou have already created password. Enter the password to access contacts.")
        pswd = input("Enter password : ")
        l = login(pswd)
        if l == "login": 
            print("Successfully Logged in.\n")
            contactsInterface()
main()