# Function
def sum_numbers(x, y):
    value = x + y
    return value

z1 = sum_numbers(22, 55)
print(z1)
z2 = sum_numbers(232, 33)
print(z2)

# Keyword arguments
def calc_sales(price, unit, tax):
    return (price * unit) * tax

sales1 = calc_sales(price=1000, unit=2, tax=1.1)
print(sales1)

# Variable length arguments
def func(x, y, *args):
    print(f"first:{x}")
    print(f"second:{y}")
    if args:
        print(f"after third:{args}")

func(1, 2, 3, 4, 5)

# Variable length keyword arguments
def func(x, y, **kwargs):
    print(f"x:{x}")
    print(f"y:{y}")
    if kwargs:
        print(f"kwargs:{kwargs}")

func(x=1, y=2, a=3, b=4)

# List type arguments
def func(x, y, z):
    print(x, y, z)
    return x + y + z

params = [1, 2, 3]
ans = func(*params)
print(ans)

# Dict type arguments
def func(x, y, z):
    print(x, y, z)
    return x + y + z

params = {"x":1, "y":2, "z":3}
ans = func(**params)
print(ans)