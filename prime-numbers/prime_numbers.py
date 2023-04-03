#taking input from the user
num = int(input("Enter any number: "))

#if number entered is less than or equal to 1
#then the print is not a prime number
if num <= 1 :
       print(num, "Is Not a Prime Number.")

# prime number is always greater than 1
elif  num> 1 :
    for x in range(2, num):
        
        if(num % x) == 0:
                print(num, "Is Not a Prime Number.")
                break

        else:
                print(num, "Is a Prime Number.")

