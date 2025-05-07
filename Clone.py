import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd

function = lambda x: x**2 + 2*x + 1
x = np.linspace(-10, 10, 100)
y = function(x)

plt.plot(x, y, label='y = x^2 + 2x + 1')
plt.title('Plot of the function y = x^2 + 2x + 1')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', lw=0.5, ls='--')
plt.axvline(0, color='black', lw=0.5, ls='--')
plt.grid()
plt.legend()
plt.show()



# Create a DataFrame from the lists
# df = pd.DataFrame({'Maximum': maximum, 'Minimum': minimum})

# print("DataFrame: \n",df)
