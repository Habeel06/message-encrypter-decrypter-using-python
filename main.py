from cryptography.fernet import Fernet
while True:
    x=input("Enter 1 to encode and 2 to decode :")
    if x==1:

        ystr=input("Enter the message you want to encrypt:")
        key = Fernet.generate_key()
        f = Fernet(key)
        estr=f.encrypt(b"ystr")
        print("Your Encrypted message is : " + str(estr))
        print("Key to decode the message :" + str(key))
    if x==2:
        dstr=input("Enter the message you want to decode:")
        dk=input("Enter Key:")

        a=str(dstr)
        y=(dk)
        x=Fernet(y)
        decodedmsg = x.decrypt(a).decode()
        print("The decoded message is : " + str(decodedmsg))

    else:
        print("Try again")

