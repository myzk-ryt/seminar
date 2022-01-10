a = np.mean(dat[:,0])
print("販売数の平均値は", a, "です。")

ureru,urenai = [],[]
for i in range(len(dat[:,0])):
  if dat[i,0] >= a:
    ureru.append(dat[i,0])
  else:
    urenai.append(dat[i,0])
print("平均値以上：", ureru, "\n平均値以下：", urenai)

#data結合
X = np.concatenate([dat[:,1], dat[:,2]],0)
Y = dat[:,0]

from sklearn.neural_network import MLPClassifier

NN = MLPClassifier(
    hidden_layer_sizes=(3,),
    max_iter=1000,
    learning_rate_init=0.01,
    random_state=0,
    verbose=True
)
