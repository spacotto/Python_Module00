# Python Module 00
An introduction to Python fundamentals through community garden data analysis. This module teaches **basic syntax** and **semantics**, including **expressions**, **variables**, **functions**, and **control flow** through practical, real-world (sort of) exercises.

## Exercise 0: Hello Garden
- [Function definition](https://github.com/spacotto/grimoire/blob/main/python/fn_definition.md)
- [`print` function](https://github.com/spacotto/grimoire/blob/main/python/print.md)

## Exercise 1, Garden Plot Area:
- [Variables](https://github.com/spacotto/grimoire/blob/main/python/variable.md)
- Data Types
- [`input()` function](https://github.com/spacotto/grimoire/blob/main/python/input.md)

## Exercise 2: Harvest Total
-
  
## Exercise 3, Plant Age Check: Conditional Statements
-

## Exercise 4, Water Reminder: Boolean Logic and Conditionals
-

## Exercise 5, Count to Harvest: Iteration and Recursion
Both iteration and recursion can solve the same problem differently.

### Iteration
**Iteration** repeats a block of code multiple times using loops. The `for` loop iterates over a sequence of values.

**Key concepts:**
- **Iteration (loops):** Use `for` with `range()` to repeat code a specific number of times
- Loops are often more intuitive for counting or repeating actions

### Recursion
**Recursion** is when a function calls itself to solve a problem by breaking it into smaller instances of the same problem.
**The `range()` function** generates a sequence of numbers, commonly used with loops.

In this case, various approaches are acceptable:
1. Using a **nested helper function** inside your main function:
```python
def ft_count_harvest_recursive():
    limit = int(input("Days until harvest: "))

    def helper(current):
        if current <= limit:
            print("Day", current)
            helper(current + 1) # Recursive step

    helper(1)
    print("Harvest time!")
```

2. Using **default parameter values**:
```python
def harvest_logic(current, limit):
    if current <= limit:
        print("Day", current)
        harvest_logic(current + 1, limit)

def ft_count_harvest_recursive():
    limit = int(input("Days until harvest: "))
    harvest_logic(1, limit)
    print("Harvest time!")
```

3. Using a **separate helper function** called by your main function:
```python
def ft_count_harvest_recursive(current=1):
    # This part only runs the very first time (when current is 1)
    if current == 1:
        # Note: This approach is tricky if we need a user-defined limit 
        # because the input() would trigger every time the function restarts.
        # To make it work for this specific prompt, we use a global-style logic:
        limit = 5 # Example fixed limit to show the default parameter style
        # (For dynamic limits, Approach 1 or 2 is much better!)
        
    # Standard recursion logic
    if current <= 5: 
        print("Day", current)
        ft_count_harvest_recursive(current + 1)
    else:
        print("Harvest time!")
```

| Approach | Best for... | Why? |
| :--- | :--- | :--- |
| Nested Helper | Cleanliness | "Keeps the ""internal"" counting variable hidden from the outside world." |
| Separate Helper | Reusability | Allows other functions in your program to use the same counting logic. |
| Default Params | Briefness | "Reduces the number of functions defined, but can be confusing for complex logic." |

**Key concepts:**
- **Recursion:** A function can call itself with modified parameters
- Recursion requires a base case to stop the function from calling itself infinitely
- Helper functions can be defined inside or outside the main function for recursion

## Exercise 6, Garden Summary: String Formatting and Output
-

## Exercise 7, Seed Inventory with Type Annotations: Function Parameters and Type Hints
-
