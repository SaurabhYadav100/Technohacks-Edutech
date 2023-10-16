print("\n-----------------------------------------------------------------------")
print("                              CALCULATOR                           ")
print("-----------------------------------------------------------------------")
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
def calculator():
    print("\n 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n 5. Exit")
    while True:
        n=int(input("\nEnter the choice:")) 
        if n<5 and n>0:
            x=eval(input("Enter the first number:"))
            y=eval(input("Enter the second number:"))  
            if n==1:
                print(f"The addition of {x} and {y} is",add(x,y))
            elif n==2:
                print(f"The subtraction of {x} and {y} is",subtract(x,y))
            elif n==3:
                print(f"The multiplication of {x} and {y} is",multiply(x,y))       
            elif n==4:
                if y==0:
                    print("Can't divide by zero")
                else:
                    print(f"The division of {x} by {y} is",divide(x,y))    
        elif n==5:
            print("Thank You!")
            exit()
        else:
            print("Invalid choice")
calculator()