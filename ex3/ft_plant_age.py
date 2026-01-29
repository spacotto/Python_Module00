def ft_plant_age():
    # Color variables for readability
    green = "\033[1;92m"
    cyan = "\033[1;96m"
    white = "\033[1;97m"
    reset = "\033[0m"
    
    # Ask for age using input() and convert str to int
    age = int(input(f"{white} Enter plant age in days: {reset}"))
    
    # Check if the age is greater than 60 or not
    if age > 60:
        print(f"{green} Plant is ready to harvest!{reset}")
    else:
        print(f"{cyan} Plant needs more time to grow.{reset}")
