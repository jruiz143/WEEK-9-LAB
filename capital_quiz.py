#9-2 PROGRAMMING EXERCISE
#WRITE A PROGRAM THAT CREATS A DICTIONARY CONTAINING
#THE U.S. STATES AS KEYS AND THEIR CAPITALS AS VALUES.
#THE PROGRAM SHOULD THEN RANDOMLY QUIZ THE USER BY DISPLAYING THE NAME OF A STATE 
#AND ASKING THE USER TO ENTER THE STATE'S CAPITAL
#THE PROGRAM SHOULD KEEP A COUNT OF THE NUMBER OF CORRECT
#AND INCORRECT RESPONSES

num_states= 5

def main(): 
      #INTIALIZE STATE CAPS DICTIONARY
      state_caps = state_cap_dictionary()
      #INTIALIZE VARIABLES TO KEEP COUNT OF THE NUMBER OF CORRECT AND INCORRECT ANSWERS
      correct = 0
      incorrect = 0
      #QUIZ THE USER.
      for count in range(num_states):
            #GET A RANDOM ENTRY FROM THE DICTIONARY
            state, capital = state_caps.popitem()
            #QUIZ THE USER
            print('WHAT IS THE CAPITAL OF', state, '?', end=' ')
            response = input()
            if response.lower()==capital.lower():
                  correct += 1
                  print('CORRECT!')
            else:
                incorrect += 1
                print ("INCORRECT!")
      print('CORRECT RESPONSES:', correct)
      print('INCORRECT RESPONSES:', incorrect)

            
#CREATE DICTIONARY OF STATES(KEY) AND CAPITALS(VALUES)
def state_cap_dictionary():
      sc = {
      'Alabama': 'Montgomery',
      'Alaska': 'Juneau',
      'Arizona': 'Phoenix',
      'Arkansas': 'Little Rock',
      'California': 'Sacramento',
      'Colorado': 'Denver',
      'Connecticut': 'Hartford',
      'Delaware': 'Dover',
      'Florida': 'Tallahassee',
      'Georgia': 'Atlanta',
      'Hawaii': 'Honolulu',
      'Idaho': 'Boise',
      'Illinois': 'Springfield',
      'Indiana': 'Indianapolis',
      'Iowa': 'Des Moines',
      'Kansas': 'Topeka',
      'Kentucky': 'Frankfort',
      'Louisiana': 'Baton Rouge',
      'Maine': 'Augusta',
      'Maryland': 'Annapolis',
      'Massachusetts': 'Boston',
      'Michigan': 'Lansing',
      'Minnesota': 'Saint Paul',
      'Mississippi': 'Jackson',
      'Missouri': 'Jefferson City',
      'Montana': 'Helena',
      'Nebraska': 'Lincoln',
      'Nevada': 'Carson City',
      'New Hampshire': 'Concord',
      'New Jersey': 'Trenton',
      'New Mexico': 'Santa Fe',
      'New York': 'Albany',
      'North Carolina': 'Raleigh',
      'North Dakota': 'Bismarck',
      'Ohio': 'Columbus',
      'Oklahoma': 'Oklahoma City',
      'Oregon': 'Salem',
      'Pennsylvania': 'Harrisburg',
      'Rhode Island': 'Providence',
      'South Carolina': 'Columbia',
      'South Dakota': 'Pierre',
      'Tennessee': 'Nashville', 
      'Texas': 'Austin',
      'Utah': 'Salt Lake City',
      'Vermont': 'Montpelier',
      'Virginia': 'Richmond',
      'Washington': 'Olympia',
      'West Virginia': 'Charleston',
      'Wisconsin': 'Madison',
      'Wyoming': 'Cheyenne'
      }
      return sc
main()

