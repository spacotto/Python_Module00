def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    # Color variables for readability
    green = "\033[1;92m"
    cyan = "\033[1;96m"
    white = "\033[1;97m"
    reset = "\033[0m"
    
    # Capitalise the first letter of the seed type
    name = seed_type.capitalize()
    
    # Check the unit type to determine the correct message format
    if unit == "packets":
        print(f"{white}", name, f"seeds:{reset}", quantity, "packets available")
    elif unit == "grams":
        print(f"{white}", name, f"seeds:{reset}", quantity, "grams total")
    elif unit == "area":
        print(f"{white}", name, f"seeds: {reset}covers", quantity, "square meters")
    else:
        # Unknown for any unit not specified in the requirements
        print(f" Unknown unit type")
