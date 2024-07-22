import numpy as np
import matplotlib.pyplot as plt

angular_frequency = 2 * np.pi * 19670.5

def normalized_gain_module(w):
    return round(1 / (np.sqrt(w**2 / angular_frequency**2 + 1)), 5)

def normalized_gain_phase(w):
    return round(np.rad2deg(np.arctan(w / angular_frequency)), 5)

def error_vector_module(w):
    return round(1 - 1 / (np.sqrt(w**2 / angular_frequency**2 + 1)), 5)

def error_vector_phase(w):
    return np.rad2deg(round(-np.arctan(w / angular_frequency) + np.pi / 2, 5))

frequencies = []
gain_modules = []
gain_phases = []
error_modules = []
error_phases = []

for i in range(11):
    frequencies.append(round(0.1 * i * angular_frequency, 5))
    gain_modules.append(normalized_gain_module(0.1 * i * angular_frequency))
    gain_phases.append(normalized_gain_phase(0.1 * i * angular_frequency))
    error_modules.append(error_vector_module(0.1 * i * angular_frequency))
    error_phases.append(error_vector_phase(0.1 * i * angular_frequency))
    
for i in range(11):
    print("Frequency = ", frequencies[i], 
          " Gain Module = ", gain_modules[i], 
          " Gain Phase = ", gain_phases[i], 
          " Error Module = ", error_modules[i], 
          " Error Phase = ", error_phases[i])
    
fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('Frequency')
ax1.set_ylabel('Error Module', color=color)
ax1.plot(frequencies, error_modules, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('Error Phase', color=color)
ax2.plot(frequencies, error_phases, color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()
plt.show()
