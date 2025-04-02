
def encrypt(n,m):
    with open('raw_text.txt', 'r',encoding='utf-8') as rawtxt:
        msg = rawtxt.read() # it reads the message from file as string

    coded_msg = '' # where the decrypted msg will acumulate
    for item in msg:
        
        if 'a' <= item <= 'm':     # in case the item is in a-m range
            coded_msg += forward(item,n*m,ord('a'),ord('m'))               
        elif 'n' <= item <= 'z':   # in case the item is in n-z range
            coded_msg += backward(item,n+m,ord('n'),ord('z'))
        elif 'A' <= item <= 'M':   # in case the item is in A-M range
            coded_msg += backward(item,n,ord('A'),ord('M'))
        elif 'N' <= item <= 'Z':   # in case the item is in N-Z range  
            coded_msg += forward(item,m*m,ord('N'),ord('Z'))    
        else:coded_msg += item

    with open('encrypted_text.txt','w',encoding='utf-8') as encrypted:
        encrypted.write(coded_msg) # it write the message to the  file
        print('The Message is encrypted')

        print('\n----------  ORIGINAL MSG   ------------')
        print(msg)
        print('\n----------  ENCRYPTED MSG  ------------')
        print(coded_msg)


def decrypt(n,m):
    with open('encrypted_text.txt', 'r',encoding='utf-8') as rawtxt:
        msg = rawtxt.read() # it reads the message as string
    
    coded_msg = '' # where the decrypted msg will acumulate
    for item in msg:

        if 'a' <= item <= 'm':    # in case the item is in a-m range  
            coded_msg += backward(item,n*m,ord('a'),ord('m'))               
        elif 'n' <= item <= 'z':  # in case the item is in n-z range
            coded_msg += forward(item,n+m,ord('n'),ord('z'))
        elif 'A' <= item <= 'M':  # in case the item is in A-M range
            coded_msg += forward(item,n,ord('A'),ord('M'))
        elif 'N' <= item <= 'Z':  # in case the item is in N-Z range
            coded_msg += backward(item,m*m,ord('N'),ord('Z'))    
        else:coded_msg += item

    return coded_msg

def forward(item,steps, low, high):    # function that steps forward
    coded_char=''  
    if ord(item) + steps > high:   # in case steps exceeds the limit
        coded_char = chr(((ord(item)-low+steps)%13)+low)
      # cicle generated from the module, the range portion and steps
    else: coded_char = chr(ord(item)+(steps))
         # in case steps don't exceed the limit, just jump positions 
    return coded_char 

def backward(item,steps, low, high):  # function that steps backward
    coded_char=''
    if ord(item) - steps < low:    # in case steps exceeds the limit
        coded_char = chr(high-(high-(ord(item)-steps))%13)
      # cicle generated from the module, the range portion and steps
    else:coded_char = chr(ord(item)-steps) 
         # in case steps don't exceed the limit, just jump positions
    return coded_char 

def compare(n,m):
    with open('raw_text.txt', 'r',encoding='utf-8') as rawtxt:
        msg = rawtxt.read()#it reads the message from file as string

    if msg == decrypt(n,m):
        print('\n >Decrypted msg and te original msg are the same<')
    else:
        print('messages do not mach')


#------------------------  MENU  ----------------------------

def menu():
    print("\n----- Menú -----")
    print("Option 1, Encrypt the msg")
    print("Option 2, compare both msgs")
    print("Option 3, Exit")
    print("----------------")

def main():
    while True:
        menu()  
        opcion = input("Select a option from the Menu :")
                              # it will show the menu with options
        match opcion:
            case '1':
                while True:    # it validates the inputs from user
                    try:
                        n = int(input('Insert n: '))
                        m = int(input('Insert m: '))
                        break 
                    except ValueError:
                        print("Please insert integer numbers")
                encrypt(n,m)
            case '2':
                compare(n,m)
            case '3':
                break  
            case _:
                print("Invalid option please try again")

main()




    


    
