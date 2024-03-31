import numpy as np

# Constants
cost_per_pretzel = 0.30
selling_prices = {1: 1.00, 2: 1.50, 3: 2.00}
probabilities = {1: 0.3, 2: 0.5, 3: 0.2}
customer_rate = 3  # per minute
duration = 480  # minutes
leftover_price = 0.05
simulation_days = 50


lost_revenue=0

# Simulation function for a day
def simulate_day(M):
    pretzels_left = M
    total_revenue = 0
    lost_revenue=0
    for _ in range(duration):
        num_customers = np.random.poisson(customer_rate)  # Number of customers arriving in this minute
        for _ in range(num_customers):
            order_type = np.random.choice([1, 2, 3], p=[probabilities[1], probabilities[2], probabilities[3]])
            if pretzels_left==0:
                lost_revenue+=selling_prices[order_type]
            else:
                pretzels_ordered = min(order_type, pretzels_left)
                pretzels_left -= pretzels_ordered
            if pretzels_ordered>0:
                total_revenue += selling_prices[pretzels_ordered]
            if pretzels_left<=0:
                pretzels_left=0
    total_revenue += pretzels_left * leftover_price  # Add revenue from leftover pretzels
    profit = total_revenue - (M * cost_per_pretzel) - lost_revenue
    return profit, pretzels_left

# Simulation across different values of M and 50 days
results = {}
for M in range(2500, 3200, 10):  # Experimenting with different M values from 2500 to 3200 with steps of 10
    profits, leftovers = [], []
    for _ in range(simulation_days):
        profit, leftover = simulate_day(M)
        profits.append(profit)
        leftovers.append(leftover)
    avg_profit = np.mean(profits)
    avg_leftover = np.mean(leftovers)
    results[M] = (avg_profit, avg_leftover)

# Find M value that maximizes average profit
# print(f"Results:{results}\n\n")
optimal_M = max(results, key=lambda x: results[x][0])
optimal_profit = results[optimal_M][0]
optimal_leftover = results[optimal_M][1]


print(f"Optimal M:{optimal_M}")
print(f"Optimal Profit:{optimal_profit}")
print(f"Optimal Leftover:{optimal_leftover}")
