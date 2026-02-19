import numpy as np

# Meals sold matrix (4 time slots × 2 days)
meals = np.array([[35, 40],
                  [50, 55],
                  [45, 48],
                  [30, 32]])

# Total meals in each time slot (row-wise sum)
time_slot_total = np.sum(meals, axis=1)

# Overall total meals
overall_total = np.sum(meals)

# Display results
print("Meals Sold Matrix:\n", meals)
print("Total Meals in Each Time Slot:", time_slot_total)
print("Overall Total Meals Sold:", overall_total)