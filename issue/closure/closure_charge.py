
def charge(price):
    def calc(num):
        return price * num
    return calc

child = charge(1000)
adult = charge(1500)

price1 = child(2)
price2 = adult(2)
print(price1)
print(price2)
