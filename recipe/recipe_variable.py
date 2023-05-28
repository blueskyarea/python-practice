# Show reserved words
from keyword import kwlist
print(kwlist)

# None
a = None
if a is None:
    print(a)

# Floating point
x = 0.1
y = 1.6
z = x + y
print(z)

# Floating point2
x = 1e-1
y = 1.6e+0
z = x + y
print(z)

# Infinity
x = float("inf")
y = float("inf")

ans1 = x - 100
ans2 = x + y

print(ans1)
print(ans2)

# Not a Number
x = float("inf")
y = -float("inf")

ans1 = x + y
ans2 = x / y

print(ans1)
print(ans2)

# Surround by triple quote
text = """
Is this your pen?
This is his pen.
"""

print(text)

# raw characters
text1 = "This\nis\this\npen."
text2 = r"This\nis\this\npen."
print(text1)
print(text2)

# Check length of characters
text = "Hello. This is python recipe for beginner. Nice to meet you."
print(len(text))

# List
l1 = [3, 7, 15]
l2 = [1, "hoge", 99]
l3 = []
l4 = list('example')
l5 = list()
print(l1)
print(l2)
print(l3)
print(l4)
print(l5)

# Access to element from last
l = ["A", "B", "C"]
print(l[-1])
print(l[-2])
print(l[-3])

# slice
l = [0,1,2,3,4,5,6,7,8,9,10]
print(l[0:5])
print(l[7:8])
print(l[0:11:3])
print(l[:11:3])
print(l[0::3])
print(l[::3])
print(l[0:10])
print(l[0:-1])

# Length of list
l = [0,1,2,3,4,5,6,7,8,9,10]
print(len(l))

# Add element to list
l = ["ball", "goal"]
l.append("shoot")
print(l)
l.insert(2, "run")
print(l)

# Remove element from list
l = ["ball", "goal", "run", "shoot", "run"]
del l[1]
print(l)

l.remove("run")
print(l)

l.pop(1)
print(l)

# Search index number
l = ["ball", "goal", "run", "shoot", "run"]
idx = l.index("run")
print(idx)

# Tuple
t1 = ()
t2 = (1, 2)
t3 = "A", "B", "C"
print(t1)
print(t2)
print(t3)

# List to Tuple
l = ["ball", "goal", "run", "shoot", "run"]
t4 = tuple(l)
print(t4)

# Refer tuple element
t = "A", "B", "C", "D", "E"
print(t[2])
print(t[2:4])
print(len(t))