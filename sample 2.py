import numpy as np

units = np.array([[120, 150, 170],
                  [100, 130, 160]])

avg_units = np.mean(units, axis=1)

print("Electricity Usage Matrix:\n", units)
print("Average Consumption per House:", avg_units)