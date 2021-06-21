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
print (text1)
print (text2)

