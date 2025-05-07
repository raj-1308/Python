import matplotlib.pyplot as plt
import numpy as np


xpoint = np.linspace(0, 2 * np.pi, 100)
ypoint = np.sin(xpoint)
plt.plot(xpoint, ypoint)
plt.title('Sine Wave')

# plt.plot(ypoint, marker='o')
# plt.title('Sine Wave with Markers')

plt.show()