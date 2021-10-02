import scipy.stats as st
Dat10 = st.pearsonr(dat[:,1],dat[:,0])
Dat20 = st.pearsonr(dat[:,2],dat[:,0])
Dat03 = st.pearsonr(dat[:,3],dat[:,0])
Dat40 = st.pearsonr(dat[:,4],dat[:,0])

print("Dat10=" + str(Dat10) + ", Dat20=" + str(Dat20) + ", Dat30=" + str(Dat03) + ", Dat40=" + str(Dat40))
