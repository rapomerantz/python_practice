#Read and Write Files
'''
fw = open('sample.txt', 'w') #<--Create an object file & prepare to write to it
fw.write('Writing some stuff in my txt file\n')
fw.write('Heres a new line')
fw.close() #<-- close it (save memory)

fr = open('sample.txt', 'r') #<--Create an object that opens a file and reads it
text = fr.read() #<--Assign the value of the object to a variable so it can be used
print(text)
testArray = []
for letter in text:
    if (letter != ' ' and letter != '\n'):
        testArray.append(letter)
print(testArray)
fr.close()
'''

#Download an image from the web
'''
import random
import urllib.request

def download_web_image (url):
    name = random.randrange(1, 1000)
    full_name = str(name) + '.jpg' #<- convert number to a string and add .jpg file extension
    urllib.request.urlretrieve(url, full_name)

download_web_image('http://2.bp.blogspot.com/-i9u4Saxb40c/T3FtMZZhg2I/AAAAAAAAA8U/C4QwoWERhUs/s1600/ligers-liger-rare-animals-liger-facts-4-5-2-1-5-6-7-2-3-1-5-3-2-1-7-3-4-2-1.png')
'''

#Modlues
'''
#name file you're importint
import taco
import random

#use dot notation to specify import.function()
taco.what_are_you()

x = random.randrange(1, 1000)
print(x)

y = random.choice([1,2,3,4])
print(y)
'''



#Dictionaries (OBJECTS)
'''
classmates = {'tony': 'cool but a little smelly', 'Ronnie': 'plays guitar', 'Emma': 'Sits behind me'}

# print(classmates)
# print(classmates['Emma'])

#loopin thru it (use .items())
for k, v in classmates.items():
    print (k, ':', v)
'''

#SETS
'''
#If you have duplicates it will only print it ONCE
groceries = {'milk', 'eggs', 'oreos', 'beer', 'duct tape', 'beer'}

print(groceries)

if 'milk' in groceries:
    print('you already have milk')
else: 
    print('Oh yeah you need milk')
'''

#Unpacking arguments
'''
def health_calculator(age, apples_eatten, cigs_smoked): 
    result = (100-age) + (apples_eatten * 3.5) - (cigs_smoked * 2)
    print('Health Rating:', result)

Atticus_data = [25, 4, 5]

#Old Way: 
health_calculator(Atticus_data[0],Atticus_data[1],Atticus_data[2])

#Pass each item in in order: 
health_calculator(*Atticus_data)
'''

#Flexible numbers of arguments
# declare *args and use a loop to address each one
'''
def add_numbers(*args): 
    print ('in add_numbers, Length:', len(args))
    total = 0
    for a in args:
        total += a
    print(total)
    return total

print('add Numbers is:', add_numbers(1,2,3,4,5)) 


def multiply_numbers (*args): 
    print ('Length:',len(args))
    print ('args[0]:',args[0])
    total = args[0]
    for a in args[1:]:
        total = total * a
    print(total)

multiply_numbers(55, 6, 9, 3, 6, 9, 3, 6, 9, 3, 6, 9, 3, 6, 9, 3, 6, 9, 3, 6, 9, 3, 6, 9)


'''

#Key Word Arguements
'''
#Pass arguments in in any order you want 

def dumb_sentence(name = 'Atticus', action = 'ate', item = 'tuna'):
    print(name, action, item)

dumb_sentence()
dumb_sentence('Sally', 'runs', 'home')
dumb_sentence(item='apples') #<--identifying the arguments by name when not adding in expected order
'''



#Variable scope
'''
a = 12345

def taco():
    a = 54321
    print(a)

def fudge():
    print(a)

taco()
fudge()
'''

#Default values for arguements 
'''
def apple_flavor(color = 'unknown'):
    if color is 'green':
        taste = 'tart'
    elif color is 'red':
        taste = 'sweet'
    else:
        taste = 'dunno'
    return(taste)

print(apple_flavor('green'))
print(apple_flavor('red'))
print(apple_flavor('purple'))
print(apple_flavor())
'''

#Return values
#This is an example in the video, forgive me for using it :/
'''
def allowed_dating_age(my_age):
    their_age = (my_age / 2) + 7
    return their_age

shaynaLimit = allowed_dating_age(32)
creepyJoeLimit = allowed_dating_age(49)

print('shayna can date boys that are at least: ', shaynaLimit)
print('creepyJoe can date boys that are at least: ', creepyJoeLimit)

for n in range(18, 65): 
    result = allowed_dating_age(n)
    print('age: ',n,'result', result)
'''

#Functions
'''
def bitcoin_to_usd(bitcoin): #<--using an argument
    result = bitcoin * 15000   
    print(result) 

bitcoin_to_usd(55) #<--call function
bitcoin_to_usd(1)

def taco():
    print('in taco function')
    print('functions are cool')
taco()
'''

#Continue
'''
numbersTaken = [1, 5, 10, 12, 15, 3]

print('Numbers still available: ')

for n in range(1, 20): 
    if n in numbersTaken: #<-- check for number in list
        continue #<-- Skip the number and rest of code and restart the loop
    print(n)
'''

# The ol' fizz buzz
'''
for n in range(101):
    if n % 3 is 0 and n % 5 is 0:
        print(n, 'FizzBuzz')
    elif n % 3 is 0:
        print ('Fizz')
    elif n % 5 is 0: 
        print('Buzz')
    else:
        print('naw')
'''

#Break
#Find a magic number!!
'''
for n in range(101):
    if n % 4 is 0:
        print(n, 'is divisiable by 4')
        

magicNumber = 26

for n in range(101, 0, -2): 
    if n is magicNumber:
        print(n, 'is the magic number!!')
        break #<-- stops the loop once the magic number is found
    else: 
        print(n)
'''

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