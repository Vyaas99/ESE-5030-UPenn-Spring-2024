import numpy as np

# Given parameters
alpha = 3
beta = 1
c=2.1093
# Define the target probability density function f(x)
def f(x, alpha, beta):
    return ((alpha + 1) * (alpha + beta + 1) / beta) * (x**alpha) * ((1 - x)**beta)

# Acceptance-rejection algorithm
def acceptance_rejection(alpha, beta, c, n_samples=1000):
    samples = []
    while len(samples) < n_samples:
        u = np.random.uniform(0, 1) # sample from uniform distribution g(x)
        v = np.random.uniform(0, c) # sample from uniform distribution [0, c]
        if v <= f(u, alpha, beta):  # accept-reject criterion
            samples.append(u)
    return np.array(samples)



# Generate the samples
samples = acceptance_rejection(alpha, beta, c)

# Calculate the simulated mean and variance
simulated_mean = np.mean(samples)
simulated_variance = np.var(samples)


print(f"Simulated Mean:{simulated_mean}")
print(f"Simulated Variance:{simulated_variance}")
