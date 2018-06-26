def answer(xs):
  #Remove 0 values
  while 0 in xs: xs.remove(0)
  #Get list of negative values
  negs = [x for x in xs if x < 0]
  #If length of negs is 1 and length of xs is 1, output 0
  if len(negs) == 1 and len(xs) == 1:
    power_int = 0
  elif len(negs) % 2 != 0 and len(negs) != 1:
    xs.remove(max(negs))
  elif len(negs) % 2 != 0 and len(negs) == 1:
    power_int = 0
  elif len(xs) == 0:
    power_int = 0 
  else:
    power_int = reduce(lambda x,y: x*y, xs)
  power_str = str(power_int)
  return power_str

def test_func():
  a2 = [2]
  a3 = [0]
  a4 = [-2]
  a5 = [2,2]
  a6 = [-2,2]
  a7 = [-2,-2]
  a8 = [-2,-2,2]
  a9 = [-2,2,2]
  arrays = [a2, a3, a4, a5, a6, a7, a8, a9]

  for a in arrays:
    print 'Array: {0}   ||   Output: {1}'.format(a, answer(a))

test_func()

