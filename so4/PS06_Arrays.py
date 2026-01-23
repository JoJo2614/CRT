'''
Arrays:
1. List --> Built-in data structure
    a.List is mutable
    b.We use [] to define a list
    c.List is heterogeneous
    d.List is indexed
    e.List is ordered
    f.List allows duplicate values
    
2. Array using array module
3. Array using numpy module

'''

Arr = [10, 20.5, True, 10,"Hello", 20+5j]
print(Arr,type(Arr),len(Arr))

#To update an element
Arr[2] = False
print(Arr)

#To add an element
Arr.append("World")
print(Arr)

Arr.insert(1,67)
print(Arr)

Arr.extend([367,467,567])
print(Arr)