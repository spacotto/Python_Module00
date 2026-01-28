def ft_count_harvest_iterative():
    limit = int(input("Days until harvest: "))
    
    for day in range(1, limit + 1):
        print("Day", day)
        
    print("Harvest time!")
