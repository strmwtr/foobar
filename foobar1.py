import array

def answer1(data, n):
    for x in data:
        if data.count(x) > n:
            data = [y for y in data if y != x]
    return data

array1 = [-200, -34, 0, 1, 2, 10, 1000]
array2 = [-200, -34, -5, 0, 1, 2, 10, 1000]


def answer(xs):
  pos_xs = [x for x in xs if x > 0]
  neg_xs = [x for x in xs if x < 0]
  if len(neg_xs) % 2 != 0:
    neg_xs.remove(max(neg_xs))
  return str(reduce(lambda x,y: x*y, neg_xs+pos_xs))

def answer(xs):
  pos_xs = [x for x in xs if x > 0]
  neg_xs = [x for x in xs if x < 0]
  if len(neg_xs) % 2 != 0:
    neg_xs.remove(max(neg_xs))
  data_list = neg_xs + pos_xs
  data_array = array.array(i,data_list)
  power = reduce(lambda x,y: x*y, data_list)
  power_str = str(power)
  return power_str
    
print answer(array1)
print type(answer(array2))	

