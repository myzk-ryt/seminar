koumoku = ["販売数","値段","広告費","ネガ口コミ","ポジ口コミ"]
heikin = []
hyouzyunhensa = []

for i in range(0,5):
  heikin.append(np.mean(dat[:,i]))
  hyouzyunhensa.append(np.std(dat[:,i]))
  print(koumoku[i], "について\n平均値は", round(heikin[i],3), "標準偏差は", round(hyouzyunhensa[i],3))

print()
print("また", koumoku[1], "について\n", round(heikin[1] - hyouzyunhensa[1],3), "から", round(heikin[1] + hyouzyunhensa[1],3), "の間に約70%のデータが集中していると考えられる。")
print(round(heikin[1] - 2 * hyouzyunhensa[1],3), "から", round(heikin[1] + 2 * hyouzyunhensa[1],3), "の間に約95%のデータが集中していると考えられる。")
