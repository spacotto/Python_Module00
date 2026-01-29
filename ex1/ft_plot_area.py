def ft_plot_area():
    # Color variables for readability
    white = "\033[1;97m"
    reset = "\033[0m"

    # Ask for length and width using input()
    # Convert the input strings to integers using int()
    length = int(input(f"{white} Enter length: {reset}"))
    width = int(input(f"{white} Enter width:  {reset}"))

    # Calculate the area
    area = length * width

    # Display the result using print()
    print(f"{white} Plot area:{reset}    {area}")
