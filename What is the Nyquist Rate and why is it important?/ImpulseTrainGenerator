import numpy as np
import matplotlib.pyplot as plt


# Define parameters
sampling_frequency = 1  # in Hz for the impulse train
duration = 5  # seconds
sampling_interval = 1 / sampling_frequency
t = np.arange(0, duration + sampling_interval, sampling_interval)  # time vector for impulse train


# Generate impulse train
impulse_train = np.zeros_like(t)
impulse_train[::int(sampling_frequency)] = 1  # Set impulses at sampling points


# Plot impulse train
plt.figure(figsize=(10, 4))
plt.stem(t, impulse_train, linefmt='b-', markerfmt='bo', basefmt='b-')
plt.title('Impulse Train with Sampling Frequency 1 Hz')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
