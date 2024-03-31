import numpy as np

# Simulation parameters
num_simulations = 10000
time_interval = 5  # hours
expected_females_40_60 = 14  # per hour
total_females_40_60_in_5hrs = expected_females_40_60 * time_interval
count_more_than_80 = 0

# Run simulations
for _ in range(num_simulations):
    # Simulate the number of females between 40 and 60 arriving in 5 hours
    females_40_60_arrivals = np.random.poisson(total_females_40_60_in_5hrs)
    # Count how many times more than 80 females between 40 and 60 arrive
    if females_40_60_arrivals > 80:
        count_more_than_80 += 1

# Calculate the simulated probability
simulated_prob_more_than_80 = count_more_than_80 / num_simulations
print(simulated_prob_more_than_80)
