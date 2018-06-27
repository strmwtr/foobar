#power_hungry final answer
def answer(xs):
  pos = [x for x in xs if x > 0]
  neg = [x for x in xs if x < 0]
  zeros = [x for x in xs if x == 0]
  if len(pos) == 0 and len(neg) == 1 and len(zeros) != 0:
    xs = [0]
  if len(neg) % 2 != 0 and len(neg) != 1:
    xs.remove(max(neg))
  while 0 in xs: xs.remove(0)
  if len(xs) == 0:
    power = 0
  else:
    power = reduce(lambda x,y: x*y, xs)
  return str(power)

arrays = [[0],[-1],[1],[0,1],[0,-1],[-1,-1],[1,1],[0,0]]
for x in arrays:
  print answer(x)











