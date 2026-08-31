# To check whether the given number is an Armstrong Number or not

# Input number
num = int(input("enter any number: "))
original_num = num

# Step 1: Count the number of digits
count = 0
temp = num
while temp > 0:
    temp //= 10
    count += 1
print("Number of digits:", count)

# Step 2: Calculate the sum of digits raised to the power of the count
sum_of_powers = 0
temp = num
while temp > 0:
    digit = temp % 10  # Extract the last digit
    sum_of_powers += digit ** count  # Add the digit raised to the power of count
    temp //= 10  # Remove the last digit

# Step 3: Check if the sum equals the original number
if sum_of_powers == original_num:
    print(f"{original_num} is an Armstrong number.")
else:
    print(f"{original_num} is not an Armstrong number.")

