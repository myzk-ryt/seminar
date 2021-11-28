y = dat[:,0]
x1 = dat[:,1]
x2 = dat[:,3]
x3 = dat[:,4]

#それぞれを一列の行列に直してxを生成
x1 = np.reshape(x1,(20,1))
x2 = np.reshape(x2,(20,1))
x3 = np.reshape(x3,(20,1))
x = np.concatenate([x1,x2,x3],1)

ModelLR = LinearRegression()
ModelLR.fit(x,y)

yosoku = round(ModelLR.coef_[0] * dat[5,1] + ModelLR.coef_[1] * dat[5,3] + ModelLR.coef_[2] * dat[5,4] + ModelLR.intercept_,3)
print("予測値：", yosoku)
print("実測値：", dat[5,0])
print("誤差：", round(yosoku - dat[5,0],3))

#---出力結果---
#予測値： 75.392
#実測値： 60.0
#誤差： 15.392
