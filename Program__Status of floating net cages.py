#!/usr/bin/env python
# coding: utf-8

# In[1]:


import skfuzzy as fuzz
import numpy as np

# Temperature
temperatur = np.arange(0, 41, 1)

cold = fuzz.gauss2mf(temperatur, 2.782, 3.434, 17.7, 2.3)
cool = fuzz.gaussmf(temperatur, 24, 1.7)
normal = fuzz.gaussmf(temperatur, 28.5, 1.7)
warm = fuzz.gaussmf(temperatur, 33, 1.7)
hot = fuzz.gauss2mf(temperatur, 38.63, 2.278, 41, 0.034)

# Dissolved Oxygen
dissolved_oxygen = np.arange(0, 10, 0.1)

very_poor = fuzz.gauss2mf(dissolved_oxygen, 0, 0.007, 2.1, 0.28)
poor = fuzz.gaussmf(dissolved_oxygen, 2.8, 0.2)
normal_DO = fuzz.gaussmf(dissolved_oxygen, 3.5, 0.2)
good = fuzz.gaussmf(dissolved_oxygen, 4.2, 0.2)
very_good = fuzz.gauss2mf(dissolved_oxygen, 5, 0.28, 10, 0.007)

# pH
pH = np.arange(0, 14, 0.1)

very_Acidid = fuzz.gauss2mf(pH, 0, 0.0119, 4, 0.5535)
Acidid = fuzz.gaussmf(pH, 5.5, 0.5)
normal_pH = fuzz.gaussmf(pH, 7.5, 0.5)
Alkaline = fuzz.gaussmf(pH, 9.5, 0.5)
very_Alkaline = fuzz.gauss2mf(pH, 11, 0.5535, 14, 0.0119)

# Visualize the membership functions
import matplotlib.pyplot as plt

fig, (ax0, ax1, ax2) = plt.subplots(nrows=3, figsize=(8, 9))

ax0.plot(temperatur, cold, 'b', linewidth=1.5, label='Cold')
ax0.plot(temperatur, cool, 'g', linewidth=1.5, label='Cool')
ax0.plot(temperatur, normal, 'r', linewidth=1.5, label='Normal')
ax0.plot(temperatur, warm, 'm', linewidth=1.5, label='Warm')
ax0.plot(temperatur, hot, 'y', linewidth=1.5, label='Hot')
ax0.set_title('Temperature')
ax0.legend()

ax1.plot(dissolved_oxygen, very_poor, 'b', linewidth=1.5, label='Very Poor')
ax1.plot(dissolved_oxygen, poor, 'g', linewidth=1.5, label='Poor')
ax1.plot(dissolved_oxygen, normal_DO, 'r', linewidth=1.5, label='Normal')
ax1.plot(dissolved_oxygen, good, 'm', linewidth=1.5, label='Good')
ax1.plot(dissolved_oxygen, very_good, 'y', linewidth=1.5, label='Very Good')
ax1.set_title('Dissolved Oxygen')
ax1.legend()

ax2.plot(pH, very_Acidid, 'b', linewidth=1.5, label='Very Acidid')
ax2.plot(pH, Acidid, 'g', linewidth=1.5, label='Acidid')
ax2.plot(pH, normal_pH, 'r', linewidth=1.5, label='Normal')
ax2.plot(pH, Alkaline, 'm', linewidth=1.5, label='Alkaline')
ax2.plot(pH, very_Alkaline, 'y', linewidth=1.5, label='Very Alkaline')
ax2.set_title('pH')
ax2.legend()

def decision_making(temperature_value, dissolved_oxygen_value, pH_value):
    if temperature_value >= 24 and temperature_value <= 33 and dissolved_oxygen_value >= 3.0 and pH_value >= 5.5 and pH_value <= 9.5:
        return "Stay_In_Position"
    else:
        return "Move"

# Get user inputs
temperature_value = float(input("Enter the temperature: "))
dissolved_oxygen_value = float(input("Enter the dissolved oxygen value: "))
pH_value = float(input("Enter the pH: "))

# Result
result = decision_making(temperature_value, dissolved_oxygen_value, pH_value)
print("The Floating Net Cage should be: ", result)


# In[ ]:




