#!/usr/bin/env python3
def print_fibonacci(length):
    if length <= 0:
        return []  
    elif length == 1:
        return [0] 
    elif length == 2:
        return [0, 1]  
    
    fibonacci_sequence = [0, 1] 
    while len(fibonacci_sequence) < length:
        next_value = fibonacci_sequence[-1] + fibonacci_sequence[-2]  
        fibonacci_sequence.append(next_value)  
    return fibonacci_sequence

