# Question_1:
# Write a function to compute 5/0 and use try/except to catch the exceptions.

# Try Block: Giving the code which may through error during run time
try:
   a = 5
   b = 0
   c=a/b
except ZeroDivisionError as zde: # It is handling the error thrown by "try" block
    print("Numerator divide by Zero will give Infinity: ", zde)
else:   # else block will run only when entire try block execute
    print(c)
    

