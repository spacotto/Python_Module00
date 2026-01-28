def ft_count_harvest_recursive():
    limit = int(input("Days until harvest: "))
    
    def count_up(current_day, max_day):
        if current_day <= max_day:
            print("Day", current_day)
            count_up(current_day + 1, max_day)
            
    count_up(1, limit)
    print("Harvest time!")
