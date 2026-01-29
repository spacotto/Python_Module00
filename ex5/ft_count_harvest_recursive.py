def ft_count_harvest_recursive(current=1, limit=None):
    # Color variables for readability
    green = "\033[1;92m"
    white = "\033[1;97m"
    reset = "\033[0m"
    
    # Initialisation: Only happens on the very first call
    if limit is None:
        limit = int(input(f"{white} Days until harvest: {reset}"))
    
    # Exit condition
    if current > limit:
        print(f"{green} Harvest time!{reset}")
        return

    # Print the current day
    print(" Day", current)
    
    # Recursion: 'current' becomes 'current + 1', 'limit' stays the same
    ft_count_harvest_recursive(current + 1, limit)
