import numpy as np

# Data usage matrix (3 users × 2 weeks)
data = np.array([[5, 7],
                 [6, 8],
                 [4, 6]])

# Total data used by each user (row-wise sum)
total_per_user = np.sum(data, axis=1)

# Average data usage per week (column-wise mean)
average_per_week = np.mean(data, axis=0)

# Display results
print("Data Usage Matrix:\n", data)
print("Total Data Used by Each User:", total_per_user)
print("Average Data Usage per Week:", average_per_week)