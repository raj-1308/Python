import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

num=[1,2,3,4,5,6,7,8,9,10]

maximum= float('-inf')
minimum=float('inf')


for i in num:
    if i>maximum:
        maximum=i
    if i<minimum:
        minimum=i

print("Maximum number is: ",maximum)
print("Minimum number is: ",minimum)

