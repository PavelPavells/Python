import random

print("Hello World");
if 5 < 2:
    print("Yes, Five more two")
else:
    print("No, Five less two");
x, y, z = "Orange", "Purple", "Apple"
d = 5
print(type(x))
print(y)
print(z)
print(type(d))
print("Hello, " + z)
#print(z + d);
x = 1
def myFunc():
    global x
    x = "fantastic"
    print("Python is " + x)
myFunc()
print(x)
x = str("Hello World")
x = int(20)
x = float(20.5)
x = complex(1j)
x = list(("apple", "banana", "cherry"))
x = tuple(("apple", "banana", "cherry"))
x = range(6, 12)
x = 3 + 5j
print(x)
x = 1
#x = bytesarray(x)
print(x)
print(random.randrange(1, 15))
a = "Hello World"
print(a[6])
print(a[8:10])
print(len(a))
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

