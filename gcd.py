# Step 1: Define the two numbers
num1 = 56
num2 = 98

# Step 2: Define a function to calculate GCD
def calculate_gcd(a, b):
    while b:
        a, b = b, a % b  # Step 3: Apply Euclidean algorithm
    return a

# Step 4: Calculate and print the GCD
gcd = calculate_gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is: {gcd}")
