#必要なライブラリの読み込み
from sklearn.linear_model import LinearRegression

#相関がなかった広告費を要素から除外して考えます。
#データ準備
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

print("切片付き回帰式A：y^ = ",round(ModelLR.coef_[0],3), "x1 + ", round(ModelLR.coef_[1],3), "x2 + ", round(ModelLR.coef_[2],3), "x3 + ", round(ModelLR.intercept_,3))

#AのRMSE評価
y_pred_01 = ModelLR.predict(x)
Mse_01 = mean_squared_error(y,y_pred_01)
Rmse_01 = np.sqrt(Mse_01)
print("回帰式AのRMSE：", Rmse_01)

ModelLR = LinearRegression(fit_intercept=False) # 線形回帰モデルのセット
ModelLR.fit(x, y)

print("切片なし回帰式B：y^ = ",round(ModelLR.coef_[0],3), "x1 + ", round(ModelLR.coef_[1],3), "x2 + ", round(ModelLR.coef_[2],3), "x3 + ", round(ModelLR.intercept_,3))

#BのRMSE評価
y_pred_02 = ModelLR.predict(x)
Mse_02 = mean_squared_error(y,y_pred_02)
Rmse_02 = np.sqrt(Mse_02)
print("回帰式AのRMSE：", Rmse_02)
