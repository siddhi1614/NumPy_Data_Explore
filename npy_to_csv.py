import numpy as np

# Load .npy file
data = np.load("saved_array.npy")

# Save as CSV
np.savetxt("saved_array.csv", data, delimiter=",", fmt="%d")

print("saved_array.csv created successfully")
