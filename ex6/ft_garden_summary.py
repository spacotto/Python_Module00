def ft_garden_summary():
    # Color variables for readability
    green = "\033[1;92m"
    cyan = "\033[1;96m"
    white = "\033[1;97m"
    reset = "\033[0m"
    
    # Variable that stores input str "name"
    name = input(f"{white} Enter garden name: {reset}")
    
    # Variable that stores input str "plants" (no need to convert to int)
    plants = input(f"{white} Enter number of plants: {reset}")
    
    # Print summary: variables + fixed status message
    print(f"{white} Garden:{reset}", name)
    print(f"{white} Plants:{reset}", plants)
    print(f"{green} Status: Growing well!{reset}")

