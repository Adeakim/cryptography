from art import art



def cryptography():
  print(art)
  #ENCRYPTING PROCESS
def encrypt(inp,key):
            encstr=""
            for i in inp:
                if ord(i)>=97 and ord(i)<=122:
                    temp=(ord(i)+key)
                    if temp > 122:
                        temp=temp%122 +97 
                    encstr= encstr + chr(temp)
                else: 
                    encstr=encstr + chr(ord(i))
            return (encstr)

#DECRYPTING PROCESS
def decrypt(inp,key):
        decstr=""
        for i in inp:
            if ord(i)>=97 and ord(i)<=122:
                temp=(ord(i)-key)
                if temp < 97:
                    temp = temp+26 # counting again from the back(z-a)
                decstr= decstr + chr(temp)
            else: 
                decstr=decstr + chr(ord(i))
        return (decstr)
    #USER REQUEST    
def cryptography():    
    userRequest= input("type 'encode' to encrypt or 'decode' to decrypt: \n")
    while not userRequest:
        userRequest= input("Invalid request.type 'encode' to encrypt or 'decode' to decrypt: \n")
        if userRequest !="encode" or userRequest != "decode":
            userRequest= input("Invalid request.type 'encode' to encrypt or 'decode' to decrypt: \n")
   
    if userRequest=='encode':    
            
            inp=input("Type what you want to encrypt: \n")
        
            while not inp:
                inp=input("Invalid message.Type what you want to encrypt again: \n")
            
            try:
                key=(input("Type your encryption key: \n"))
                while key.isdigit()==False:
                    key=int (input('Invalid key.Key can only be empty of integer:'))
            except ValueError:
                key=0
            result=encrypt(inp,int(key))
            print(f'Your encryption code is {result}')
    
    elif userRequest=='decode':
       
        
        inp=input("Type what you want to decrypt: \n")
        while not inp:
            inp=input("Invalid message.Type what you want to decrypt: \n")
        try:
            key = input("Type your decryption key: \n")
            while key.isdigit()==False:
                key=input('Invalid key. Type a valid decryption key: ')
        except ValueError: 
            key=0
        result=decrypt(inp,int(key))
        print (f'Your encryption code is {result}')

cryptography()

while True:
    reusable= input ("Type 'Yes' if you want to continue, otherwise type 'No' : \n")
    if reusable.lower() == "yes":
        cryptography()
    elif reusable.lower()=='no':
        
        break
print("Thank you for using our service")

