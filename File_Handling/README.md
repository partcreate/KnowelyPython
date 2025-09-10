Ja, ich kann den bereitgestellten HTML-Code in Markdown konvertieren. Hier ist das Ergebnis, das du direkt in eine `README.md`-Datei kopieren kannst.

-----

[ ](https://www.google.com/search?q=%23file-handling)

# File Handling

Whenever long-term data storage is needed, files are used; they prove particularly handy for recording data on programs run regularly. They're used for logging their start, proper function, or errors. However, as future developers, we shouldn’t limit ourselves to *saving* data only. There’s so much to be done with files, and we’ll discuss all the possibilities today.

[ ](https://www.google.com/search?q=%23opening-modes)

### Opening Modes

Before working with a file, we need to open it using the built-in `open()` method, with the file path — and the opening mode — specified in parentheses. If we don’t specify the mode, it will open in the **default `r` mode,** where `r` stands for `reading`. There are a few modes:

  - `r` reads the file, and returns an error if it doesn’t exist.
  - `w` writes data to a file; if the file exists, it overwrites it, otherwise creates a new one.
  - `a` appends data to a file; if the file doesn't exist, it creates a new one.
  - `x` writes data to a file and returns an error if the file already exists (exclusive creation).
  - `t` is used for text files (text mode — we see the text).
  - `b` is used for binary files, such as images or videos (binary mode — we see `0` and `1`).
  - `+` allows both reading and writing to the file simultaneously.

To give an example, let’s consider an "errors.txt" file that contains the following data:

```
10:53 12/09/2022 too many requests
21:17 13/09/2022 user admin not found
```

We can open this file as follows:

```python
file = open("errors.txt")
```

Here, the file was opened in the default `r` mode since no mode was specified. Now let's open this file in **read** mode:

```python
file = open("errors.txt", "r")
```

There’s no difference since the **read mode is the default one.**

-----

[ ](https://www.google.com/search?q=%23closing)

### Closing

Imagine we have a large project that frequently writes to a file, and we forget to close it. The program continues to run and write unnecessary data, eventually filling the file and occupying a large amount of memory — which can lead to system errors. We can avoid this by closing the file with the built-in `close()` method:

```python
file = open("errors.txt", "r")
file.close() # Here we closed the file
```

-----

[ ](https://www.google.com/search?q=%23reading)

### Reading

To read the entire file into one variable, we use the `read()` method:

```python
file = open("errors.txt", "r")

print(file.read())
# 10:53 12/09/2022 too many requests
# 21:17 13/09/2022 user admin not found

file.close() # And do not forget to close your file
```

If we pass a numeric argument to the `read()` method, it will return the specified number of characters from the file:

```python
file = open("errors.txt", "r")
print(file.read(10)) 	# 10:53 12/0
file.close()
```

To start reading from a position other than the beginning of the file, use the `seek()` method and specify the number of bytes to skip:

```python
file = open("errors.txt", "r")

file.seek(10)
print(file.read())
# 9/2022 too many requests
# 21:17 13/09/2022 user admin not found

file.close()
```

To read a file line by line, use a loop with the `readline()` or `readlines()` method. The `readline()` method returns one line at a time, while `readlines()` returns all lines as a list, with each element being a line in the file. For example:

```python
file = open("errors.txt", "r")

print("Readline method working")
print(file.readline())

file.close()
```

In the console, we’ll see:

```
Readline method working
10:53 12/09/2022 too many requests
```

Here’s the `readlines()` method in action:

```python
file = open("errors.txt", "r")

line_number = 1 		# Variable for seeing the number of a line 
print("Readlines method working")
for line in file.readlines():
    print(f"Line number {line_number}")	
    print(line)
    line_number += 1

file.close()
```

In the console, we’ll see:

```
Readlines method working
Line number 1
10:53 12/09/2022 too many requests
Line number 2
21:17 13/09/2022 user admin not found
```

An advantage of these methods is that they manage memory efficiently by reading only one line at a time — unlike the `read()` method which reads the whole file. This lets us process even large files line by line. Another way to read line by line is to iterate over the file using a `for` loop:

```python
file = open("errors.txt", "r")

line_number = 1 		# Variable for seeing the number of a line 
for line in file:
    print(f"Line number {line_number}")	
    print(line)
    line_number += 1

file.close()
```

In the console, we’ll see:

```
Line number 1
10:53 12/09/2022 too many requests
Line number 2
21:17 13/09/2022 user admin not found
```

-----

[ ](https://www.google.com/search?q=%23writing-and-appending)

### Writing and Appending

To write information to a file, we use the `w` (write) mode that creates a new file — if it doesn't exist — or overwrites an existing file. The built-in `write()` method is one way to write information to a file; it accepts only strings as arguments:

```python
file = open("errors.txt", "w")
file.write("17:00 14/09/2022 value error")

file.close()
```

"errors.txt" now contains the string "17:00 14/09/2022 value error" which overwrites the old information. If we’d like to append data *without* losing the existing information, we can open the file in the `a` (append) mode which either creates the file (if it doesn't exist) or appends new data. Let’s combine it with the `write()` method — to write to the file:

```python
file = open("errors.txt", "a")
file.write("17:00 14/09/2022 value error")

file.close()
```

In the console, we’ll see:

```
10:53 12/09/2022 too many requests
21:17 13/09/2022 user admin not found
17:00 14/09/2022 value error
```

These examples illustrate the difference between the write and append modes. In the first example, the existing information is replaced with new information. In the second example, the new information is added to the end of the file, preserving the existing content.

-----

[ ](https://www.google.com/search?q=%23context-managers-in-files)

## Context Managers in Files

If we forget to close a file after opening it, we might cause issues, which Python can prevent with context managers. Using the `with` statement, context managers automatically close the file when exiting the scope, for example:

```python
# Solution 1

file = open("errors.txt", "r")
# Some actions with file
file.close()


# Solution 2

with open("errors.txt", "r") as file:
	# Some actions with file
```

In both solutions, the file is opened and closed, but the second case is more elegant, takes up less space, and guarantees the file will be closed even if forgotten. Also if an error occurs\! For example, this file will be closed:

```python
with open("errors.txt", "w+") as file:
	file.read()
    file.write(1/0)
```

Context managers don’t work with files only, but we'll cover the alternative use cases later on. The main points to remember when working with context managers are:

1.  A context manager always contains two special methods: `__enter__` and `__exit__`.
2.  The `__enter__` method returns an object assigned to a variable after the `as` keyword. The default value is `None` and it is optional.
3.  If an error occurs in `__init__` or `__enter__`, the code block is never executed, and `__exit__` is not called.
4.  After entering a block of code, `__exit__` is always called, even if an exception occurs.

Here’s a context manager structure:

```python
class CustomContextManager():
    def __init__(self):
        pass

    def __enter__(self):
        pass

    def __exit__(self):
        pass

    def __del__(self):
        pass
```