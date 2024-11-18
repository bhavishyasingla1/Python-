# Step 1: Define the two numbers
num1 = 56
num2 = 98

# Step 2: Define a function to calculate GCD (as it is used in the LCM formula)
def calculate_gcd(a, b):
    while b:
        a, b = b, a % b  # Apply Euclidean algorithm
    return a

# Step 3: Define a function to calculate LCM using the formula
def calculate_lcm(a, b):
    gcd = calculate_gcd(a, b)  # Step 4: Get the GCD
    lcm = abs(a * b) // gcd    # Step 5: Use the LCM formula
    return lcm

# Step 6: Calculate and print the LCM
lcm = calculate_lcm(num1, num2)
print(f"The LCM of {num1} and {num2} is: {lcm}")
