from sklearn.linear_model import LinearRegression
#相関がなかった広告費を要素から除外して考えます。

#データ
y = dat[:,0]
x1 = dat[:,1]
x2 = dat[:,3]
x3 = dat[:,4]

#---まず、切片付きの回帰式A---

x1 = np.reshape(x1,(20,1))
x2 = np.reshape(x2,(20,1))
x3 = np.reshape(x3,(20,1))
x = np.concatenate([x1,x2,x3],1)

ModelLR = LinearRegression()
ModelLR.fit(x,y)

#回帰式を出力する関数です。
def abcOutput():
  print("y^ = ",round(ModelLR.coef_[0],3), "x1 + ", round(ModelLR.coef_[1],3), "x2 + ", round(ModelLR.coef_[2],3), "x3 + ", round(ModelLR.intercept_,3))

print("切片付き回帰式A")
abcOutput()
  
#---次に、切片なし回帰式B---

ModelLR_noB = LinearRegression(fit_intercept=False) #線形回帰モデルのセット
ModelLR_noB.fit(x,y) #パラメータ獲得

print("切片付き回帰式B")
abcOutput()
