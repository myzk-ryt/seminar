#---データは別で用意してあります。---

import matplotlib.pyplot as plt

namelist = ["price","advertising expenses","Number of negative reviews","Number of positive reviews"]
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
  
  plt.title("Relationship between " + namelist[i-1] + " and the number of sales")  # タイトル
  plt.xlabel(namelist[i-1]) # 軸名
  plt.ylabel("Number of sales") #軸名
  plt.grid(True)      #グリッド線（True:引く、False:引かない）
