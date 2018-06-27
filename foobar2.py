def answer(xs): 
  #Remove 0 Values
  while 0 in xs: xs.remove(0)
  #Create list of negative integers
  negs = [x for x in xs if x < 0]
  #If odd num of neg vals and negs > 1,
  #Remove smallest abs value from negs
  if len(negs) % 2 != 0 and len(xs) != 1:
    xs.remove(max(negs))
  #If xs is empty set power_int to 0
  if len(xs) == 0:
    max_int = 0
  else:
    max_int = reduce(lambda x,y: x*y, xs)
  #Turn int to str
  max_str = str(max_int)
  return max_str

listx = [[0],[1],[-1],[0,0],[1,0],[-1,0],[-1,-1]]
for x in listx:
  print answer(x)

'''
Test 3 fails with current script, passes Test 4
Test 4 is a single negative output and is looking for a negative result

Check against [-1, 0]. Should return 0, not -1

Below currently returns bytes error, but on the right track

def answer(xs): 
  #Create list of negative integers
  negs = [x for x in xs if x < 0]
  #Get a count of all 0 elements
  count_0 = len([x for x in xs if x != 0])
  #If odd num of neg vals and negs > 1,
  #Remove smallest abs value from negs
  if len(negs) % 2 != 0 and len(xs) != 1:
    xs.remove(max(negs))
  elif len(negs) == 1 and len(count_0) != 0:
    max_int = 0
  else:
    while 0 in xs: xs.remove(0)
    if len(xs) == 0:
      max_int = 0
    else:
      max_int = reduce(lambda x,y: x*y, xs)
  #Turn int to str
  max_str = str(max_int)
  return max_str
'''

