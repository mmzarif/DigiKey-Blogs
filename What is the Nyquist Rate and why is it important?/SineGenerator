import numpy as np
import matplotlib.pyplot as plt


# Define parameters
amplitude = 1
frequency = 1  # in Hz
time_period = 1 / frequency  # one complete cycle
# sampling_rate = 1000  # samples per second
t = np.arange(0, 5, 0.01)  # time vector from 0 to 5 seconds with 0.01 second intervals


# Generate sine wave
sine_wave = amplitude * np.sin(2*np.pi*frequency * t)


# Plot sine wave
plt.plot(t, sine_wave)
plt.title('Sine Wave with Amplitude 1 and Frequency 1 Hz')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()


