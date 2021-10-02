#---データは別で用意してあります。---

import matplotlib.pyplot as plt

for i in range(1,5):
  x = [dat[:,i]]
  y = [dat[:,0]]

  plt.figure(figsize=(5,4))

  plt.scatter(x[0],y[0],
              s = 30,
              c = 'orange',
              marker = 's',
              alpha = 0.8,
              linewidths = 0.5,
              edgecolors = 'black')
