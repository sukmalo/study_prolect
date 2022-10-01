from math import radians
from statistics import median
import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import face

def desc(arr, nvals = 5):
    lvls = np.linspace(arr.min(), arr.max(), nvals)
    for i in range(len(lvls) - 1):
        lmin, lmax = lvls[i], lvls[i+1]
        pos = np.logical_and(arr >= lmin, arr < lmax)
        arr[pos] = lmin

def block_mean(image, by_size = 8, bx_size = 8):
    result = image.copy()
    
    for y in range(0, image.shape[0], by_size):
        for x in range(0, image.shape[1], bx_size):
            sub = result[y:y+by_size, x:x+bx_size]
            sub[:] = np.mean(sub)
            #count += 1
        
    
    return result


image = face(True)

plt. subplot(121)
plt.imshow(image )
plt.subplot(122)
dimage = image.copy()
res = block_mean(dimage, 32, 32)
plt.imshow(res)
plt.show()

# count = 1

# for x in range(0, image.shape[0], 25):
#     for y in range(0, image.shape[1], 25):
#         sub = image[y:y+25, x:x*25]
#         sub[:] = count
#         count += 1



# image = np.zeros((100,100))

# for y in range(image.shape[0]):
#     for x in range(image.shape[1]):
#         image[y,x] = np.sin(np.deg2rad(x * 5)) + np.cos(np.deg2rad(y))
        
# plt.imshow(image, cmap = "BuPu")
# plt.show()


# t = np.linspace(-4 * np.pi, 4 * np.pi, 300)
# cs = np.cos(2 * t)
# sn = 4 * np.sin(t)
# plt.plot(t, cs, label = "$cos$" )
# plt.plot(t, sn, label = "$sin$" )
# plt.legend()
# plt.show()



# x = np.arange(-10, 10.2, 0.2)
# a, b, c = 2, 3, 1

# y = a + b * x + c

# ys = []
# for i in range( 1, 6 ):
#     ys.append( x ** i )

# plt.figure(figsize = ( 10, 5 ))
# plt.subplot( 121 )
# plt.plot( x, y )
# plt.subplot( 122 )
# for i, y in enumerate(ys):
#     plt.plot( x, y, label = f"$y_{i} = x^{i}$")
# plt.legend()




