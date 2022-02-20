print("Please enter your name here: ")
name = input()
print(f"Welcome {name}, please enter your choices: ")

x = ""
while(x !='q'):
    print("Enter the operation you want to perform 1. Addition\n 2.Subration\n 3.Multiply\n 4.Division\n 5.Modulus.")
    b = input()
    if b == "1":
        print("Enter the operands in the format op1 op2: ")
        a,c = map(int, input().split(" "))
        print(a+c)
    elif b == "2":
        print("Enter the operands in the format op1 op2: ")
        a,c = map(int, input().split(" "))
        print(a-c)
    elif b == "3":
        print("Enter the operands in the format op1 op2: ")
        a,c = map(int, input().split(" "))
        print(a*c)
    elif b == "4":
        print("Enter the operands in the format op1 op2: ")
        a,c = map(int, input().split(" "))
        if c == 0:
            print("b cannot be 0")
        else:
            print(a/c)
    elif b == "5":
        print("Enter the operands in the format op1 op2: ")
        a,c = map(int, input().split(" "))
        print(a%c)
    else:
        print("Invalid Operation")
    print("press q to quit or to continue press any key: ")
    x = input()
    
