def ft_count_harvest_iterative():
    # Color variables for readability
    green = "\033[1;92m"
    white = "\033[1;97m"
    reset = "\033[0m"

    # Convert exit condition from str to int
    limit = int(input(f"{white} Days until harvest: {reset}"))

    # for loop
    for day in range(1, limit + 1):
        print(" Day", day)

    print(f"{green} Harvest time!{reset}")
