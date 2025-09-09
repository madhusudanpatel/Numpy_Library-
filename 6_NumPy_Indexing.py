#........................................Indexing a 2D array ( matrices)............................
import numpy as np

arr_2d=np.array(([5,10,15],[20,24,30],[35,40,45]))
print(arr_2d)

# Indexing row..................
# print(arr_2d[1])

# # Indexing items....................
# print(arr_2d[1][0])
# print(arr_2d[1,0]) # second method

#  2D Slicing..........................

print(arr_2d[:2,1:2])
 
print(arr_2d[:1,1:])

print(arr_2d[:2,1:])

#..........................................Fanciny Indexing...........................
arr2d=np.zeros((8,10))

print(arr2d)
arr_lenght=arr2d.shape[0] #[row=0,column=1]
print(arr_lenght)

# Setting Up Array......................

for i in range(arr_lenght):
    arr2d[i]=[i]
    print(arr2d[i])
    
print(arr2d[[2,4,6]])    



# ..........................................Selection .........................................

arr =np.arange(1,11)
print(arr)

bool_arr=arr>4
print(bool_arr)

print(arr[bool_arr])
    
        