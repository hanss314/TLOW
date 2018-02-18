#             custom range
#             |   starting from el
#             |   |   with el elements
#             |   |   |      with difference the previous element
#             |   |   |      |              for every index i and element el
#             |   |   |      |              |            in arr
def r3(arr): #|   |   |      |              |            |            returning the result reversed
  return [nrange(el, el, arr[i - 1]) for (i, el) in enumerate(arr)][::-1]
def nrange(start, n, diff): 
  return [start + i * diff for i in range(n)]
