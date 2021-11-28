yosoku = round(ModelLR.coef_[0] * dat[5,1] + ModelLR.coef_[1] * dat[5,3] + ModelLR.coef_[2] * dat[5,4] + ModelLR.intercept_,3)
print("予測値：", yosoku)
print("実測値：", dat[5,0])
print("誤差：", round(yosoku - dat[5,0],3))
