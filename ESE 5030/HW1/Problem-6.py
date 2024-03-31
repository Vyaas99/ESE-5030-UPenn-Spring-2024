import numpy as np

def solve_linear_system(p1, p2, q1, q2):
    #Solve the linear system for t1 and t2 to check if the line segments intersect.
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = q1
    x4, y4 = q2

    denominator = (x2 - x1) * (y4 - y3) - (y2 - y1) * (x4 - x3)
    if denominator == 0:
        return False  # Parallel or coincident lines

    t1 = ((x3 - x1) * (y4 - y3) - (y3 - y1) * (x4 - x3)) / denominator
    t2 = ((x3 - x1) * (y2 - y1) - (y3 - y1) * (x2 - x1)) / denominator

    return 0 <= t1 <= 1 and 0 <= t2 <= 1

# Monte Carlo simulation 
intersection_count = 0
num_simulations=5000
for _ in range(num_simulations):
    x11, y11, x12, y12, x21, y21, x22, y22 = np.random.uniform(0, 1, 8)
    if solve_linear_system((x11, y11), (x12, y12), (x21, y21), (x22, y22)):
        intersection_count += 1

intersection_probability_linear = intersection_count / num_simulations
print(intersection_probability_linear)