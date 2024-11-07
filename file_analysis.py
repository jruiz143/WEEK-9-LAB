#9-6 PROGRAMMING EXERCISE
#WRITE A PROGRAM THAT READS THE CONTENTS OF TWO
#TEXT FILES AND COMPARES THEM IN THE FOLLOWING:
#DISPLAY A LIST OF ALL UNIQUE WORDS CONTAINED IN BOTH FILES (union)
#DISPLAY A LIST OF THE WORDS THAT APPEAR IN BOTH FILES (intersection)
#DISPLAY A LIST OF THE WORDS THAT APPEAR IN THE FIRST FILE BUT NOT THE SECOND (difference)or for words in file1.difference(file2)
#DISPLAY A LIST OF THE WORDS THAT APPEAR IN THE SECOND FILE BUT NOT THE FIRST (difference)or for words in file2.difference(file1)
#DISPLAY A LIST OF THE WORDS THAT APPEAR IN EITHER THE FIRST OR SECOND BUT NOT BOTH(symmetric)
#HINT USE SET OPERATIONS TO PERFORM ANALYSES(for name in blank.difference())

#OPEN AND READ TWO FILES. CREATE SETS
with open('file1.txt', 'r') as file1:
      file1_contents= file1.read() #STORE FILE CONTENTS IN FILE1_CONTENTS VARIABLE
      contents1= set(file1_contents.split())#SPLIT THE CONTENTS FOUND IN FILE1 INTO SET. SPLIT WORDS.

with open('file2.txt', 'r') as file2:
      file2_contents= file2.read() #STORE FILE CONTENTS IN FILE2_CONTENTS VARIABLE
      contents2= set(file2_contents.split())#SPLIT THE CONTENTS AFTER THE FILE HAS BEEN READ


unique_words = contents1.union(contents2) #COMBINE BOTH SETS USING UNION OPERATOR--AUTOMATICALLY 
combine_contents = contents1.intersection(contents2)#LIST OF THE WORDS THAT APPEAR IN BOTH FILES (intersection)
file1_unique_words = contents1.difference(contents2)#LIST OF THE WORDS THAT APPEAR IN THE FIRST FILE BUT NOT THE SECOND (difference)
file2_unique_words = contents2.difference(contents1)#LIST OF THE WORDS THAT APPEAR IN THE SECOND FILE BUT NOT THE FIRST
words_in_either = contents1.symmetric_difference(contents2)#DISPLAY A LIST OF THE WORDS THAT APPEAR IN EITHER THE FIRST OR SECOND BUT NOT BOTH
#DISPLAY RESULTS
print (f"FILE 1 CONTENTS: {contents1}")
print (f"FILE 2 CONTENTS: {contents2}")
print(f"ALL THE UNIQUE WORDS FOUND IN BOTH FILES:\n{unique_words}")
print (f"A LIST OF THE WORDS THAT APPEAR IN BOTH FILES:\n {combine_contents}")
print (f"A LIST OF THE WORDS THAT APPEAR IN THE FIRST FILE BUT NOT THE SECOND:\n {file1_unique_words}")
print (f"A LIST OF THE WORDS THAT APPEAR IN THE SECOND FILE BUT NOT THE FIRST:\n {file2_unique_words}")
print (f"A LIST OF THE WORDS THAT APPEAR IN EITHER THE FIRST OR SECOND BUT NOT BOTH:\n {words_in_either}")









