import numpy as np



# Probabilities and corresponding times for the heater run time and between call times
run_time_probs = np.array([0.05, 0.10, 0.15, 0.20, 0.20, 0.15, 0.10, 0.05])
run_times = np.arange(1, 9)

between_call_probs = np.array([0.10, 0.15, 0.25, 0.25, 0.15, 0.10])
between_call_times = np.arange(1, 7)

# Probabilities and corresponding times for coil replacement
replacement_time_probs = np.array([0.2, 0.5, 0.3])
replacement_times = np.array([1, 2, 3])

# Heater failure probability
failure_probability = 0.4

# Simulation time (in minutes) - 50 hours converted to minutes
simulation_time = 50 * 60

# Counters for the simulation results
number_of_calls = 0
number_of_replacements = 0

# Current time in the simulation
current_time = 0

while current_time < simulation_time:
    # Heater is called 
    number_of_calls += 1

    # Determine if the coil fails when it is called 
    coil_fails = np.random.random() < failure_probability

    if coil_fails:
        # Coil needs to be replaced, keeping count
        number_of_replacements += 1
        # Determine replacement time based on the replacement time distribution
        replacement_time = np.random.choice(replacement_times, p=replacement_time_probs)
        # Add the replacement time to the current time
        current_time += replacement_time
    else:
        # Coil doesn't fail, determine run time based on the run time distribution
        run_time = np.random.choice(run_times, p=run_time_probs)
        # Add the run time to the current time
        current_time += run_time

    # Determine between call time based on the between call time distribution
    between_call_time = np.random.choice(between_call_times, p=between_call_probs)
    # Add the between call time to the current time
    current_time += between_call_time

print("Number of times heater had to be called:",number_of_calls)
print("Number of times heater had to be repaired:", number_of_replacements)

