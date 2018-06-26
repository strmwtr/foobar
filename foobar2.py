array1 = [-200, -34, 0, 1, 2, 10, 1000]
array2 = [-200, -34, -5, 0, 1, 2, 10, 1000]
array3 = [2, 0, 2, 2, 0]
array4 = [-3]
'''
def answer(xs):
  pos_xs = [x for x in xs if x > 0]
  neg_xs = [x for x in xs if x < 0]
  if len(neg_xs) % 2 != 0:
    neg_xs.remove(max(neg_xs))
  data_list = neg_xs + pos_xs
  power_int = reduce(lambda x,y: x*y, data_list)
  power_str = str(power_int)
  return power_str
'''
def answer(xs):
  xs = [x for x in xs if x != 0]
  negs = [x for x in xs if x < 0]
  if len(negs) % 2 != 0:
    xs.remove(max(negs))
  return str(reduce(lambda x,y: x*y, xs))

print (answer(array1))
print (answer(array2))
print (answer(array3))	

