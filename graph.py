import numpy as np
from matplotlib import pyplot as plt

a = np.arange(25)
b = a**2

plt.plot(a,b)

plt.xlabel('Days')
plt.ylabel('Corona cases')
plt.title('Day vs Corona')
plt.show()