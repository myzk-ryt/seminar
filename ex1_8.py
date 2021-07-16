#[注意]if文書くときは、より小さい部分集合から並べないといけない。
#コンピュータは文を上から読むため、大きい集合から書くと、条件の篩にうまくかけられないから。

def func1(a,b,c):
  if a >= b:
    list.append(-1)
    print("aはbより小さい値を入力してください。")
  elif b - a <= c:
    print("[警告]単一の値しか返ってきません")
  else:
    for i in range(a,b,c):
      list.append(i)
    print(list)
