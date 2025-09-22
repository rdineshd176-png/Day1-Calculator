#This is day 1 
#In this day one we build a simple claculator using Python 
while True:
    try:
        num1 = float(input("Enter a Number :" ))   #Get input for num1
        num2 = float(input("Enter a Number :" ))   #Get input for num2
        oper = input("Enter a Operation (+, -, *, /) : ")     #Get input for operation 
        
        if oper == "+":
            ans = num1 + num2   #To add two numbers

        elif oper == "-":
            ans = num1-num2     #To subtract two numbers

        elif oper == "/":
            if num2 == 0:
                print("Error: Cannot divide by 0")
                continue
            ans = num1/num2     #To divide two numbers
        
        elif oper == "*":
            ans = num1*num2     #To multiple two numbers
        
        else:
            print("Invalid operation")      #To print invalid operation if the input is wrong 

        choice = input("Do you want to continue? (y/n): ")
        if choice.lower() != "y":
            break

        print("Answer is :",ans)            #print the answer 
    except ValueError:
        print("Invalid input. Please enter numbers only.")



