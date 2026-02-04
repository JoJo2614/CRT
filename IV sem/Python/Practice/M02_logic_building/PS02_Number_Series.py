'''#1.Print n natural numbers
n=int(input())
for i in range(1,n+1):
    print(i)

#2.print n even numbers
n=int(input())
for i in range(2,n+1,2):
    print(2*i)

#3.print n odd numbers
n=int(input())
for i in range(1,n+1,2):
    print(i)

#4.print n fibonacci series
n=int(input())
a,b=0,1
for i in range(n):
    print(a,end=' ')
    c=a+b
    a,b=b,c

#5.multiplication table
n=int(input())
for i in range(n):
    print(n,'x',i,'=',n*i)
#6.print the square of first n natural numbers
n=int(input())
for i in range(1,n+1):
    print(i*i)
#7.cube
n=int(input())
for i in range(1,n+1):
    print(i*i*i)
#8.alternative series
n = int(input("Enter n: "))
odd = 1
even = 2
for i in range(n):
    if i % 2 == 0:
        print(odd, end=" ")
        odd += 2
    else:
        print(-even, end=" ")
        even += 2
'''
