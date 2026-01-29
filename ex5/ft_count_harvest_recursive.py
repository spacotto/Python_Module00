# Helper function
def harvest_helper(current, limit):
    if current > limit:                 # Exit condition
        return
    print(" Day", current)
    harvest_helper(current + 1, limit)


def ft_count_harvest_recursive():
    # Color variables for readability
    green = "\033[1;92m"
    white = "\033[1;97m"
    reset = "\033[0m"

    limit = int(input(f"{white} Days until harvest: {reset}"))
    harvest_helper(1, limit)
    print(f"{green} Harvest time!{reset}")
