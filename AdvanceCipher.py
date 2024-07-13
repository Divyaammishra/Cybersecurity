def encrypt(message, key):
      # Initialize a list of empty strings to hold the ciphertext columns
      ciphertext = [''] * key

      # Loop through each column in the transposition grid
      for column in range(key):
        # Start at the current column
        pointer = column

        # Continue looping until the pointer goes past the end of the message
        while pointer < len(message):
          # Add the character at the current pointer position to the current column
          ciphertext[column] += message[pointer]
          # Move the pointer to the next row in the current column
          pointer += key

      # Join all the columns to form the final encrypted message
      return ''.join(ciphertext)

def main():
      # Get the message to encrypt from the user
      message = input("Enter the message: ")
      # Get the encryption key (number of columns) from the user
      key = int(input("Enter the key: "))

      # Encrypt the message and print the result
      print(encrypt(message, key))

    # If this script is run directly (not imported as a module), execute the main function
if __name__ == "__main__":
      main()
