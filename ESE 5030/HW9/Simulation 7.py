import numpy as np
from scipy.stats import truncnorm

# Set the number of customers
num_customers = 2000

# Define function to generate truncated normal data
def truncated_normal(mean, std, lower, upper, size):
    a, b = (lower - mean) / std, (upper - mean) / std
    return truncnorm.rvs(a, b, loc=mean, scale=std, size=size)

# Generate interarrival times: N(3, 4) truncated at 0 and 5
interarrival_times = truncated_normal(3, 2, 0, 5, num_customers)

# Generate service times: N(2, 4) truncated at 0 and 4
service_times = truncated_normal(2, 2, 0, 4, num_customers)

# Initialize simulation variables
arrival_times = np.cumsum(interarrival_times)  # Cumulative sum of interarrival times
start_service_times = np.zeros(num_customers)
end_service_times = np.zeros(num_customers)
waiting_times = np.zeros(num_customers)
idle_times = []

# Start the simulation
for i in range(num_customers):
    if i == 0:
        start_service_times[i] = arrival_times[i]
    else:
        start_service_times[i] = max(arrival_times[i], end_service_times[i-1])
    end_service_times[i] = start_service_times[i] + service_times[i]
    waiting_times[i] = start_service_times[i] - arrival_times[i]
    if i > 0:
        idle_time = start_service_times[i] - end_service_times[i-1]
        if idle_time > 0:
            idle_times.append(idle_time)

# Metrics calculations
average_waiting_time = np.mean(waiting_times)
probability_wait = np.mean(waiting_times > 0)
total_idle_time = np.sum(idle_times)
total_simulation_time = max(end_service_times)
fraction_idle_time = total_idle_time / total_simulation_time
average_service_time = np.mean(service_times)
average_interarrival_time = np.mean(interarrival_times)
average_time_in_system = np.mean(waiting_times + service_times)
average_number_in_system = np.mean([len(end_service_times[end_service_times > t]) for t in np.arange(total_simulation_time)])/1000
average_number_waiting = np.mean([len(waiting_times[(arrival_times <= t) & (start_service_times > t)]) for t in np.arange(total_simulation_time)])


# Printing Answers
print(f"average_waiting_time:{average_waiting_time}") 
print(f"probability_wait:{probability_wait}")
print(f"fraction_idle_time:{fraction_idle_time}")
print(f"average_service_time:{average_service_time}")
print(f"average_interarrival_time:{average_interarrival_time}")
print(f"average_time_in_system:{average_time_in_system}")
print(f"average_number_in_system:{average_number_in_system}")
print(f"average_number_waiting:{average_number_waiting}")
