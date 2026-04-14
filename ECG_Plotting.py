
import numpy as np
import matplotlib.pyplot as plt

# tidsakse
t = np.linspace(0,1,500)

# "rent" signal
signal = np.sin(5*2*np.pi*t)

# støj
noise = np.random.normal(0,0.3,500)

# støjfyldt signal
noisy_signal = signal + noise

# plot
plt.plot(t, signal, label="Rent signal")
plt.plot(t, noisy_signal, label="Støjfyldt signal")
plt.legend()
plt.show()