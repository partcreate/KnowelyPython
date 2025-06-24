# Mutable and Immutable Objects
Some objects in Python allow us to change their internal state. Let's call them mutable objects. If we can't change the internal state of an object - it is unmutable. In this lesson we will learn how they work, how to use them – and why.

## Immutable Objects
Once an immutable object is created, we cannot change its internal state — i.e., behavior — during its lifetime. Such objects in Python are int, float, boolean, tuple, and string:

Let's look at the following code:

```python
string = "Hello, world!"
string[0] = "A"	# Error occurs
```

When we try to change an existing integer, Python creates a new integer object and sets the variable to reference the original object:

```python

```

```python
age = 18
age += 1 		# age = 19 but it is a new object in your program
```


We can see a new object with the id() function, which returns the memory address referenced by a variable. If two objects with the same value have different ids, they are different objects:

```python
age = 18	
print(id(age)) 		# 9789536

age += 1	
print(id(age)) 		# 9789568
```


This applies to other types as well:



```python
# string
string = "Hello"	
print(id(string)) 		# 140188299651440
string += ", world!"	            # We can create new strings using `+=` and `-=` operators
print(id(string)) 		# 140188299652208

# boolean
is_child = True		
print(id(is_child)) 		# 9476448
is_child = False	
print(id(is_child)) 		#  9474016

# tuple
fruits = ("apple", "banana")
fruits += "orange"	# Error occurs

# float
temperature = 23.3	
print(id(temperature)) 		# 139970588006672
temperature -= 1	
print(id(temperature)) 		# 139970588006544
```


As for tuples, even though they’re immutable, we can still modify mutable objects inside them:

```python
my_bag = (["phone charger", "laptop charger"], "napkins")

# Not allowed due to an error — tuple is an immutable object
my_bag[0] = ["phone charger", "laptop charger", "tablet charger"]

# Allowed because we change mutable objects inside
my_bag[0].append("tablet charger")
```


Mutable Objects
Mutable objects, such as list, dictionary, or set, can change their values, and often store data collections. They maintain the same memory id even after deleting, adding or changing elements. For example:

```python
# list
my_list = [1, 2, 3, 4, 5]			
print(id(my_list))			# 140389498084928
my_list.append(6)			
print(id(my_list))			# 140389498084928
my_list.remove(2)			
print(id(my_list))			# 140389498084928

# dictionary
my_dict = {"name": "Mariia"}		
print(id(my_dict))			# 140457455135872
my_dict["age"] = 18			
print(id(my_dict))			# 140457455135872

# set
my_set = {1, 2, 3, 4, 5}		
print(id(my_set))			# 140657553430784
my_set.add(6)				
print(id(my_set))			# 140657553430784
```


Also, we can create two different variables of the same id:

```python
first_list = [1, 2, 3]
second_list = first_list		
print(second_list) # [1, 2, 3]

print(id(first_list))	# 140276000714240
print(id(second_list))	# 140276000714240

print(first_list is second_list)	# True
first_list.append(4)

print(first_list)			# [1, 2, 3, 4]
print(second_list)		# [1, 2, 3, 4]

print(first_list is second_list)	# True
print(first_list == second_list)	# True
```


As shown, when the first list was changed, the second list was changed as well. It happened because the two lists are mutable — they share the same memory location and IDs.

Mutable and Immutable Objects in Functions
If you send a mutable object to a function and change it there, it will remain changed after exiting the function. This behavior differs from that of immutable objects, e.g:

```python
my_list = ["apple", "banana"]
my_text = "I love apple"


def add_word(lst: list, text: str, word: str):
	lst.append(word)
	text += word 


# Before function: my_list = ["apple", "banana"], my_text = "I love apple"

add_word(my_list, my_text, "orange")

# Inside function: my_list = ["apple", "banana", "orange"], my_text = "I love appleorange"
# After function: my_list = ["apple", "banana", "orange"], my_text = "I love apple
```
