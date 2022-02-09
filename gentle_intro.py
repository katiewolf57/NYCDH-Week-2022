#!/usr/bin/env python3

## A Gentle Intro to Python ##

## THESE ARE COMMENTS ##
# They don't affect the code and are used to make code more readable
# Comments are made by using the hashtag '#' symbol
# as you can see the '#' symbol in quotes won't affect the comment
"""
You can make
multiline comments
by using a triple ' " ' symbol
"""
# Comments can also be used to only test out certain blocks of code at a time

## these are all the MODULES I use in this set of code
## we'll talk about these at the end! 
import random


"""
~~~
An intro to the basic buidling blocks of Python
~~~

"""




## Variables ##

# ## x is the variable
# x = "hello"
# print(x)

# ## you can assign multiple variables at a time
# x, y, z = "a", "b", "c"
# print(x, y, z)

# ## can assign many values to a variable
# ## but be careful! this results in a tuple data tupe
# testing = 6, 8, 9
# print(testing)
# print(type(testing))


## Data Types! ##

## Strings + Integers + Floats ##

# string_text = "Hello there!"
# integer_number = 57
# float_number = 2.22222
# print('~~~~~~\n')

# print(string_text)
# print(type(string_text))
# print('~~~~~~\n')

# print(integer_number)
# print(type(integer_number))
# print('~~~~~~\n')

# print(float_number)
# print(type(float_number))
# print('~~~~~~\n')


## Operators ##
## +, -, **, *, %, >, <, ==, != ##

# print("2+2 =", 2+2)
# print("10 * 5 =", 10*5)
# print("2^2 =", 2**2)
# print("Is 3 > 5", 3>5)
# print("Is 6 equal to 7?", 6==7)
# print("Is 10 not equal to 20?", 10!=20)
# print("Is 'a' in cat?", 'a' in 'cat')


## Lists ##
## an ORDRED sequence of elements ##

# animal_list = ['cat', 'dog', 'mouse']
# print(animal_list)

# number_list = [0, 1, 2, 3, 4, 5]
# print(number_list)

# mixed_list = [0, 'one', True]
# print(mixed_list)

# lists can also have lists in them! 
# a list within a list - a nested list! 

# list_in_a_list = [1, 2, [3, 4, 5], 6]
# print(list_in_a_list)


## Dictionaries ##
## key:value pairs ##

# a_dictionary = {"name":"Spot",
# 				"age": 7,
# 				"adpoted": True,
# 				"colors": ["brown", "black", "yellow"]
# 				}

# print(a_dictionary)

## dictionaries can be nested just lists

# nested_dictionary = {
# 					"pet_1" : {
# 					"name": "Fuzzy",
# 					"species": "cat",
# 					"age": 10,
# 					},
# 					"pet_2": {
# 					"name": "Ratthew",
# 					"species": "rat",
# 					"age": 1,
# 					},
# 					"pet_3": {
# 					"name": "Spot",
# 					"species": "dog",
# 					"age": 7,
# 					}
# }

# print(nested_dictionary)






"""
~~~
Now let's play around with these objects!
Indexing + Slicing + Counting
~~~

"""




## Indexing ##

# a_list = ["cat", "dog", "bird", "mouse", "lizard", "horse"]
# print(a_list)

# print(a_list[0])

# print(a_list[4])

# print(a_list[-1])

# print(a_list[-3])


## Slicing ##

# format -> [ start : end : step size ]
# a_list = ["cat", "dog", "bird", "mouse", "lizard", "horse"]
# print(a_list)

# print(a_list[:3])
# # remember that the index is NOT inclusive
# # so this will stop at the SECOND entry 
# # it goes all the way up to but DOES NOT INCLUDE the 3rd entry

# print(a_list[2:])

# print(a_list[-6:-2])

# print(a_list[0:4])
# # notice that [-6:-2] is the same as [0:4]!

# print(a_list[-2:-5])
# # this gives an empty list! any idea why?

# print(a_list[0:5:2])
# # now we skip every other entry

# print(a_list[::-1])
# # this gives us the list backwards

## Indexing and slicing strings ##

# my_string = "hello there!"
# print(my_string)

# print(my_string[0])
# print(my_string[-1])
# print(my_string[4] == 'o')
# print(my_string[0:-1:2])

## What if we encoutnered a list within a list ##

# list_2 = [1, 2, [3, 4, 5], 6]
# print(list_2)

# print(list_2[2])
# # the above gives us a list as a result - can that be indexed or sliced? 
# # YES! 

# print(list_2[2][0])
# print(list_2[2][1:2])


## you can also use indexing to change strings! ##
# a_list = ["cat", "dog", "bird", "mouse", "lizard", "horse"]
# print(a_list[2])

# # simple REASSIGN it
# a_list[2] = "butterfly"
# print(a_list)
# print(a_list[2])
# # bird is now gone! 

## Let's count a bit too!  ##

# my_string = "hello there!"
# print(len(my_string))
# ## counts total number of characters

# my_list = [1, 2, 3, 4, 5]
# print(len(my_list))
# ## counts number of items in the list! 


# ## before it prints - any idea what this will do?
# print(my_list[0:5])





"""
~~~
Now let's play around with STRINGS!
Fun String Things
~~~

"""





# long_string = "this is a long bit of text that we need to check for content! Won't this be fun.   "

# # how long is our long string?
# print(len(long_string))

# # check to see if the string contains a certain bit of text
# print("text" in long_string)
# print("cat" in long_string)

# # check to see if this string DOES NOT contain a bit of text
# print("text" not in long_string)
# print("cat" not in long_string)

# print('~~~~~~\n')

# # just like with lists, we can change strings! 
# # but - the method is a bit different
# # we are using a "method" - these are built in tools that work on strings
# # the method we'll use is replace()

# print(long_string)
# print(long_string.replace("long", "very long"))

# print(long_string.replace("t", "w"))


# print('~~~~~~\n')

# # let's change the format a bit
# print(long_string.upper())
# """
#  note the above is NOT permanently chaning the string stored in the
#  'long_string' variable
#  it is printing out that variable in a different format. 
#  What if we WANTED to change the format permanently?
#  We'd need to 'reassign' the variable
#  """
# print(long_string)

# # NOW it's upper case
# long_string = long_string.upper()
# print(long_string)

# # now we want it lower case! 
# long_string = long_string.lower()
# print(long_string)

# print('~~~~~~\n')


# # what if we want to split it into two sentences?
# # use split()!

# split_string = long_string.split("!")
# print(split_string)
# print(type(split_string))
# print(len(split_string))
# # wait a minute! this isn't a string any more! it's a list! 

# print('~~~~~~\n')


# # remember we can smush strings togehter using the + charater
# string_a = "first bit"
# string_b = "second bit"

# combo = string_a + string_b
# print(combo)
# # notice it does not add a space! 

# combo_with_a_space = string_a + " " + string_b
# print(combo_with_a_space)

# print('~~~~~~\n')

# # now let's see if we can put this all back together! 

# print(split_string[0])
# print(split_string[1])

# new_long_string = split_string[0] + "!" + split_string[1]
# print(new_long_string)

# # what if we wanted these two separate strings capitalized as well?

# new_long_string = split_string[0].capitalize() + "!" + split_string[1].capitalize()
# print(new_long_string)

# print('~~~~~~\n')


# # wait! why didn't the second sentence get capitalized?
# # let's take a look
# print(split_string[1])
# # it looks like it has a whitespace in front of it! 

# print('~~~~~~\n')


# # you can remove whitespace from a string using strip()!
# whitespace_string = "   hello there's a lot of whitespace here     "
# print(whitespace_string)

# stripped_string = whitespace_string.strip()
# print(stripped_string)

# print('~~~~~~\n')

# ## now let's try it out our whitespace heavy string
# new_long_string = split_string[0].capitalize() + "! " + split_string[1].strip().capitalize()
# print(new_long_string)

## NOTES ABOUT ABOVE ##
"""
Note 1: I added in a space to the "!" part 
because we removed the space that was there before when
we used the strip() method

If we were printing like this: 
print(split_string[0].capitalize, "!", split_string[1].strip().capitalize())
We wouldn't need to add a space, as a space is automatically added in between everything listed by commas in a print statement
Note 2: Do you see how I combined strip() and capitalize()?
You can combine methods! They'll be performed in the order you write them! 
"""



"""
~~~
Now let's play around with LISTS!
Let's Look at LISTS
~~~

"""

## you can add to lists! use append()

# list_a = ["cat", "dog", "mouse", "rat"]
# print(list_a)


# list_a.append("lizard")
# print(list_a)

# ## but what if we don't want it at the end?

# list_a.insert(0, "butterfly")
# print(list_a)

# ## actually we don't like butterflies! 

# list_a.remove("butterfly")
# print(list_a)

# ## we want whatever the 2nd index is to go as well

# list_a.pop(2)
# # del list_a[2] #<- this is the same as above
# print(list_a)

# # these need to be in alphabetical order! 
# list_a.sort()
# print(list_a)

# #no! the other way! 
# list_a.sort(reverse=True)
# print(list_a)

# ## we need two of these please
# list_b = list_a.copy()

# ## notice we needed to assign this one = that's because we have to be able to call the copy somehow!

# print(list_b)

# ## a new round of animals! 
# list_c = ["kangaroo", "koala", "wallaby"]

# ## let's get these animals acquainted :)
# big_list = list_a + list_c

# print(big_list)

# ## there's another way too
# ## but this requires to reassigning! 
# list_b.extend(list_c)
# print(list_b)

# ## so the "+" is used to create a new bigger list, while extend() is used to make an existing list bigger
# ## and finally let's just empty the list completely! 

# list_a.clear()
# print(list_a)

# """
# Important note! 
# When we're updating using a method on lists
# we don't have to reassign it a new variable like we did with strings! 
# """

"""
~~~
Now let's play around with DICTIONARIES
What about DICTIONARIES
~~~

"""


# a_dictionary = {"name":"Spot",
# 				"age": 7,
# 				"adpoted": True,
# 				"colors": ["brown", "black", "yellow"]
# 				}


# # # let's learn about our dictionary
# print(a_dictionary)
# print(len(a_dictionary))
# print(a_dictionary["age"])
# print(a_dictionary.get("age"))

# print('~~~~~~\n')

# print(a_dictionary.keys())
# print(a_dictionary.values())
# print(a_dictionary.items())


# print('~~~~~~\n')

# # let's check to see what we have in it
# print("name" in a_dictionary)
# print("species" in a_dictionary)

# # now let's mess with it!
# ## use the method update() to update
# a_dictionary.update({"age":7})
# print(a_dictionary)

# a_dictionary.update({"species":"dog"})
# print(a_dictionary)

# """
# Important note! 
# When we're updating using a method on dictionaries
# we don't have to reassign it a new variable like we did with strings! 
# """

# a_dictionary["height"] = 5.3
# print(a_dictionary)
# # this also adds a key:value pair to the dictionary

# # let's remove some of this! 
# a_dictionary.pop("height")
# # this is the same as a_dictionary.del("height")
# print(a_dictionary)

# # what if we wanted to empty this? use clear()
# a_dictionary.clear()
# print(a_dictionary)
# ## prints just emtpy curly brackets! 

## nested dictionaries work the same! they just require a little thinging

# nested_dictionary = {
# 					"pet_1" : {
# 					"name": "Fuzzy",
# 					"species": "cat",
# 					"age": 10,
# 					},
# 					"pet_2": {
# 					"name": "Ratthew",
# 					"species": "rat",
# 					"age": 1,
# 					},
# 					"pet_3": {
# 					"name": "Spot",
# 					"species": "dog",
# 					"age": 7,
# 					}
# }

# print(nested_dictionary)
# print('~~~~~~\n')

# print(nested_dictionary["pet_1"])
# # this returns a dictionary! one of the nested ones
# # we can interact with this like any other dictionary

# print(nested_dictionary["pet_1"]["name"])

# # it may be easier to think of if we visualize it like this
# pet_1_dict = nested_dictionary["pet_1"]
# print(pet_1_dict)
# print(pet_1_dict["name"])



"""
~~~
If, Elif, and Else
Important Statements!
~~~

"""

## if statements are great for testing conditions

# ## remember how we can check to see if strings contain other strings?

# test_string = "hello, my name is Katie"

# if "name" in test_string:
# 	print("They're telling us a name!")
# else:
# 	print("no name info here")

# print('~~~~~~\n')

# ## these can also be used on lists, dictionaries, basically any object in python!

# test_list = [1, 4, 6, 8, 10, 100, 0]
# if 10 in test_list:
# 	print("10 is at index number " + str(test_list.index(10))) # <_ the index() method will tell us the index of the value we put in the (brackets)
# else:
# 	print("10 isn't here")

# print('~~~~~~\n')

# ## you can also nest if loops! 

# x = 500
# y = 500

# print("X = ", x, ", Y = ", y)
# if x > y:
# 	print("X is greater than Y.")
# 	if x % 10 == 0: ## this is a way of asking if x is divisilby by 10 with a remainder of 0
# 		print("X is divisible by 0")
# 	else:
# 		print("X is NOT divisible by 0")
# elif x == y:
# 	print("X is equal to Y.")
# 	if x % 3 == 0:
# 		print("X is divisible by 3")
# 	else:
# 		print("X is NOT divisible by 3")
# else:
# 	print("Y is greater than X")
# 	if y % 5 == 0:
# 		print("Y is divisible by 5")
# 	else:
# 		print("Y is NOT divisible by 5")

"""
IMPORTANT NOTES ON FORMATING

Note 1:
An "if statement" officially ends when you complete it with an "else statement"
However - you don't NEED an else statement
THIS:
if x == y:
	print("x equals y")

is a complete statement.

Note 2:
"elif" is an important keyword 
- it let's Python know that all your "if statments" are connected
You can have as many if statements as you want!
If you don't use "elif" and just have a series of "if statements" 
Python will treat them all as seperate sets of instructions
"""

## let's see the lots of elifs vs. lots of plain ifs in action

# print('~~~~~~\n')

# x = "cat"

# ### ALL ONE GROUP ##
# if x == "cat":
# 	print("cat")
# elif x == "dog":
# 	print("dog")
# elif x == "mouse":
# 	print("mouse")
# else:
# 	print("Not a animal worth talking about")

# ## NOT ALL ONE GROUP ##
# if x == "cat":
# 	print("cat")
# if x == "dog":
# 	print("dog")
# if x == "mouse":
# 	print("mouse")
# else:
# 	print("Not a animal worth talking about")


# ## note! 

# ## if statements CAN be written all in one line! 

# if x == "cat": print("x is a cat") ## this one does not support an else statement

# print("x is a cat") if x == "cat" else print("x is not a cat") 

## This can make it a bit harder to read in my opinion
## but others think that this looks cleaner
## You can use what you prefer! 

# ## Let's test out some logical operators ##
# print('~~~~~~\n')

# # And tests if BOTH conditions are true

# x = 10
# y = 100
# z = 1
# print("X = ", x, ", Y = ", y, ", Z = ", z)
# if x < z and y < z:
# 	print ("z is the biggest number")
# elif z < x or z < y:
# 	print("z is NOT the biggest number")
# elif z == x or z == y:
# 	pass
# else:
# 	("I'm not sure what's going on with z!")



"""
~~~
Stay a While! 
While Loops! 
~~~

"""

## while loops continually test if a condition is true
## they're a great way to count or measure change


# x = 1
# while x < 10:
# 	x += 1
# 	print(x)

# x = 1
# while x < 10:
# 	print(x)
# 	x += 1

# """
# IMPORTANT NOTE
# notice the difference between these two counters! 
# The first one prints 2 - 10
# The second prints 1 - 9
# That's because the first one adds to x and THEN prints
# The second prints out x and then ADDS! 
# Python will do exactly what you tell it in exactly the order you tell it
# So be aware of the order you're asking it to do things in
# I've had this mess me up many times! 
# """

# ## you can also use while loops to change lists
# ## and control their size


# list_a = [1, 2, 3]

# while len(list_a) < 8:
# 	list_a.append(random.randrange(0, 11))
# 	print(list_a)

# ## use break to stop the while statement, even if the original condition is try! 
# print('~~~~~~\n')

# list_a = [1, 2, 3]

# while len(list_a) < 8:
# 	list_a.append(random.randrange(0, 11))
# 	print(list_a)
# 	if 5 in list_a:
# 		break # this will stop the loop if a 5 appears in the randomly added numbers


# print('~~~~~~\n')

# ## use continue to go back to the behinning without completing the entire loop
# ## kind of like a "skip over this one" action


# ## what if I want to print out 1 - 10 but NOT 5
# x = 0

# while x < 10:
# 	x += 1
# 	if x == 5:
# 		continue
# 	print(x)

# ## question: what would happen if I put the x += 1 AFTER The continue?

# ## the else keyword should be familiar! 
# ## it has the same syntax as in the if statement - it's not indented under the while
# print('~~~~~~\n')

# list_a = [1, 2, 3]

# while 5 not in list_a:
# 	list_a.append(random.randrange(0,11))
# else:
# 	print(list_a)
# 	print("There's now a 5 at index", list_a.index(5))





"""
~~~
It's FOR the best to know FOR LOOPS
~~~

"""




## for loops work on any iterable object - because for loops iterate! 
# animal_list = ["cat", "dog", "mouse"]

# for animal in animal_list:
# 	print(animal)

# hi_there_string = "hi!"

# for char in hi_there_string:
# 	print(char)

# print('~~~~~~\n')

# pet_dict = {"name":"Spot", 
# 			"age":7,
# 			"colors":["brown", "white", "black"]	
# }

# for info in pet_dict:
# 	print(info)
# print('\n')

# ## this will ONLY print the keys, not the values
# ## how to fix this?

# for key in pet_dict:
# 	print(key, pet_dict[key]) ## as you can see, you can use the "info" to call the value associated with whatever key the loop is currently on


# ## now let's see some keywords! 
# print('~~~~~~\n')

# a_list = [1, 2, 3, 4, 5]
# for x in a_list:
# 	if x == 2:
# 		continue
# 	if x == 4:
# 		break
# 	print(x)

# print('\n')

# ## continue vs. pass! 
# a_list = [1, 2, 3, 4, 5]
# for x in a_list:
# 	if x == 3:
# 		continue
# 	print(x)

# print('\n')

# for x in a_list:
# 	if x == 3:
# 		pass
# 	print(x)

# #let's try our hand out at nested for loops! ##
# print('~~~~~~\n')

# list_1 = ["blue", "red", "green"]
# list_2 = ["dog", "cat", "mouse"]

# for x in list_1:
# 	print("This is an outer loop!")
# 	print("We're on the color ", x)
# 	for y in list_2:
# 		print('\n')
# 		print("This is an inner loop!")
# 		print("We're on the animal ", y)
# 		print("The ", y, " is ", x)
# 	print('~~~')

# ## maybe numbers might be more helpful?

# print('~~~~~~\n')

# for x in range(1,4):
# 	print("This is outer loop number", x)
# 	for y in range(1,3):
# 		print("This is the number", y, "inner loop for outer loop", x)
# 	print('~~~~~')




"""
~~~
Modular Building! 
Let's understand modules, libraries, and packages
~~~

"""


## to use a m/l/p you've imported, simply call it! 

# import random

# print(random.randint(0,9))




