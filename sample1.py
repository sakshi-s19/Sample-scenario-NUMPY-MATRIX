import numpy as np

beds = np.array([[12, 10, 11],
                 [9,  8,  7],
                 [15, 14, 13]])

total_beds = np.sum(beds)

print("Bed Occupancy Matrix:\n", beds)
print("Total Occupied Beds:", total_beds)