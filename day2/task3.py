def multiplication_table(num):
    big_table = []
    for i in range(num):
        small_table = []
        for j in range(i+1):
            small_table.append((j+1) * (i+1))
        big_table.append(small_table)
    return big_table

val = input("Enter the number plz: ")
if(not val.isdigit()):
    print("Enter a valid number plz !!")
else:
    print(multiplication_table(int(val)))