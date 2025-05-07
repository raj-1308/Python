import matplotlib.pyplot as plt
import numpy as np

y= np.array([45,20,15,10,5,5])

mylabels= ['Study','Diet','Gym','Other','Running','Walking']
mycolors= ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6']

plt.pie(y, labels= mylabels, colors= mycolors, startangle= 90, shadow= True, explode= (0.1,0.1,0.1,0.1,0.1,0.1), autopct='%1.1f%%')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()