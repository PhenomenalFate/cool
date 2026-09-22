a=[1,2,3,'abc','@#$','rahul','rohit']
print(a)
b=a
print(b)
print("-----------------Sliceing od]f list-----------------")
print(a[:])
print(a[2:6:2])
print(a[4])

print("-----------------updating list-----------------")
a[5]="ravi"
print(a)



print(a.pop())
print(a.pop(5))
print(a.pop(4))
print(a.pop(3))
print(a.pop(2))
print(a.pop(1))
a=b
del a[0]

