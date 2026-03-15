age = input("Enter your age: ")
have_coupon = input("Do you have a coupon? (yes/no): ")

if have_coupon.lower() != "yes" and have_coupon.lower() != "no":
    print("Please enter 'yes' or 'no' for the coupon question.")
elif age.isdigit():
    age = int(age)
    if age < 18 or age > 65 or have_coupon.lower() == "yes":
        print("You are eligible for a discount.")
    else:
        print("You are not eligible for a discount.")
else:
    print("Please enter a valid number for age.")