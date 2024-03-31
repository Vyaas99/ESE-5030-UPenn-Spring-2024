import numpy as np

# Constants
L = 84  # Length of the bridge in feet
a = 3  # Min speed in feet per second
b = 7  # Max speed in feet per second
arrival_interval = 20  # Time between arrivals in seconds (3/minute)
total_natives = 10000  # Total number of natives 


natives_waiting = []  # Queue of waiting times for natives waiting to cross
bridge_status = 'free'  
time = 0  # Simulation time in seconds
crossing_times = []  # Times natives take to cross the bridge
waiting_times = []  # Times natives spend waiting to cross
finished_natives = 0  # Count of natives who have finished crossing

# Variables for the native currently crossing the bridge
crossing_start_time = None  # Start time for the current crossing
crossing_duration = None  # Duration of the current crossing

# Main simulation loop
while finished_natives < total_natives:
    # Handle native arrivals
    if time % arrival_interval == 0:  # New native arrives
        natives_waiting.append(time)  # Record arrival time

    # Handle bridge crossing
    if bridge_status == 'free' and natives_waiting:
        bridge_status = 'occupied'
        crossing_start_time = time
        start_waiting_time = natives_waiting.pop(0)  # Get the time the native started waiting
        speed = np.random.uniform(a, b)  # Assign random speed
        crossing_duration = L / speed
        waiting_times.append(time - start_waiting_time)  # Calculate waiting time

    # Check if the current native has finished crossing
    if bridge_status == 'occupied' and time >= crossing_start_time + crossing_duration:
        bridge_status = 'free'
        crossing_times.append(time - crossing_start_time)
        finished_natives += 1

    # Advance simulation time
    time += 1

# Answers
average_crossing_time = np.mean(crossing_times)
average_waiting_time = np.mean(waiting_times)
total_simulation_time = time
average_total_time = average_waiting_time + average_crossing_time
natives_getting_out = finished_natives

# Printing results
print(f'Average crossing time: {average_crossing_time} seconds')
print(f'Average waiting time: {average_waiting_time} seconds')
print(f'Average total time from arrival to having crossed: {average_total_time} seconds')
print(f'Total simulation time: {total_simulation_time} seconds')
print(f'Number of natives getting out of the village: {natives_getting_out}')
