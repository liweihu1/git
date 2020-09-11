import matplotlib.pyplot as plt
import numpy as np

sinValue = input("Please type a number \n")
cosValue = input("Please type a number \n")

x = np.arange(0, 30, 0.1)
plt.plot(x, np.sin(x * int(sinValue)), label="sinus")
plt.plot(x, np.cos(x * int(cosValue)), label="cosinus")
plt.legend()
plt.show()