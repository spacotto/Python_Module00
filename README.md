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
* **Function Definition:** How to declare a named block of code that performs a specific task.
* **Standard Output:** Using the `print()` function to interact with the user or console.
* **Encapsulation:** Writing code that is contained within a function rather than running as a global script.

### Exercise 1: Garden Plot Area
* **User Input and Type Conversion**: Capturing user data as strings and converting them into integers to allow for mathematical processing.
* **Variable Assignment**: Assigning data to descriptive labels to store and manipulate values throughout the function's execution.
* **Arithmetic Operations**: Applying basic math (multiplication) to variables to solve a specific problem.
* **Sequential Logic and Flow**: Executing a series of instructions in a specific order: collecting inputs, performing a calculation, and then outputting the result.

### Exercise 2: Harvest Total
* **Cumulative Data Collection**: Gathering multiple distinct user inputs to be processed as a related set of data.
* **Arithmetic Summation**: Utilizing the addition operator to aggregate multiple numerical variables into a single total.
* **Variable Initialization and Update**: Managing multiple variables to store sequential data points before performing a final calculation.
* **Data Flow Management**: Handling the progression of data from individual inputs to a processed aggregate output.
  
### Exercise 3: Plant Age Check
* **Conditional Logic**: Using if-else statements to allow the program to make decisions and execute different code paths based on specific criteria.
* **Comparison Operators**: Utilizing relational operators (such as greater than) to evaluate the relationship between two values.
* **Boolean Evaluation**: Understanding how expressions resolve to True or False to control the flow of a program.
* **Dynamic Output**: Generating different string responses based on the state of the data being processed.

### Exercise 4: Water Reminder
* **Binary Branching**: Implementing a logic structure that chooses between exactly two distinct outcomes based on a single condition.
* **Relational Comparison**: Using comparison operators to evaluate if a variable exceeds a specific threshold (in this case, 2).
* **Control Flow**: Directing the execution of code based on real-time user input to provide contextually relevant responses.
* **Data-Driven Decision Making**: Using stored numerical data to automate a recommendation or alert system.

### Exercise 5: Count to Harvest
* **Iteration**: Using loops (such as `for` with the `range()` function) to repeat a specific block of code a set number of times.
* **Recursion**: Implementing a process where a function calls itself to solve a problem by breaking it down into smaller sub-problems.
* **Base Cases and Stop Conditions**: Understanding how to define a termination point in a recursive function to prevent infinite execution.
* **Helper Functions**: Utilizing nested or separate helper functions to manage state and logic, particularly within recursive implementations.
* **Algorithmic Equivalence**: Demonstrating how the same logical outcome can be achieved using two fundamentally different programming paradigms.

### Exercise 6: Garden Summary
* **Multi-type Data Handling**: Managing and processing different data types, such as strings for names and integers for quantities, within a single logical unit.
* **String Concatenation and Formatting**: Combining user-provided variables with static text labels to create structured, human-readable output.
* **Input Synchronization**: Orchestrating multiple sequential user prompts to collect a complete dataset before processing.
* **Fixed vs. Dynamic Output**: Distinguishing between dynamic data (user inputs) and static constants (fixed status messages) in a program's output.

### Exercise 7: Seed Inventory with Type Annotations
* **Type Annotations**: Using type hints in function signatures to explicitly define the expected data types for parameters and return values.
* **String Manipulation**: Applying string methods to format text, such as capitalizing the first letter of a word for professional output.
* **Conditional Branching with Multiple Cases**: Implementing logic that evaluates a variable against several specific string values to determine the correct output format.
* **Function Arguments and Parameters**: Defining and passing multiple positional arguments to a function to perform data-driven tasks.
* **Default Error Handling**: Providing a fallback or "catch-all" output for unrecognized or unsupported input types.
