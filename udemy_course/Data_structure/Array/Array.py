# import array as arr
from array import array

val = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9])
# val= array('u',['a', 'b', 'c'])

# Print using index
# for i in range(0, len(val)):
#     print(val[i], end=' ')

# print()  # New line

# # Print using direct iteration
# for x in val:
#     print(x, end=', ')

# print(val.typecode)
   
# val.reverse()
# for x in val:
#     print(x, end=', ')

# insert function

# val.insert(1, 50)
# val.append(100)
# val[2] = 200

# print()

copyArray = array(val.typecode, (x*3 for x in val))

# copyArray.pop()
# copyArray.remove(15)

# for i in range(0, len(copyArray)):
#     print(copyArray[i], end=' ')

# print(val)

# trimArray = val[2 : -3]
# trimArray = val[::-1]


# arr= array('i', [])

# n = int(input('enter a number: '))

# for i in range(0, n):
#     arr.append(int(input('Enter next input: ')))

# for x in arr:
#     print(x, end=' ')


# for i in range(0, len(trimArray)):
#     print(trimArray[i], end=' ')

arr=array('i', [12, 23, 45, 234, 134, 235])

i = arr.index(234)

print('index of the number: ', i )