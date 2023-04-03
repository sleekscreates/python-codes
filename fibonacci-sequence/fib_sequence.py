 # Declare function for an  nth fibonacci
def Fibonacci(n):

 # Checks whether input is less than 0 then
   # Prints Invalid input
    if n < 0:
        print("Invalid input")

    # checks if n = 0
    # then it returns 0
    elif n == 0:
        return 0 
 
    # checks whether n is 1,2
    # then it returns 1,2 
    elif n == 1 or n == 2:
        return 1 
 
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
        

print(Fibonacci(7)) 
