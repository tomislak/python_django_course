import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0., 10., 0.2)

plt.subplot(1, 2, 1)
plt.plot(t, np.sin(t), 'r-')

plt.subplot(1, 2, 2)
plt.plot(t, np.cos(t), 'b--')

plt.savefig('slika.png')
