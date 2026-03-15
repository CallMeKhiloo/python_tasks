num = input("Enter a number: ")

start = input("Enter your start: ")
end = input("Enter your end: ")

if num.isdigit() and start.isdigit() and end.isdigit():
    num = int(num)
    start = int(start)
    end = int(end)

    if start <= num <= end:
        print(f"{num} is between {start} and {end}.")
    else:
        print(f"{num} is not between {start} and {end}.")
else:
    print("Please enter valid numbers for num, start, and end.")