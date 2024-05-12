import numpy as np

c=0.0015139
# Define the target probability density function f(x)
def f(x):
    return np.exp(-4*x)+3*x*np.exp(-2*(x**2))

# Acceptance-rejection algorithm
def acceptance_rejection(c, n_samples=1000):
    samples = []
    while len(samples) < n_samples:
        u = np.random.uniform(0, 1) # sample from uniform distribution g(x)
        v = np.random.uniform(0, c) # sample from uniform distribution [0, c]
        if v <= f(u):  # accept-reject criterion
            samples.append(u)
    return np.array(samples)



# Generate the samples
samples = acceptance_rejection(c)

# Calculate the simulated mean and variance
simulated_mean = np.mean(samples)
simulated_variance = np.var(samples)


print(f"Simulated Mean:{simulated_mean}")
print(f"Simulated Variance:{simulated_variance}")