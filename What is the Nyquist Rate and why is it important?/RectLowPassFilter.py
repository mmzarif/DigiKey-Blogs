import numpy as np
import matplotlib.pyplot as plt


# Parameters
omega_M = 3  # Cutoff frequency of the low-pass filter


# Frequency vector
omega = np.linspace(-10, 10, 1000)


# Rectangular low-pass filter in the frequency domain
def rectangular_low_pass_filter(omega, omega_M):
    return np.where(np.abs(omega) <= omega_M, 1, 0)


# Generate the rectangular low-pass filter
H_omega = rectangular_low_pass_filter(omega, omega_M)




# Plot the rectangular low-pass filter
plt.figure(figsize=(10, 6))
plt.plot(omega, H_omega, 'b', label='Rectangular Low-Pass Filter')
plt.xlabel(r'$\omega$')
plt.ylabel(r'$|H(j\omega)|$')
plt.title('Rectangular Low-Pass Filter in the Frequency Domain')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()
plt.show()
