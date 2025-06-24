# List and Dict Comprehensions
Comprehensions are a convenient and concise option of creating a list or a dict.

## List Comprehension
List comprehension is considerably faster than processing a list using a for loop. It provides a shorter syntax for creating a new list based on the values of any iterable object:

```python
result = [expression for element in iterable]
```


where:

iterable is the object we iterate over;
element is the value from iterable at each step;
expression is the modified element from iterable objects, which will be written to the result list;
result is the newly created list.
Let's consider some examples of list comprehension:


```python
squared_list = [i ** 2 for i in range(5)]		# [0, 1, 4, 9, 16]
upper_letters = [char.upper() for char in "Hello!"]		# ["H", "E", "L", "L", "O", "!"]
double_list = [item * 2 for item in [1, 3, 5, 7]]		# [2, 6, 10, 14]
tuple_values = [fruit for fruit in ("apple", "banana", "orange")]	# ["apple", "banana", "orange"]
```


Let’s compare two different ways to create a list, one using the tried for loop, and one — using the list comprehension. Every element of the list should be double in value. First up, the loop:
```python
input_list = [1, 5, 3, 21]
double = []

for item in input_list:
	double.append(item * 2)

print(double)	# [2, 10, 6, 42]
```


Second up, list comprehension:
```python
input_list = [1, 5, 3, 21]
double = [item * 2 for item in input_list]	# [2, 10, 6, 42]
```


…and since there is no such thing as too many examples, here are two more. In the first one, list comprehensibility is a much better choice in terms of code readibility. In the second example, the for loop is enough:

- age < 3 — Baby;
- 3 <= age < 10 — Child;
- 10 <= age < 18 — Teenager;
- age >= 18 — Adult.

```python
people = [
    {"name": "Ivan", "age": 18}, 
    {"name": "Mariia", "age": 20}, 
    {"name": "Dariia", "age": 15}
]

# First example
result_1 = []
for person in people:
	if person["age"] >= 18:
		result_1.append(person["name"])


result_2 = [person["name"] for person in people if person["age"] >= 18]

# result_1 = result_2 = ["Ivan", "Mariia"]

# Second example
result_1 = []
for person in people:
    if person["age"] < 3:
        result_1.append({person["name"]: "Baby"})
    elif 3 <= person["age"] < 10:
        result_1.append({person["name"]: "Child"})
    elif 10 <= person["age"] < 18:
        result_1.append({person["name"]: "Teenager"})
    else:
        result_1.append({person["name"]: "Adult"})

result_2 = [
   {person["name"]: "Baby"} if person["age"] < 3
   else {person["name"]: "Child"}
   if 3 <= person["age"] < 10
   else {person["name"]: "Teenager"}
   if 10 <= person["age"] < 18
   else {person["name"]: "Adult"}
   for person in people
]
 

# result_1 = result_2 = [{"Ivan": "Adult"}, {"Mariia": "Adult"}, {"Dariia": "Teenager"}]
```


## Conditionals in List Comprehension
List comprehension lets us specify a condition for elements that must be included in a new list:

```python
result_1 = [expression for element in iterable if condition]
result_2 = [expression if condition else default_expression for element in iterable]
```


…where:

condition is a condition under which the value is added to the list.
default_expression is a value added to the list if the condition isn’t met.
For example:

```python
odd_numbers = [num for num in range(10) if num % 2 == 1]		# [1, 3, 5, 7, 9]
short_words = [word for word in ("abc", "abcabc", "a") if len(word) <= 3]	# ["abc", "a"]
odd_numbers_or_0 = [num if num % 2 == 1 else 0 for num in range(10)]	
# [0, 1, 0, 3, 0, 5, 0, 7, 0, 9]
```
