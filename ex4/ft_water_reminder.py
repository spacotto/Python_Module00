def ft_water_reminder():
    # Color variables for readability
    green = "\033[1;92m"
    cyan = "\033[1;96m"
    white = "\033[1;97m"
    reset = "\033[0m"
    
    # Ask for days using input() and convert str to int
    days = int(input("Days since last watering: "))
    
    # Check if the number of days is greater than 2
    if days > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
