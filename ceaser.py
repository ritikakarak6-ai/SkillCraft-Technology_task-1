def caesar_cipher(text, shift, mode):
    result = ""
    
    # If the mode is decryption, reverse the shift
    if mode.lower() == 'd':
        shift = -shift
        
    for char in text:
        # Encrypt/Decrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt/Decrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        # Keep spaces and special characters as they are
        else:
            result += char
            
    return result

def main():
    print("--- Caesar Cipher Program ---")
    
    # Take user input for the operation mode
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? Enter E or D: ").strip().lower()
    
    if choice not in ['e', 'd']:
        print("Invalid choice! Please enter 'E' or 'D'.")
        return

    message = input("Enter your message: ")
    
    try:
        shift = int(input("Enter the shift value (e.g., 3, 5): "))
    except ValueError:
        print("Invalid shift value! Please enter an integer.")
        return

    # Perform the operation
    output = caesar_cipher(message, shift, choice)
    
    if choice == 'e':
        print(f"\nEncrypted Message: {output}")
    else:
        print(f"\nDecrypted Message: {output}")

if __name__ == "__main__":
    main()
