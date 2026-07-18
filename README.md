# Caesar Cipher Tool

A simple and interactive Python program that implements the **Caesar Cipher** algorithm to encrypt and decrypt text messages based on a user-defined shift value.

## Features
- **Encryption**: Encodes a plaintext message by shifting letters forward.
- **Decryption**: Decodes a ciphertext message by reversing the shift.
- **Case Preservation**: Automatically preserves uppercase and lowercase letters.
- **Non-Alphabetic Support**: Keeps spaces, numbers, and special characters untouched during execution.
- **Input Validation**: Includes basic error handling for shift values and operational choices.

## How It Works
The Caesar Cipher is a type of substitution cipher where each letter in the plaintext is shifted a certain number of places down the alphabet. For instance, with a shift of 3, `A` becomes `D`, `B` becomes `E`, and so on.

## Technologies Used
- **Language**: Python 3.x
- **Core Libraries**: Built using standard Python without external dependencies.

## How to Run
1. Make sure you have Python installed.
2. Clone this repository or download the script.
3. Run the following command in your terminal:
   ```bash
   python caesar_cipher.py
