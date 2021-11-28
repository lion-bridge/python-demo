# 生成数组
def gen1(start: int, end: int):
  arr = []
  for x in range(start, end):
    arr.append(x)
  return arr;

# 简写
def gen2(start: int, end: int):
  return [x for x in range(start, end)]

print('gen1=', gen1(1,10))
print('gen2=', gen2(1,10))


