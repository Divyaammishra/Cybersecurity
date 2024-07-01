def caesar(message, key, mode):
  # List of uppercase alphabet letters
  LetterList = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  translated = ''
  # Convert message to uppercase
  message = message.upper()
  # Ensure key is within the range of 0-25
  key = key % 26

  # Iterate over each character in the message
  for i in message:
      # Find the index of the character in the alphabet list
      tempLetter = LetterList.find(i)
      # Check if character is found in the list
      if tempLetter != -1:
          # Encrypt or decrypt based on mode
          if mode == 'encrypt':
              tempLetter += key
          elif mode == 'decrypt':
              tempLetter -= key

          # Handle wrap-around if index goes out of bounds
          if tempLetter >= len(LetterList):
              tempLetter -= len(LetterList)
          elif tempLetter < 0:
              tempLetter += len(LetterList)

          # Append the translated character to the result
          translated += LetterList[tempLetter]
      else:
          # If character is not in the list, add it unchanged
          translated += i

  return translated

# Get user inputs
userMessage = input("Enter your message: ")
userKey = int(input("Enter your key: "))
userMode = input("Enter your mode (encrypt/decrypt): ")

# Print the translated message
print(caesar(userMessage, userKey, userMode))
