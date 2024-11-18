# Step 1: Define the two numbers
num1 = 56
num2 = 98

# Step 2: Define a function to calculate HCF
def calculate_hcf(a, b):
    while b:
        a, b = b, a % b  # Step 3: Apply Euclidean algorithm
    return a

# Step 4: Calculate and print the HCF
hcf = calculate_hcf(num1, num2)
print(f"The HCF of {num1} and {num2} is: {hcf}")
