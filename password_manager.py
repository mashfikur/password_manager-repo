from cryptography.fernet import Fernet

user_masterpass=input("what is the master pass? ")

'''def write_key():
    key=Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)'''




mode=input("Do you want to see your pass or add a new one? (view/add), To quit the programme press q: ").lower()

def view():
    with open("passwords.txt","r") as y:
        for x in y.readlines():
            data=x.strip()
            user,password=data.split("-")
        print("The username:",user)
        print("The password:",password)
            

def add():
    name=input("Account name :")
    password=input("Enter your password :")

    with open("passwords.txt","a") as x:
        x.write(name+"-"+password+"\n")
    


while True:
    if mode=="q":
        break

    if mode=="view":
        view()
        break
    elif mode=="add":
        add()
        break 
        
    else:
        print("invalid value")
        break