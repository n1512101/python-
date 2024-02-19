import numpy as np

uk_path = './files/uk.csv'
us_path = './files/usa.csv'

us_data = np.loadtxt(us_path, delimiter=',', dtype=int)
uk_data = np.loadtxt(uk_path, delimiter=',', dtype=int)

zeros_data = np.zeros((us_data.shape[0],1)).astype(int)
ones_data = np.ones((uk_data.shape[0],1)).astype(int)

us_data = np.hstack((us_data, zeros_data))
uk_data = np.hstack((uk_data, ones_data))

final_data = np.vstack((us_data,uk_data))
print(final_data)