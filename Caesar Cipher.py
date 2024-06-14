def caesar_cipher(text: str, shift: int, encrypt: bool = True) -> str:
    """
    Encrypts or decrypts a text using the Caesar cipher algorithm.

    Args:
        text (str): The input text to be encrypted or decrypted.
        shift (int): The shift value to be used for encryption or decryption.
        encrypt (bool, optional): Whether to encrypt (True) or decrypt (False). Defaults to True.

    Returns:
        str: The encrypted or decrypted text.
    """
    result_text = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            shift_direction = shift if encrypt else -shift
            result_text += chr((ord(char) - offset + shift_direction) % 26 + offset)
        else:
            result_text += char
    return result_text

def encrypt_message(text: str, shift: int) -> str:
    """
    Encrypts a message using the Caesar cipher algorithm.

    Args:
        text (str): The input text to be encrypted.
        shift (int): The shift value to be used for encryption.

    Returns:
        str: The encrypted text.
    """
    return caesar_cipher(text, shift, encrypt=True)

def decrypt_message(text: str, shift: int) -> str:
    """
    Decrypts a message using the Caesar cipher algorithm.

    Args:
        text (str): The input text to be decrypted.
        shift (int): The shift value to be used for decryption.

    Returns:
        str: The decrypted text.
    """
    return caesar_cipher(text, shift, encrypt=False)

def main() -> None:
    """
    The main function that runs the Caesar cipher program.
    """
    while True:
        choice = input("Do you want to (e)ncrypt or (d)ecrypt a message? ").lower()
        if choice in ['e', 'd']:
            text = input("Enter your message: ")
            shift = int(input("Enter the shift value: "))
            if choice == 'e':
                processed_text = encrypt_message(text, shift)
                print("Encrypted text:", processed_text)
            else:
                processed_text = decrypt_message(text, shift)
                print("Decrypted text:", processed_text)
        else:
            print("Invalid choice! Please select 'e' for encryption or 'd' for decryption.")
        
        continue_choice = input("Do you want to continue? (yes/no): ").lower()
        if continue_choice!= 'yes':
            break

if __name__ == "__main__":
    main()
