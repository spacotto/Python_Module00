def ft_harvest_total():
    # Color variables for readability
    white = "\033[1;97m"
    reset = "\033[0m"

    # Each input provided as str is converted to int
    day1 = int(input(f"{white} Day 1 harvest: {reset}"))
    day2 = int(input(f"{white} Day 2 harvest: {reset}"))
    day3 = int(input(f"{white} Day 3 harvest: {reset}"))

    # Sum of 3 inputs
    total = day1 + day2 + day3

    # Display total
    print(f"{white} Total harvest:{reset}", total)
