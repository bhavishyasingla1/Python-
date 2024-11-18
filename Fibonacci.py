# Step 1: Define the number of terms in the sequence
n_terms = 10  # Number of Fibonacci numbers to generate

# Step 2: Initialize the first two terms
n1, n2 = 0, 1
count = 0  # Counter for the loop

# Step 3: Check if the number of terms is valid
if n_terms <= 0:
    print("Please enter a positive integer.")
elif n_terms == 1:
    print(f"Fibonacci sequence up to {n_terms}:")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count < n_terms:
        print(n1)  # Print the current term
        nth = n1 + n2  # Step 4: Calculate the next term
        # Update values for the next iteration
        n1 = n2
        n2 = nth
        count += 1
