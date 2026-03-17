def cal_area(shape, l1, l2=0):
    if(shape == 't'):
        return 0.5*l1*l2
    elif(shape== 'r'):
        return l1*l2
    elif(shape == 's'):
        return l1*l1
    elif (shape == 'c'):
        return 3.14*l1*l1

ch = input("Enter the value of the character of the shape: ")

if(ch == 't' or ch == 'r'):
    l1 = float(input("Enter the value of the first length: "))
    l2 = float(input("Enter the value of the second length: "))
    print(f"The area is {cal_area(ch, l1, l2)}")
elif(ch == 's' or ch == 'c'):
    l1 = float(input("Enter the value of the length: "))
    print(f"The area is {cal_area(ch, l1)}")
else:
    print("Enter a valid character either 't', 'r', 's' or 'c' !!!")