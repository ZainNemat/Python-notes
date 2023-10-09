#!/bin/python3 

print("hello world!")
print('hello,world!')
print("""This string runs 
multiple lines!""") #triple quote for multi-line
print("This string is "+ "awesome!") #we can also concatenate
print('\n') #new line
print('Test that new line out.')

quote = "All is fair in love and war."
print(quote)

print(quote.upper()) #uppercase
print(quote.lower()) #lowercase
print(quote.title()) #titlecase
print(len(quote)) #counts characters

name = "Heath" #string
age = 33 #int
gpa = 3.7 #float - has a decimal

print(int(age))
print(int(30.1))
print(int(30.9)) #will it round? NO.

print("My name is " + name + " and I am " + str(age) + "years old.")

age += 1
print(age)

birthday = 1
age+= birthday
print(age)

print('\n')

#FUNCTIONS 

def who_am_i(): #this is a function without parameters
	name = "Zain" #local variable
	age = 30
	print("My name is " + name + " and I am " + str(age) + "years old.")
	
who_am_i()


def add_one_hundred(num):
	print(num + 100) 
	
		
add_one_hundred(100)

def add(x,y):
	print( x + y )
add(7,7)



def multiply(x,y):
	return x * y
	
multiply(7,7)
print(multiply(7,7))

def square_root(x):
	print(x ** .5)
	
square_root(64)

def nl():
	print('\n')
	
nl()

#BOOLEAN EXPRESSIONS (TRUE OR FALSE)

bool1 = True
bool2 = 3*3 == 9
bool3 = False
bool4 = 3*3 != 9 

print(bool1,bool2,bool3,bool4)
print(type(bool1))

bool5 = "True"
print(type(bool5))

nl()
#RELATIONAL AND BOOLEAN OPERATORS
greater_than = 7 > 5 
less_than = 5 < 7
greater_than_or_equal_to = 7 >= 7
less_than_equal_to = 7 <= 7

test_and = (7 > 5) and (5 < 7) #True
test_and2 = (7 > 5) and (5 > 7) #False
test_or = (7 > 5) or (5 < 7) #True
test_or2 = (7 > 5) or (5 > 7) #True

test_not = not True #False

#CONDITIONAL STATEMENTS - if/else 

def drink(money):
	if money >= 2:
		return "You've got yourself a drink!"
	else:
		return "No drink for you!"
print(drink(3))
print(drink(1))

def alcohol(age,money):
	if(age >= 21) and (money >= 5):
		return "We're getting a drink!"
	elif (age >= 21) and (money < 5): 
		return "Come back with more money."
	elif (age < 21) and (money >= 5):
		return "Nice try,kid!"
	else:
		return "You're too young and too poor."

print(alcohol(21,5))
print(alcohol(21,4))
print(alcohol(20,5))
print(alcohol(20,4))


nl()
#LISTS - Have brackets []
movies = ["When Harry Met Sally", "The Hangover" , "The Perks of Being a Wallflower", "The Exorcist"]

print(movies[1]) #returns the second item in the list
print(movies[0]) #return the first item in the list
print(movies[1:3]) #return the first index number given right until the last number, but not include the last number
print(movies[1:])
print(movies[:1])
print(movies[-1]) #return last item in the list

print(len(movies)) #count items in the list
movies.append("JAWS")
print(movies) #appends to the end of the list

movies.insert(2, "Hustle")
print(movies) 

movies.pop() #removes last item in the list
print(movies)

movies.pop(0) #removes the first item in the list
print(movies)

friend_movies = ['Just Go With It' , '50 First Dates' ]
our_favourite_movies = movies + friend_movies
print(our_favourite_movies)

grades = [["Bob", 82], ["Alice",90] , ["Jeff" , 73] ]
bobs_grade = grades[0][1]
print(bobs_grade)
grades[0][1] = 83
print(grades)


nl() 
#TUPLES - Do not change, ()
grades = ("a", "b" , "c" , "d" , "f")

print(grades[1])

nl()
#LOOPING

#For loops - start to finish of an iterate
vegetables = ["cucumber", "spinach" , "cabbage"]
for x in vegetables:
	print(x)
	
	
#While loops -execute as long as True
i = 1 

while i < 10:
	print(i)
	i += 1
	
nl()
#ADVANCED STRINGS

my_name = "Zain"
print(my_name[0]) #first letter
print(my_name[-1]) #last letter

sentence = "This is a sentence."
print(sentence[:4])
print(sentence.split()) #delimeter - default is a space

sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split)
print(sentence_join)

quote = "He said, give me all your money"
print(quote)
quote = "He said , \"give me all your money \" "
print(quote)

too_much_space = "                       hello              "
print(too_much_space.strip())


print("A" in "Apple") #True
print("a" in "Apple") #False
letter = "A"
word = "Apple"		
print(letter.lower() in word.lower()) #improved

movie = "The Hangover"
print("My favorite movie is {}.".format(movie))
print("My favorite movie is %s." % movie)
print(f"My favorite movie is {movie}.")


nl()
#DICTIONARIES - key/value pairs {} 

drinks = {"White Russian": 7 , "Old Fashioned" : 10, "Lemon Drop" : 8} #drink is the key, price is the value

print(drinks)

employees = {"Finance" : ["Bob" , "Linda" , "Tina" ] , "IT": ["Gene" , "Louise", "Teddy"] , "HR": ["Jimmy Jr." , "Mort"]}
print(employees)

employees['Legal'] = ["Mr. Frond "] #adds new key:value pair
print(employees)

employees.update({"Sales": ["Andie", "Ollie"]}) #adds new key:value pair
print(employees)

drinks['White Russian'] = 8
print(drinks)

print(drinks.get("White Russian"))
										
