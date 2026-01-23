'''
Data types:
1.Fundamental:
    int,float,complex,boolean,string

2.Collection:
    list,tuple,set,dictionary
'''
x=1
y=1.5
z=1+2j
print(x,type(x))
print(y,type(y))
print(z,type(z))

f1=3e2
f2=4E3
print(f1,type(f1))
print(f2,type(f2))

c1=4+5j
c2=complex(2,-3)
print(c1+c2)
print(c1-c2)
print(c1*c2)
print(c1/c2)

print(c1.real)
print(c1.imag)

h="JoJoDio"
print(h[2])
print(h[::])
print(h[::2])
print(h[::-1])