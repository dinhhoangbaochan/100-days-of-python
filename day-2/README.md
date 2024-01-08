# Python 100 Days - Day 2

## What have I learned in day 2?

### To check a type of a variable
In Python, to check a type of a variable, you could use the `type()` function. Example:

```Python
name = "Chan Dinh"
print( type(name) ) # It should return something like <class 'str'>, which means it's a string
```

### Data Types in Python

#### String
- String is wrapped between a double quote.
- You can access to string's character by using index. For example:

```Python
name = "Chan"
print(name[0]) # Letter C will be printed out
```

### Integer
- Simply a number. For example:

```Python
age = 23
year = 2024
```

### Float
- A number with decimal point.

## Day 2 Challenge

### The instruction

Write a program that will take user input - which is expected to be a 2 digits number. After it's inputted, return a summary of that 2-digits number, by adding first digit with second digit.

For example:
- Input = 35
- Output = 8 (3 + 5)

### My improvement

I add an improvement to the initial instruction. Since the challenge expects the input to be a 2-digits number, if user inputs a more than 2-digits number, the program stops.