import numpy as np

# my_list=[1,3,4,]
# print(my_list)
# print(type(my_list))

# #.....................................Converted into  Array .......................
# print(np.array(my_list))

# nested_list =[[1,2,3],[4,5,6],[7,8,9]]
# print(nested_list)

# print(np.array(nested_list))


#....................................Built_in Method ...............................

#.......................There are several bulit in metheod to generation arrays.................

#............arrange() -Methods

# print(np.arange(0,10)) 
# print(np.arange(0,10,2))

# #...................................Zero and Ones..............................

# #.............Generation arrays of zeros and ones......................

# print(np.zeros(3))

# print(np.zeros((5,5)))

# print(np.ones(5))
# print(np.ones((4,6)))

# #...................................Linspace..................................

# print(np.linspace(0,10,3))

# print("LineSpce :",np.linspace(0,10,50))



#.....................................Eyes...................................
# print(np.eye(5))
# print(np.eye(2,3))



#.....................................Random..........................................

#...............Rand..................................................................
print(np.random.rand(5))

print(np.random.rand(5,6))


#...............Randn..............................................................

print(np.random.randn(2))

print(np.random.randn(5,6))


#...............Randint...............................................................
# return random integer from low (incluisive ) to high(exclusive)

# print(np.random.randint(1,100 ))

# print(np.random.randint(1,100,10))


# #.............................................Aray attributes and Methods.........................   
# arr=np.arange(25)
# ranarr=np.random.randint(0,50,10)
# print(arr)

# #............................................Reshape...............................

# #it return a array contentaing the same data with shape

# print(arr.reshape(5,5))

# #..........................................Max,Min,  argmax, argmin........................
# print(ranarr.max(),type(ranarr.max()))

# print(ranarr.min())
# print(ranarr.argmax())
# print(ranarr.argmin())

#..........................................Shape..............................................

# # shape is an attribute the array have ( not meethod)
# print(arr.shape)
# print(ranarr.shape)

# print(arr.reshape(5,5).shape)

# print(arr.reshape(25,1))
# print(arr.reshape(25,1).shape)