import numpy as np

a = np.loadtxt('123.txt')
print(a)

# np.genfromtxt('file.csv',delimiter=',') | From a CSV file
# np.savetxt('file.txt',arr,delimiter=' ') | Writes to a text file
# np.savetxt('file.csv',arr,delimiter=',') | Writes to a CSV file

# create array
print(np.array([1,2,3])) #1d array
print(np.array([(1,2,3),(4,5,6)])) #2d array
print(np.zeros(3)) #1d of lenght 3 all values 0 
print(np.ones((3,4))) #3*4 array with all values 1
print(np.eye(5)) #5*5 array of 0 with 1 on diagonal
print(np.linspace(0,100,6)) #array of 6 evenly divided values from 0 to 100
print(np.arange(0,10,3)) #array of values from 0 to less than 10 with step 3 (eg [0,3,6,9])
print(np.full((2,3),8)) #2*3 array with value of 8
print(np.random.rand(4,5)) #4x5 array of random floats between 0-1
print(np.random.rand(6,7)*100) ##4x5 array of random floats between 0-100
print(np.random.randint(5,size=(2,3)))

# inspect array
print(a.size)
print(a.shape)
print(a.dtype)
print(a.astype(float))
print(a.tolist())
print(np.info(np.ones))

# copy, sort, reshape
b = np.copy(a)
print(b)
print(b.view(float))
# print(b.sort()) #does not work
# print(b.sort(axis=1)) #does not work
print(b.flatten())
print(b.T)
print(b.reshape(4,1))
# print(b.resize((5,6))) #does not work

#add and remove
print(a)
print(np.append(b, (5,6)))
# print(np.append(b, 2, 1)) #cannot be implemented
# np.delete(arr,1,axis=0) | Deletes row on index 3 of arr
# np.delete(arr,0,axis=1)

#combine and split
print(np.concatenate((a,b)))
print(np.concatenate((a,b),axis=1))
print(np.split(a, 2)) #splits arr into 3 sub-arrays
print(np.hsplit(b, 2)) #splits arr horizontally on the 2nd index

#indexing/slicing/subsetting
print(np.array([1,2,3])[0])
print(a[1,1])
a[1,1] = 10 #a[0] = 4
print(a[0:3])
print(a[0:2,1])
print(a[:1])
print(a[:,1])
print(a<5)
print((a<3) & (a>5))
print(a[a<5])

#math
print(np.add(a,1))
print(np.subtract(a,2))
print(np.multiply(a,3))
print(np.divide(a,4))
print(np.power(a,5))

#vector math
c = np.array([(2,2),(2,2)])
print(c)
print(np.add(a,c))
print(np.subtract(a,c))
print(np.multiply(a,c))
print(np.divide(a,c))
print(np.power(a,c))
print(np.array_equal(a,c))
print(np.sqrt(a))
print(np.sin(a))
print(np.log(a))
print(np.abs(a))
print(np.ceil(a))
print(np.floor(a))
print(np.round(a))

print(np.mean(a,axis=0))
print(a.sum())
print(a.min())
print(a.max(axis=0))
print(np.var(a))
print(np.std(a,axis=1))
#print(a.corrcoef())