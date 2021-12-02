#---ネガティブな口コミの平均値を求める。---
M = np.mean(dat[:,3])

H = []
L = []

#---ネガティブな口コミが平均以上の製品の値段をH、以下の製品の値段をLに格納する。---
for i in range(len(dat[:,0])):
  if dat[i,3] >= M:
    H.append(dat[i,0])
  else:
    L.append(dat[i,0])

#---H、Lの平均値を求める。---
Have = sum(H) / len(H)
Lave = sum(L) / len(L)

#---差を求める。---
difference = Lave - Have
print("高批判製品群・低批判製品群それぞれの販売数の平均値の差は", difference, "でした。")

#---t検定を行い、p値を求める。---
Ttest = st.ttest_ind(H, L, equal_var=False)
print("t検定のp値は、小数点第四位で丸めて", round(Ttest[1],4), "でした。")
if Ttest[1] < 0.01:
  print("よって1%有意水準です。")
elif Ttest[1] > 0.05:
  print("よって5%有意水準です。")
else:
  print("よって有意な差は認められませんでした。")
  
#---出力結果より、仮説が正しいことが示された。---
