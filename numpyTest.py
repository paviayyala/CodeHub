import numpy
import matplotlib.pyplot as plt

x = numpy.random.uniform(0.0, 5.0, 100000)

plt.hist(x, 100)
plt.show()


#Execution time for both Vectorized and Non-vectorized versions. 
 
import time
 
a = np.random.rand(10000000)
b = np.random.rand(10000000)
 
x = time.time()
c = np.dot(a,b)
y = time.time()
 
print(c)
print("Vectorized version: " + str(1000*(y-x))+ "ms")
 
 
c = 0
x = time.time()
for i in range(10000000):
    c+= a[i] * b[i]
y = time.time()
 
print(c)
print("Non-vectorized version: " + str(1000*(y-x))+"ms")
