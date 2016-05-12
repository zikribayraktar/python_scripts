# This file aims to document some of the simple
# introductory Python information for future reference:
#
# This line is a comment line.
""" This is a multiline comment that spans over
 multiple lines and combines multiple comments """
#
# For help on built-in functions:
help(len)   #help for the built-in function len().
#----------------------------------------------------------
#useful packages
from datetime import datetime
dtNOW = datetime.now()
dtNOW.year	#current year
dtNOW.month #current month
dtNOW.day	#current day
dtNOW.hour	#current hour
dtNOW.minute  #current minute
dtNOW.second  #current second
#----------------------------------------------------------
print 'Hello World!'

ApplePi = 3.1415
print("%.2f" % ApplePi)	  #only prints two decimal places of the FLOATING number

#note the use of backslash to print special characters
print 'This isn\'t apple pie, it is blueberry!'

# the letter from second place of the string. Remember, index starts from ZERO.
second_letter = "MONTYPYTHON"[2] 
print second_letter

#----------------------------------------------------------
# indentation
def myNumber(answer):
    myN = 12*answer
    return myN
# Note that 4 space indentation is required 
# as well as the semicolon at the end of DEF line.
myNumber(5)  #call the function
#----------------------------------------------------------
# Simple Math
1+2
4-3
3*4
9/5	# note that int/int will only return int.
9/5.0	# at least one of the terms need to be float.
10**2	# to the second power.
pow(10,2)	# to the second power.
4%3		# modulo
#----------------------------------------------------------

#----------------------------------------------------------
# Variables, 
x = 9
y = 2
x += y		# same thing as x=x+y
my_int = 7
my_float = 3.1415
my_bool = True
my_bool = 3*4 != 3**4
#other boolean operators:  and , or , not , 
#----------------------------------------------------------

#----------------------------------------------------------
# Strings
a = 'Hello'
b = ' ' 
c = 'World'
d = a+b+c
e = 'Another ' + 'string ' + 'combined.'

len(d)  #length of the string
d.lower()   #converts to all lower letters
d.upper()    #converts to all upper letters
d.isalpha()   #check if alpha-numeric
pi=3.1415   #floating number
str(pi)		#convert floating to string

#STRING FORMATTING - combine strings with variables
string_1 = 'NYC'
string_2 = 'Sunday'
z =  "I'm in %s. today is %s." % (string_1, string_2)

#----------------------------------------------------------

#----------------------------------------------------------
# input from console:
datain = raw_input('Please type a word!\n')
#----------------------------------------------------------

#----------------------------------------------------------
# Lists
myCars= ['Ferrari', 'Porsche', 'Massarati', 'Bentley', 330]
myCars.append("Tesla")  #append another item to the list.
carIndex = myCars.index('Tesla')  #find the index of the item specified.
myCars.pop(0)  #remove item from list
print myCars[0]				#remember that Python index starts from ZERO.
print myCars[-1]			# negative indexing in Lists goes backwards in the list
print myCars[2:]			#start position# to end of list
print myCars[:3]			#from beginning of the list to end position#
myCars.remove('Bentley')    #remove item from list

# RANGE function
range(stop)
range(start, stop)
range(start, stop, step)
#----------------------------------------------------------
#CONTROL FLOW
# IF ELSE CONDITIONAL STATEMENTS
answer = raw_input("Enter a number between 1 and 4\n")
if answer == "1" or answer == "2":
    print "You picked first half!"
elif answer == "3" or answer == "4":
    print "You picked second half!"
else:
    print "You didn't pick properly!"


# FOR LOOP
my_list = [1,2,3,4,5]
for number in my_list:
    print 3*number

#----------------------------------------------------------
#FUNCTIONS
def cubed(n):
    """Returns the 3rd power of a number."""
    cubed = n**3
    print "%d cubed is %d." % (n, cubed)
    return cubed
    
#call the function with a value
cubed(10)

# Import *everything* from the math module on line 3!
from math import *

# import random module
import random
AllFunctions = dir(random)

#----------------------------------------------------------
# DICTIONARY -- key-value pairs
cars = {'Ferrari' : 250, 'Porsche' : 100, 'BMW' : 100, 'Tesla' : 100 }
print cars['Ferrari']
del cars['Ferrari']  #delete by key.
cars['Tesla'] = 200	 #change the value.
cars['Honda'] = 30   #add new key-value to dictionary


#----------------------------------------------------------
#----------------------------------------------------------
#----------------------------------------------------------
#----------------------------------------------------------
#----------------------------------------------------------

# Recursive Function
def factorial(nv):
	if nv==0:
		return 1
	else:
		return nv*factorial(nv-1)
#----------------------------------------------------------