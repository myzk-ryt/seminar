import scipy.stats as st

dat10cor = st.pearsonr(dat[:,1],dat[:,0])
dat20cor = st.pearsonr(dat[:,2],dat[:,0])
dat30cor = st.pearsonr(dat[:,3],dat[:,0])
dat40cor = st.pearsonr(dat[:,4],dat[:,0])

print("値段と販売数の相関係数：", round(dat10cor[0],3), "そのp値：", round(dat10cor[1],5))
print("広告費と販売数の相関係数：", round(dat20cor[0],3), "そのp値：", round(dat20cor[1],5))
print("ネガティブな口コミ数と販売数の相関係数：", round(dat30cor[0],3), "そのp値：", round(dat30cor[1],5))
print("ポジティブな口コミと販売数の相関係数：", round(dat40cor[0],3), "そのp値：", round(dat40cor[1],5))

# 値段と販売数の相関関係は、相関係数が-0.44であり、5%有意水準だった。
# 広告費と販売数の相関関係は、相関係数が-0.17、p値は0.47であり、有意な相関関係は存在しなかった。 
# ネガティブな口コミ数と販売数の相関関係は、相関係数が-0.74であり、1%有意水準だった。 
# ポジティブな口コミ数と販売数の相関関係は、相関係数が0.73であり、1%有意水準だった。
