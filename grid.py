import numpy as np
import matplotlib.pyplot as plt

x= np.array([70,75,80,85,90,95,100])
y= np.array([0.9,0.6,0.2,0.8,1.8,2.0,3.1])

plt.title('Sport watch data')
plt.xlabel('Heart Rate')
plt.ylabel('Calories Burned')


plt.plot(x,y, marker='o', color='blue', label='Calories Burned')

plt.grid(True)

plt.show()
