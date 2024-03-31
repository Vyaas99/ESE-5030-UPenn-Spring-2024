 # Re-import numpy and redefine the simulation function with order control after reset
import numpy as np

def simulate_with_order_control(days, M, P, C, a, b, gamma, c, d):
    inventory = M
    orders = []
    daily_profits = []
    order_pending = False  # Track if an order is pending
    
    for day in range(days):
        demand = np.random.randint(a, b + 1)
        sold_items = min(demand, inventory)
        inventory -= sold_items
        
        # Calculate profit for the day
        profit = sold_items * P
        if demand > sold_items:
            profit -= (demand - sold_items) * P
            
        daily_profits.append(profit)
        
        # Check if restock is needed and no order is pending
        if inventory < (gamma * M) and not order_pending:
            lead_time = np.random.randint(c, d + 1)  # Adjusted lead time from c to d days
            # print(lead_time)
            orders.append((day + lead_time+1, M))
            order_pending = True  # Mark that an order is now pending
            
        # Process any orders that have arrived
        orders_to_remove = []
        for order in orders:
            if day >= order[0]:
                # if gamma<0.5:
                #     print(f"Increasing inventory by {M} from {inventory} for gamma={gamma}")
                inventory += order[1]
                if inventory>M:
                    profit-=(inventory-M)*C
                    inventory=M
                orders_to_remove.append(order)
                order_pending = False  # Reset order pending status
                
                
        for order in orders_to_remove:
            orders.remove(order)
    return np.mean(daily_profits)

# Parameters for re-running the simulation
days = 2000
M = 250  # Maximum inventory level
P = 10  # Selling price per item
C = 6  # Cost per item for understock
a = 25  # Minimum daily demand
b = 50  # Maximum daily demand
c = 1  # Minimum lead time
d = 5  # Maximum lead time
gammas = np.linspace(0, 1, 21)  # Gamma values from 0 to 1
# print(f"gammas:{gammas}")

# Re-run simulation with order control logic
controlled_results = {gamma: simulate_with_order_control(days, M, P, C, a, b, gamma, c, d) for gamma in gammas}

# Find the best gamma with order control
best_gamma_controlled = max(controlled_results, key=controlled_results.get)
best_profit_controlled = controlled_results[best_gamma_controlled]


for i in controlled_results.keys():
    print(f"gamma:{i}")
    print(f"Average Daily Profit:{controlled_results[i]}")


print(f"\n\nBest gamma:{best_gamma_controlled}")
print(f"best daily profit: {best_profit_controlled}")
