#9-3 PROGRAMMING EXERCISE
#WRITE A PROGRAM THAT USES A DICTIONARY TO ASSIGN "CODES" 
#TO EACH LETTER OF THE ALPHABET
#EXAMPLE: CODES = {'A':'%', 'a':'9'}
#THE PROGRAM SHOULD OPEN A SPECIFIED TEXT FILE, READ ITS CONTENTS,
#THEN USE THE DICTIONARY TO WRITE AN ENCRYPTED VERSION OF THE FILE'S
#CONTENTS TO A SECOND FILE. EACH CHARACTER IN THE SECOND FILE SHOULD 
#CONTAIN THE CODE FOR THE CORRESPONDING CHARACTER IN THE FIRST FILE.
#WRITE A SECOND PROGRAM THAT OPENS AN ENCRYPTED FILE AND DISPLAYS ITS
#DECRYPTED CONTENTS ON THE SCREEN


# CREATE DICTIONARY TO STORE CODES
codes = {
    'A': '%', 'B': '&', 'C': '#', 'D': '@', 'E': '$', 'F': '!', 'G': '^', 'H': '*', 'I': '(', 'J': ')',
    'K': '-', 'L': '+', 'M': '=', 'N': '~', 'O': '{', 'P': '}', 'Q': '[', 'R': ']', 'S': '|', 'T': '\\',
    'U': ':', 'V': ';', 'W': '"', 'X': "'", 'Y': '<', 'Z': '>', 
    'a': '9', 'b': '8', 'c': '7', 'd': '6', 'e': '5', 'f': '4', 'g': '3', 'h': '2', 'i': '1', 'j': '0',
    'k': '!', 'l': '@', 'm': '#', 'n': '$', 'o': '%', 'p': '^', 'q': '&', 'r': '*', 's': '(', 't': ')',
    'u': '-', 'v': '=', 'w': '_', 'x': '+', 'y': '~', 'z': '{', ' ': ' '
}
#CREATE A DICTIONARY TO REVERSE CODES FOR DECRYPTION
reverse_codes = {}
for key, value in codes.items():
    reverse_codes[value] = key

# WRITE AN ENCRYPTED VERSION OF THE FILE'S CONTENTS TO A SECOND FILE
def text_encryption(input_filename, output_filename, codes):
    try:
        with open(input_filename, 'r') as file:
            original_text = file.read()#READ CONTENTS OF FILE
        
        encrypted_text = "" #CREATE EMPTY STRING THAT WILL STORE RESULTS
        for char in original_text:#LOOP THROUGH EACH CHARACTER IN THE STRING
            encrypted_text += codes.get(char, char)  # CHECK IF CHARACTER EXISTS AS A KEY IN THE CODES DICTIONARY
        
        with open(output_filename, 'w') as encrypted_file:
            encrypted_file.write(encrypted_text)
        
        print("THE FILE HAS BEEN ENCRYPTED")
    
    except FileNotFoundError:
        print(f"ERROR: {input_filename} NOT FOUND!")

# CREATE FUNCTION TO DECRYPT TEXT FROM ENCRYPTED FILE AND WRITE TO OUTPUT FILE
def decrypt_file(encrypted_filename, decrypted_filename, reverse_codes):
    try:
        with open(encrypted_filename, 'r') as file:
            encrypted_text = file.read()
        
        decrypt_text = ""
        for char in encrypted_text:
            decrypt_text += reverse_codes.get(char, char)  # DECRYPT USING REVERSE CODES
        
        with open(decrypted_filename, 'w') as decrypted_file:
            decrypted_file.write(decrypt_text)
        
        print("THE FILE HAS BEEN DECRYPTED")
    
    except FileNotFoundError:
        print(f"ERROR: {encrypted_filename} NOT FOUND!")

# ENCRYPT AND DECRYPT FILES
text_encryption('input.txt', 'encrypted_output.txt', codes)
decrypt_file('encrypted_output.txt', 'decrypted_output.txt', reverse_codes)
