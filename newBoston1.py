





#Range and While
'''
#While loop (define your increment)
testNumber = 5;

while testNumber < 10:
    print(testNumber)
    testNumber += 1

#Loop through range setting increment
for x in range(0, 10, 2):
    print(x)
   
#Run a loop through a range
for x in range(5, 12): 
    print(x)

#Run a loop 10 times (not releated to a list)
for x in range(10):
    print('')
'''

#For Loops
'''
foods = ['taco', 'burrito', 'pasta', 'coffee']

#functions in the same way as a JS 'for in' loop
#use braket notation like [1:3] to only to through a slice of the list
#a for loop of a string will loop through each character in a string

for item in foods: 
    print(item)

for item in foods[1:3]: 
    print(item)
    print('Number of letters in',item,':', len(item))    
'''

#if/elif/else
'''
number = 1
if number is 1:
    print('number is 1')
elif number is 'Atty':
    print('Name is Atty')
else:
    print('Nada baby')
'''