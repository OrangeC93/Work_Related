from itertools import *

# merging and splitting iterators

test_list = [[1,2,3,4], ['a','b','c']]
chain_result = list(chain(*test_list))
print(chain_result)

zip_result = list(zip(*test_list))
print(zip_result)
# zip_loggest_result = list(zip_longest(*test_list))
# print(zip_loggest_result)

shapes = ['circle', 'triangle', 'square', 'pentagon']
selections = [True, False, True, False]
compress_result = list(compress(shapes, selections))
print(compress_result)

# repeating
for x in repeat('abc', 10):
    print(x)

arr = 'BCDDIIJKNNOOPPPSTTVX'
grps = []
keys = []
for key, grp in groupby(arr):
    grps.append(list(grp))
    keys.append(key)
print(''.join(keys))
print(grps)