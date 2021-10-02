import scipy.stats as st
Dat10 = st.pearsonr(dat[:,1],dat[:,0])
Dat20 = st.pearsonr(dat[:,2],dat[:,0])
Dat03 = st.pearsonr(dat[:,3],dat[:,0])
Dat40 = st.pearsonr(dat[:,4],dat[:,0])

print("Dat10=" + str(Dat10) + ", Dat20=" + str(Dat20) + ", Dat30=" + str(Dat03) + ", Dat40=" + str(Dat40))

# 値段と販売数の相関関係は、相関係数が-0.44であり、5%有意水準だった。
# 広告費と販売数の相関関係は、相関係数が-0.17、p値は0.47であり、有意な相関関係は存在しなかった。 
# ネガティブな口コミ数と販売数の相関関係は、相関係数が-0.74であり、1%有意水準だった。 
# ポジティブな口コミ数と販売数の相関関係は、相関係数が0.73であり、1%有意水準だった。
