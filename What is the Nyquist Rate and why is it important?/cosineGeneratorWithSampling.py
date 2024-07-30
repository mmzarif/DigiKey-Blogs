import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d


# Define parameters
amplitude = 1
frequency = 1  # in Hz
sampling_frequency = 1  # in Hz for the impulse train
time_period = 1 / frequency  # one complete cycle
t = np.arange(0, 5, 0.01)  # time vector from 0 to 5 seconds with 0.01 second intervals


# Generate cosine wave
cosine_wave = amplitude * np.cos(2 * np.pi * frequency * t)


# Generate sampling points
sampling_points = np.arange(0, 5 + 1 / sampling_frequency, 1 / sampling_frequency)  # time points for impulse train
sampled_wave = amplitude * np.cos(2 * np.pi * frequency * sampling_points)  # sampled values of the cosine wave


# Adjust the end of the interpolation range to match the sampled points
t_interpolated = np.arange(0, 5, 0.01)  # time vector for the interpolated wave
valid_range = t_interpolated[t_interpolated <= sampling_points[-1]]


# Perform interpolation to trace the outline of the sampled points
interpolated_func = interp1d(sampling_points, sampled_wave, kind='cubic')
interpolated_wave = interpolated_func(valid_range)


# Plot cosine wave
plt.plot(t, cosine_wave, label='Cosine Wave', alpha=0.5)


# Plot sampled points with stem plot
plt.stem(sampling_points, sampled_wave, linefmt='r-', markerfmt='ro', basefmt='r-', label='Sampled Points')


# Plot the interpolated outline
plt.plot(valid_range, interpolated_wave, 'g--', label='Interpolated Outline')


# Add titles and labels
plt.title('Cosine Wave with Amplitude 1 and Frequency 1 Hz with Impulse Train Sampling at 1 Hz')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.show()
