import matplotlib.pyplot as plt
import math

# Function to calculate P(n)
def birthday_probability(n):
    if n > 365:
        return 1.0
    return 1 - (math.perm(365, n) / (365 ** n))

# Range of n values (1 to 100)
n_values = range(1, 101)
probabilities = [birthday_probability(n) for n in n_values]

# Create a list of tuples [(n, P(n))]
probability_tuples = list(zip(n_values, probabilities))

# Print the list of tuples
# print("List of (n, P(n)):")
# for n, p in probability_tuples:
#   print(f"({n}, {p:.4f})")

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(n_values, probabilities, marker='o', linestyle='-', color='b', markersize=3)  # Reduced marker size
plt.axhline(y=0.5, color='r', linestyle='--', label='50% Probability')
plt.axvline(x=23, color='g', linestyle='--', label='n = 23')
plt.title('Probability of Shared Birthday as a Function of Group Size (n)', y=1.05)  # Title moved higher
plt.xlabel('Number of People (n)')
plt.ylabel('Probability P(n)')
plt.grid(True)
plt.legend()
plt.show()
