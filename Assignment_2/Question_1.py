#Assignment 2:
    
# Question 1

# Creating a below pattern using Nested for loop    



for i in range(0,5):
    for j in range(0,i+1):
        print("*",end=" ")
    print("\r")
    
for i in range(5,0,-1):
    for j in range(0,i-1):
        print("*",end=" ")
    print("\r")