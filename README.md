# Python Module 00
An introduction to Python fundamentals through community garden data analysis. This module teaches **basic syntax** and **semantics**, including **expressions**, **variables**, **functions**, and **control flow** through practical, real-world (sort of) exercises.

## Exercise 0, Hello Garden: Function Definition and `print`
### Functions
A **function** is a **reusable block of code that performs a specific task**. 

**Syntax:**
```python
def function_name(parameters):
    # function body
```

**Key concepts:** 
- Functions are defined using the `def` keyword.
- Function names should be descriptive and follow `snake_case` convention.
- The colon `:` indicates the start of the function body.
- **Indentation** (4 spaces) defines the function's scope.

### `print()` Function
**The `print()` function** outputs text to the console. It takes one or more arguments and displays them.

## Exercise 1, Garden Plot Area: Variables and User Input
**Variables** store data values that can be referenced and manipulated throughout your program. Python uses dynamic typing, meaning **you don't need to declare variable types explicitly**.

**The `input()` function** reads user input from the console as a **string**.

**Type conversion** using `int()` converts string data to integers for mathematical operations.

**Key concepts:**
- Variables are created by assignment: `variable = value`
- `input()` **always returns a string**, regardless of what the user types
- `int()` **converts strings to integers** for arithmetic operations
- Basic arithmetic operators: `+`, `-`, `*`, `/`
- Variables can store the results of calculations

## Exercise 2, Harvest Total: Arithmetic Operations and Accumulation
**Arithmetic operations** perform mathematical calculations on numeric values. 
**Accumulation** is the pattern of collecting or summing values over multiple steps.

**Key concepts:**
- Multiple variables can store different values simultaneously
- Values can be added together using the `+` operator
- Results can be stored in new variables
- Sequential operations build upon previous results
- Variables can be reused and updated throughout the program

## Exercise 3, Plant Age Check: Conditional Statements
**Conditional statements** allow programs to make decisions and execute different code based on conditions.
**Comparison operators** evaluate relationships between values, returning boolean results (`True` or `False`).

**Key concepts:**
- `if` statements execute code only when a condition is True
- `else` provides an alternative path when the condition is False
- Comparison operators: `>` (greater than), `<` (less than), `>=`, `<=`, `==`, `!=`
- Indentation defines which code belongs to each branch
- Programs can respond differently based on input values

## Exercise 4, Water Reminder: Boolean Logic and Conditionals
**Boolean logic** deals with True/False values and conditions that evaluate to these states.
**Conditional branching** directs program flow based on boolean evaluations.

**Key concepts:**
- Conditions evaluate to boolean values (True or False)
- `if`/`else` structures create decision points in code
- Comparison operators return boolean results
- Different messages can be displayed based on conditions
- Logical flow allows programs to respond appropriately to different scenarios

## Exercise 5, Count to Harvest: Iteration and Recursion
**Iteration** repeats a block of code multiple times using loops. The `for` loop iterates over a sequence of values.
**Recursion** is when a function calls itself to solve a problem by breaking it into smaller instances of the same problem.
**The `range()` function** generates a sequence of numbers, commonly used with loops.

**Key concepts:**
- **Iteration (loops):** Use `for` with `range()` to repeat code a specific number of times
- **Recursion:** A function can call itself with modified parameters
- Both approaches can solve the same problem differently
- Loops are often more intuitive for counting or repeating actions
- Recursion requires a base case to stop the function from calling itself infinitely
- Helper functions can be defined inside or outside the main function for recursion

## Exercise 6, Garden Summary: String Formatting and Output
**String concatenation** combines multiple strings or values into a single output.
**Formatted output** presents data in a structured, readable format.

**Key concepts:**
- Multiple pieces of information can be displayed together
- `print()` can output strings and variables
- Information can be organized into clear, formatted displays
- Combining user input with fixed text creates meaningful output
- Well-formatted output improves program usability and readability

## Exercise 7, Seed Inventory with Type Annotations: Function Parameters and Type Hints
**Function parameters** allow functions to accept input values and operate on them.
**Type annotations** explicitly document the expected types of function parameters and return values, improving code readability and enabling better tooling support.
**String methods** are built-in functions that perform operations on string objects.

**Key concepts:**
- Parameters are defined in the function signature: `def func(param1, param2):`
- Type hints specify expected types: `param: str`, `param: int`
- Return type annotations use `-> Type` syntax
- `-> None` indicates a function doesn't return a value
- String methods like `.capitalize()` or `.title()` transform text
- Parameters make functions flexible and reusable with different inputs
- Type annotations serve as documentation and help catch errors early

# Resources
- [Python 3.14.2 documentation](https://docs.python.org/3/)
- [Python Functions](https://www.w3schools.com/python/python_functions.asp)
