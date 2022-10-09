# Loop for that prints numbers from 1 to 100
for fizzbuzz in range(1,101):
 
 # Prints FizzBuzz in place of numbers 
    # divisible by 15
    if fizzbuzz % 15 == 0:
        print("FizzBuzz")                                        
        continue
 
 # Prints Buzz in place of numbers 
    # divisible by 5
    elif fizzbuzz % 5 == 0:        
        print("Buzz")                                    
        continue

    # Prints Fizz in place of numbers 
    # divisible by 3
    elif fizzbuzz % 3 == 0:    
        print("Fizz")                                        
        continue

    # Print numbers
    print(fizzbuzz)