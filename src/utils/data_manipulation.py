# data_manipulation.py

def calculate_average(lst):
    if not lst:
        return 0
    
    total = sum(lst)
    average = total / len(lst)
    return average
