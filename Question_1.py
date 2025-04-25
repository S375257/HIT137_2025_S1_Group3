import os

def encrypt_char(char, n, m):
    # Encrypt a single character based on its type and rules
    if char.islower():
        shift = n * m
        return chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
    elif char.isupper():
        shift = m ** 2
        return chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
    return char  # Non-alphabetic characters unchanged

def decrypt_char(char, n, m):
    # Decrypt a single character by reversing the encryption rules
    if char.islower():
        shift = n * m
        return chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
    elif char.isupper():
        shift = m ** 2
        return chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
    return char

def encrypt_text(text, n, m):
    # Encrypt an entire string using the defined rules
    return ''.join(encrypt_char(c, n, m) for c in text)

def decrypt_text(text, n, m):
    # Decrypt an entire string using the inverse of the encryption rules
    return ''.join(decrypt_char(c, n, m) for c in text)

def main():
    # Main function to perform file reading, encryption, decryption, and file writing
    folder_path = input("Enter the folder where 'raw_text.txt' is located (e.g., C:/Users/John/Desktop/Working Files): ").strip()
    input_file = os.path.join(folder_path, "raw_text.txt")
    encrypted_file = "encrypted_text.txt"
    decrypted_file = "decrypted_text.txt"

    # Get user inputs for encryption
    print("Encryption requires two numbers.")

    while True:
        try:
            n = int(input("Enter a whole positive number for n: "))
            m = int(input("Enter a whole positive number for m: "))
            if n > 0 and m > 0:
                break  # Exit loop if values are valid
            else:
                print("Both numbers must be greater than zero. Please try again.")
        except ValueError:
            print("Invalid input. Please enter whole numbers only.")

    # Check if raw_text file exists
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found. Please make sure it exists in the same directory.")
        return

    try:
        print("Starting encryption process...")

        with open(input_file, "r") as infile:
            raw_text = infile.read()

        # Encrypt and save
        encrypted = encrypt_text(raw_text, n, m)
        with open(encrypted_file, "w") as ef:
            ef.write(encrypted)

        # Decrypt and save
        decrypted = decrypt_text(encrypted, n, m)
        with open(decrypted_file, "w") as df:
            df.write(decrypted)

        # Output results
        print("Encryption and decryption completed.")
        print(f"Encrypted file saved to: {os.path.abspath(encrypted_file)}")
        print(f"Decrypted file saved to: {os.path.abspath(decrypted_file)}")

        if decrypted == raw_text:
            print("Decryption successful. Output matches the original.")
        else:
            print("Decryption failed. Output does not match the original.")

    except Exception as e:
        print(f"Unexpected error occurred: {type(e).__name__} - {e}")

        # Pause before closing
    input("Press Enter to exit...")

# Run the main program
if __name__ == "__main__":
    main()
