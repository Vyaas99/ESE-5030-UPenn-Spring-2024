import numpy as np


n = 10  # number of customers
lambda_inv = 5  # 1/λ = 5 minutes 
theta = 0.8  # separation time
runs = 1000  # number of simulation runs

# Theoretical probability
lambda_param = 1 / lambda_inv
theoretical_probability = np.exp(-(n-1) * lambda_param * theta)

# Simulation
successes = 0
for _ in range(runs):
    # Generate n interarrival times
    interarrival_times = np.random.exponential(lambda_inv, n)
    # Check if all interarrival times are greater than theta
    if all(t > theta for t in interarrival_times[1:]):
        successes += 1
simulated_probability = successes / runs

print(f"Simulated Probability:{simulated_probability}")
print(f"Theoretical Probability:{theoretical_probability}")
