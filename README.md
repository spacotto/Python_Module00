# Python Module 00: Growing Code, Python Fundamentals Through Garden Data
The main topic of this module is an introduction to **Python's fundamental syntax and semantics**. It focuses on building core programming blocks such as variables, expressions, functions, control flow, and iteration (both loops and recursion). By solving hypothetical and simplified real-world scenarios, like calculating garden plot areas or tracking harvest yields, you develop computational thinking and problem-solving skills while contributing to sustainable community initiatives.

## Instructions
Git clone the repository:
```shell
https://github.com/spacotto/Python_Module00.git
```

### Use functions through `main.py`
Run the main:
```shell
python3 main.py
```

Enter your choice:
```
 ============================================================================
 🌱 Welcome to Growing Code! 🌱
 ============================================================================
 This helper will test your exercises for you.
 Which exercise would you like to test?

 n.  Name                Description
 ----------------------------------------------------------------------------
 0   ft_hello_garden     Say hello to the garden community
 1   ft_plot_area        Calculate garden plot area
 2   ft_harvest_total    Add up harvest weights
 3   ft_plant_age        Check if plant is ready
 4   ft_water_reminder   Check if plants need water
 5   ft_count_harvest    Count days to harvest
 6   ft_garden_summary   Display garden info
 7   ft_seed_inventory   Seed inventory with type hints
 a   -                   Test all exercises

 🌱 Enter your choice: 
```

### Use functions directly in the terminal
Switch to Python terminal:
```shell
python3
```

Import the file and function:
```python
>>> from ex7.ft_seed_inventory import ft_seed_inventory
```

Call the function directly in the main:
```python
>>> ft_seed_inventory("tomato", 15, "packets")
```

## Exercises
### Exercise 0: Hello Garden
* **Function Definition**: Understanding the `def` keyword and basic function structure.
* **Standard Output**: Utilizing `print()` to display strings to the console.
* **String Literals**: Representing text data within code.

### Exercise 1: Garden Plot Area
* **User Input**: Using `input()` to capture data from the user.
* **Type Casting**: Converting string input to integers using `int()` for mathematical operations.
* **Arithmetic Expressions**: Implementing basic multiplication to calculate area ($length \times width$).
* * **Variables**: Storing and manipulating numerical values.

### Exercise 2: Harvest Total
* **Variable Management**: Handling multiple distinct inputs for different variables.
* **Accumulation**: Calculating a total sum from multiple data points.
* **Sequential Logic**: Managing the flow of multiple `input()` and `int()` calls.
  
### Exercise 3: Plant Age Check
* **Comparison Operators**: Using relational operators like `>` to evaluate conditions.
* **Conditional Statements**: Implementing `if/else` logic to branch program execution.
* **Boolean Logic**: Understanding how programs make decisions based on value assessments.

### Exercise 4: Water Reminder
* **Control Flow**: Directing the program to print different messages based on conditional outcomes.
* **Relational Logic**: Testing if a value exceeds a specific threshold (e.g., more than 2 days).

### Exercise 5: Count to Harvest
* **Iteration**: Using `for` loops or `while` loops to repeat actions.
* **Range Function**: Using `range()` to generate a sequence of numbers.
* **Recursion**: Understanding how a function calls itself to solve a repetitive task.
* **Helper Functions**: Implementing nested or separate helper functions to support recursive logic.

### Exercise 6: Garden Summary
* **Data Aggregation**: Combining user input with fixed string constants.
* **String Formatting**: Displaying multiple variables (strings and integers) in a structured summary.

### Exercise 7: Seed Inventory with Type Annotations
* **Type Hinting**: Defining function signatures with explicit types (`str`, `int`, `-> None`).
* **String Methods**: Using built-in methods (e.g., for capitalisation) to format output.
* **Multi-way Branching**: Validating specific string inputs ("packets", "grams", "area") and handling unknown types.
