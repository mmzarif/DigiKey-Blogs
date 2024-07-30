import numpy as np
import matplotlib.pyplot as plt


# Parameters
omega_M = 3  
omega_period = 6  # Period of the repeating triangular function in rad/s, not s


# Frequency range
omega = np.linspace(-3 * omega_period, 3 * omega_period, 1000)


# Generate the repeating triangular function and its components
X = np.zeros_like(omega)
components = []


for k in range(-3, 4):  # Adjust the range for more repetitions of triangles
    component = np.maximum(0, 1 - np.abs(omega - k * omega_period) / omega_M)
    components.append(component)
    X += component


# Plot the triangular function
plt.figure(figsize=(12, 6))
plt.plot(omega, X, 'b', label='Sum of Components')


# Plot each individual component as a dotted line
for i, component in enumerate(components):
    plt.plot(omega, component, 'r--', label=f'Component {i-3}')


plt.xlabel(r'$\omega$')
plt.ylabel(r'$|X(j\omega)|$')
plt.title(r'$X(j\omega)$ Repeating Triangular Function and Components')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
for k in range(-3, 4):
    plt.axvline(k * omega_period, color='black', linestyle='--', linewidth=0.5)
    if k != 0:
        plt.text(k * omega_period, 0.05, f'${k} \cdot {omega_period}$', horizontalalignment='center')
plt.ylim(-0.1, 1.1)
plt.legend()
plt.grid(True)
plt.show()
