list = []

def func1(a,b,c):
   if a < b:
      for i in range(a,b,c):
        list.append(i)
   print(list)
   else:
      list.append(-1)
      print("aはbより小さい値を入力してください。\n",list)
