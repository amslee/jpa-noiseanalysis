import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#defining linear function
def func(t, a, b):
    return a*t + b

#importing data from excel files
jpa_gain = pd.read_excel('jpa_gain_dc.xlsx').values
jpa_snr = pd.read_excel('jpa_snr_dc.xlsx').values

#parsing data into arrays (that wont throw errors)
arr_length = len(jpa_gain)
y_data = np.zeros(arr_length)
x_data = np.zeros(arr_length)
for i in range(0, arr_length):
    value = (jpa_snr[i] / jpa_gain[i])
    y_data[i] = value
    x_data[i] = jpa_snr[i]

xp = np.linspace(10,22)
popt, _ = curve_fit(func, x_data, y_data)
#constrained b coefficient using ideal TC and TH values
#popt_ideal, _ = curve_fit(func, x_data, y_data, bounds=([-np.inf, 0.0325], [np.inf, 0.0326]))

print(popt)
#print(popt_ideal)

plt.plot(x_data, y_data, '.')
plt.plot(xp, func(xp, *popt))
#plt.plot(xp, func(xp, *popt_ideal))
plt.show()






