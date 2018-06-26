def answer(xs): 
  #Remove 0 Values
  while 0 in xs: xs.remove(0)
  #If single negative number given output 0
  negs = [x for x in xs if x < 0]
  if len(negs) == 1 and len(xs) == 1:
    power_int = negs[0]
  #Address odd number of negative values by removing smallest abs value  
  elif len(negs) % 2 != 0:
    xs.remove(max(negs))
  #If length of xs is 0, output 0 (Causes by array with only 0 values)
  if len(xs) == 0:
    power_int = 0 
  #All other cases multiply xs together to get max output
  else:
    power_int = reduce(lambda x,y: x*y, xs)
  #Turn int to str
  power_str = str(power_int)
  return power_str

def test_func():
  a1 = [0, 0]
  a2 = [2]
  a3 = [0]
  a4 = [-2]
  a5 = [2,2]
  a6 = [-2,2]
  a7 = [-2,-2]
  a8 = [-2,-2,2]
  a9 = [-2,2,2]
  a10 = [-1000,1000,-1000]

  arrays = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10]

  for a in arrays:
    print 'Array: {0}   ||   Output: {1}'.format(a, answer(a))

test_func()

