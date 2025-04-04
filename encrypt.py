import os       # Importing to check the existence of files

# Check if the file 'raw_text.txt' exists before proceeding
if not os.path.exists('raw_text.txt'):
    print("Error: 'raw_text.txt' not found.")
else:
      # If 'raw_text.txt' exists, proceed to ask for values of n and m
    def encrypt(n, m):
        with open('raw_text.txt', 'r', encoding='utf-8') as rawtxt:
           msg = rawtxt.read()       # Read the message from the file
    

        coded_msg = ''  # Variable to accumulate the encrypted message
        for item in msg:

            if 'a' <= item <= 'm':        # If the character is in the range a-m
                coded_msg += forward(item, n * m, ord('a'), ord('m'))          
            elif 'n' <= item <= 'z':      # If the character is in the range n-z
                coded_msg += backward(item, n + m, ord('n'), ord('z'))
            elif 'A' <= item <= 'M':      # If the character is in the range A-M
                coded_msg += backward(item, n, ord('A'), ord('M'))    
            elif 'N' <= item <= 'Z':      # If the character is in the range N-Z
                coded_msg += forward(item, m * m, ord('N'), ord('Z'))  
            else: 
                coded_msg += item              # Keep other characters unchanged

          # If the file 'encrypted_text.txt' does not exist, create an empty one
        if not os.path.exists('encrypted_text.txt'):
            with open('encrypted_text.txt', 'w', encoding='utf-8') as encrypted:
                pass                  # Create an empty file if it doesn't exist

                        # Now write the encrypted message to 'encrypted_text.txt'
        with open('encrypted_text.txt', 'w', encoding='utf-8') as encrypted:
            encrypted.write(coded_msg) # Write the encrypted message to the file
            print('The message is encrypted') 

            print('\n----------  ORIGINAL MESSAGE   ------------')
            print(msg) 
            print('\n----------  ENCRYPTED MESSAGE  ------------')
            print(coded_msg) 


    def decrypt(n, m):

        with open('encrypted_text.txt', 'r', encoding='utf-8') as rawtxt:
            msg = rawtxt.read()  # Read the message from the file

        coded_msg = ''                            # Variable to accumulate the decrypted message
        for item in msg:
            if 'a' <= item <= 'm':                        # If the character is in the range a-m
                coded_msg += backward(item, n * m, ord('a'), ord('m'))  # Backward shift for a-m                
            elif 'n' <= item <= 'z':                      # If the character is in the range n-z
                coded_msg += forward(item, n + m, ord('n'), ord('z'))    # Forward shift for n-z
            elif 'A' <= item <= 'M':                      # If the character is in the range A-M
                coded_msg += forward(item, n, ord('A'), ord('M'))        # Forward shift for A-M
            elif 'N' <= item <= 'Z':                      # If the character is in the range N-Z
                coded_msg += backward(item, m * m, ord('N'), ord('Z'))  # Backward shift for N-Z
            else: 
                coded_msg += item  # Keep other characters unchanged

        return coded_msg              # Return the decrypted message


    def forward(item, steps, low_limit, high_limit):                # Function to move forward
        coded_char = ''  
        if ord(item) + steps > high_limit:              # If the shift exceeds the upper limit
            coded_char = chr(((ord(item) - low_limit + steps) % 13) + low_limit)  # Calculate with mod 13 cycle
        else: 
            coded_char = chr(ord(item) + steps)   # If it doesn't exceed, simply shift forward
        return coded_char


    def backward(item, steps, low_limit, high_limit):              # Function to move backward
        coded_char = ''
        if ord(item) - steps < low_limit:               # If the shift exceeds the lower limit
            coded_char = chr(high_limit - (high_limit - (ord(item) - steps)) % 13)  # Calculate with mod 13 cycle
            coded_char = chr(high_limit - (high_limit - (ord(item) - steps))%13)
        else: 
            coded_char = chr(ord(item) - steps)  # If it doesn't exceed, simply shift backward
        return coded_char


    def compare(n, m):

        with open('raw_text.txt', 'r', encoding='utf-8') as rawtxt:
            msg = rawtxt.read()  # Read the message from the file

        if msg == decrypt(n, m):  # Compare the original message with the decrypted message
            print('\n >Encrypted message and the original message are the same<')
        else: 
            print('Messages do not match')              # If they don't match, show message


    # Main loop to ask for n and m from the user
while True:
    try:
        n = int(input('Insert n: '))  # Ask for value of n
        m = int(input('Insert m: '))  # Ask for value of m

        # Validate that the numbers are not negative
        if n < 0 or m < 0:
            print("Numbers cannot be negative. Please try again.")
            continue  # If negative, prompt for input again

        encrypt(n, m)       # Call the encryption function
        compare(n, m)       # Call the comparison function
        break  # Exit the loop if everything is correct

    except ValueError:  # Handle the case where input is not an integer
        print("Please insert integer numbers.")
