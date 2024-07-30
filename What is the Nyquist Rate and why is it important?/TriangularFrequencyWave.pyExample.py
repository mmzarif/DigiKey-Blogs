import numpy as np
import matplotlib.pyplot as plt


# Parameters
omega_M = 3 * np.pi  # angular frequency of wave


# Frequency range
omega = np.linspace(-omega_M * 1.1, omega_M * 1.1, 1000)


# Magnitude of the triangular function
X = np.maximum(0, 1 - np.abs(omega) / omega_M)


# Plot the triangular function
plt.figure(figsize=(8, 4))
plt.plot(omega, X, 'b')
plt.xlabel(r'$\omega$')
plt.ylabel(r'$|X(j\omega)|$')
plt.title(r'$X(j\omega) = 0$ for $|\omega| > \omega_M$')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.axvline(omega_M, color='black', linestyle='--', linewidth=0.5)
plt.axvline(-omega_M, color='black', linestyle='--', linewidth=0.5)
plt.text(omega_M, 0.05, r'$\omega_M$', horizontalalignment='center')
plt.text(-omega_M, 0.05, r'$-\omega_M$', horizontalalignment='center')
plt.ylim(-0.1, 1.1)
plt.grid(True)
plt.show()
