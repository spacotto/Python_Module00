def ft_plot_area():
    try:
        length = int(input("Enter the length of the plot: "))
        width = int(input("Enter the width of the plot: "))        
        area = length * width
        print(f"The total area of the plot is: {area}")
    except ValueError:
        print("Error: Please enter valid numerical values for length and width.")
