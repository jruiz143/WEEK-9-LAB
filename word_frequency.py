#9-5 PROGRAMMIN EXERCISE
#WRITE A PROGRAM THAT READS THE CONTENTS OF A TEXT FILE.
#THE PROGRAM SHOULD CREATE A DICTIONARY IN WHICH THE KEYS ARE INDIVIDUAL WORDS
#FOUND IN THE FILE. FOR EXAMPLE, IF THE WORD "THE" APPEARS 128 TIMES,
#THE DICTIONARY WOULD CONTAIN AN ELEMENT 'THE' AS THE KEY AND 128 AS THE VALUE.
#THE PROGRAM SHOULD EITHER DISPLAY THE FREQUENCY OF EACH WORD OR CREATE A SECOND FILE
#CONTAINING A LIST OF EACH WORD AND ITS FREQUENCY

with open('word_frequency.txt', 'r') as file:
      file_contents = file.read().lower()#READ FILE
      words = set(file_contents.split())#CREATE SET FOR FILE CONTENTS
      print(file_contents)

word_count= {}

for word in words:
      word = word.strip("'!,.?;:")#REMOVE EXCLAMATION CHARACTERS
      if word in word_count:#LOOP THROUGH EACH LINE 
            word_count[word]+= 1#ADD WORD TO WORD COUNT IF FOUND MULTIPLE TIMES
      else:
            word_count[word] = 1#ELSE JUST KEEP IT TO SINGLE COUNT

for word, count in word_count.items():
      print(f'THE WORD "{word}", APPEARS "{count}" TIMES.')
