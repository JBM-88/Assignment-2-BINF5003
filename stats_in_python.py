import sys
import math

def load_data(filepath:str, column:int)->tuple[list, int]:
    # TODO - Complete the function so it loads the data from the file into a list
    # The function returns a tuple that contains the list of values and the total number 
    # of values in the column
    
    values_of_data_list = []
    
    with open (filepath, "r") as file:
        for line in file:
            columns = line.strip().split(",")
            values_of_data_list.append(columns[column])
        
    return values_of_data_list, len(values_of_data_list)

def calculate_average(numbers:list)->float:
    # TODO - Complete the function to return the average of the list of numbers
    
    if len(numbers) == 0:
        return 0.0
        
    return sum(numbers)/len(numbers)

def get_max_and_min(numbers:list)->tuple[float, float]:
    # TODO - Complete the function to return a tuple with the maximum and minimum
    # values in the list, in that order
    
    maximum = float(max(numbers))
    minimum = float(min(numbers))
    return maximum, minimum

def calculate_variance(numbers:list)->float:
    # TODO - Complete the function to return the variance of the numbers in the list
    
    if len(numbers) <= 1:
        return 0.0

    mean = sum(numbers)/len(numbers)
    
    deviation = []
    square_deviation = []
    
    for num in numbers:
        deviation_value = num - mean
        deviation.append(deviation_value)
    
    for n in deviation:
        square_deviation_value = math.pow(n, 2)
        square_deviation.append(square_deviation_value)
        
    mean_of_square_deviation = sum(square_deviation)/(len(square_deviation) -1)
        
    return mean_of_square_deviation

def calculate_std_dev(numbers:list)->float:
    # TODO - Complete the function to return the standard deviation of the numbers in the list
    
    if len(numbers) <= 1:
            return 0.0

    mean = sum(numbers)/len(numbers)
    
    deviation = []
    square_deviation = []
    
    for num in numbers:
        deviation_value = num - mean
        deviation.append(deviation_value)
    
    for n in deviation:
        square_deviation_value = math.pow(n, 2)
        square_deviation.append(square_deviation_value)
        
    mean_of_square_deviation = sum(square_deviation)/(len(square_deviation) -1)
    
    standard_deviation = float(math.sqrt(mean_of_square_deviation))
        
    return standard_deviation

def calculate_median(number:list)->float:
    # TODO - Complete the function to return the median of the numbers in the list
    number.sort()
    n = len(number)
    
    if n % 2 == 1:
        middle = n//2
        median = number[middle]
        
    else:
        middle_1 = (n//2) - 1
        middle_2 = n//2
        median = (number[middle_1] + number[middle_2])/2
        
    return float(median)


