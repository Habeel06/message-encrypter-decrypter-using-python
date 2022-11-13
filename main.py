from cryptography.fernet import Fernet
from termcolor import colored
import colorama 
colorama.init()
print(colored('''
\n
\n
  ________                                                     __                         
|        \                                                   |  \                        
| $$$$$$$$ _______    _______   ______   __    __   ______  _| $$_     ______    ______  
| $$__    |       \  /       \ /      \ |  \  |  \ /      \|   $$ \   /      \  /      \ 
| $$  \   | $$$$$$$\|  $$$$$$$|  $$$$$$\| $$  | $$|  $$$$$$\\$$$$$$  |  $$$$$$\|  $$$$$$\
| $$$$$   | $$  | $$| $$      | $$   \$$| $$  | $$| $$  | $$ | $$ __ | $$    $$| $$   \$$
| $$_____ | $$  | $$| $$_____ | $$      | $$__/ $$| $$__/ $$ | $$|  \| $$$$$$$$| $$      
| $$     \| $$  | $$ \$$     \| $$       \$$    $$| $$    $$  \$$  $$ \$$     \| $$      
 \$$$$$$$$ \$$   \$$  \$$$$$$$ \$$       _\$$$$$$$| $$$$$$$    \$$$$   \$$$$$$$ \$$      
                                        |  \__| $$| $$                                   
                                         \$$    $$| $$                                   
                                          \$$$$$$  \$$                                     ''','green'))

print(colored("Report a bug at:https://github.com/Habeel06/msg-encrypter-decrypter-python ",'yellow'))
while True:


        x=input("Type encode to encode and decode to decode :")

        if "encode" in x:

                        data = input("Type in the message you want to encrypt : ")
                        data = bytes(data,'utf-8')    
                    
                        key = Fernet.generate_key()
                        f = Fernet(key)
                        estr=f.encrypt(data)
                        print("Your Encrypted message is : " +str(estr))
                        print("Key to decode the message :" + str(key))

        elif "decode" in x:
                        try:
                                dstr=input("Enter the message you want to decode (make sure that you exclude b) :")
                                dk=input("Enter Key (make sure that you exclude b) :")
                                y=Fernet.generate_key()
                                a=str(dstr)
                                y=(dk)
                                x=Fernet(y)
                                decodedmsg = x.decrypt(a).decode()
                                print("The decoded message is : " + str(decodedmsg))
                        except ValueError:
                                print('''Oops! Wrong encrypted message or wrong key given.
TRY AGAIN!''')


        
